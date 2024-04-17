import requests
from .models import Card

def fetch_and_insert_data():
    url_template = "https://api.pokemontcg.io/v2/cards/xy1-{number}"
    cards_to_insert = []
    for number in range(1, 151):
        url = url_template.format(number=number)
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Data for number {number} not found.")
            continue
        try:
            data = response.json().get('data', {})
            card_number = data.get('number', None)
            if not Card.objects.filter(numbers=card_number).exists():
                card = Card(
                    numbers=card_number,
                    name=data.get('name', None),
                    subtypes=', '.join(data.get('subtypes', [])),
                    rules=', '.join(data.get('rules', [])),
                    attack_names=', '.join([attack['name'] for attack in data.get('attacks', [])])
                )
                cards_to_insert.append(card)
            else:
                print(f"Skipping insertion because number {number} already exists.")
        except Exception as e:
            print(f"Error processing data for number {number}: {e}")

    # Bulk insert the cards
    try:
        Card.objects.bulk_create(cards_to_insert)
        print("Bulk insertion completed successfully.")
    except Exception as e:
        print(f"Error bulk inserting data: {e}")
