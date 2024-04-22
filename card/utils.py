import requests
import logging
from .models import Card

logging.basicConfig(filename='exception.log', level=logging.ERROR)

def fetch_and_insert_data():
    url_template = "https://api.pokemontcg.io/v2/cards/xy1-{number}"
    for number in range(1, 151):
        url = url_template.format(number=number)
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Data for number {number} not found.")
            continue
        try:
            data = response.json().get('data', {})
            card_number = data.get('number', None)
            if Card.objects.filter(numbers=card_number).exists():
                print(f"Card with number {card_number} already exists. Skipping insertion.")
                continue
            card = Card(
                numbers=card_number,
                name=data.get('name', None),
                subtypes=', '.join(data.get('subtypes', [])),
                rules=', '.join(data.get('rules', [])),
                attack_names=', '.join([attack['name'] for attack in data.get('attacks', [])])
            )
            card.save()
            print(f"Data for number {number} inserted successfully.")
        except Exception as e:
            error_msg = f"Error inserting data for number {number}: {e}"
            print(error_msg)
            logging.error(error_msg)




# ---------------------------------------------
# django-admin startproject caseStudy
# django-admin startapp cards
# python -m venv venv
# .\venv\Scripts\Activate
# python manage.py fetch_data
# ---------------------------------------------




# import asyncio
# import aiohttp
# from asgiref.sync import sync_to_async
#
# from .models import Card
#
# async def fetch_card_data(session, number):
#     url_template = "https://api.pokemontcg.io/v2/cards/xy1-{number}"
#     url = url_template.format(number=number)
#     async with session.get(url) as response:
#         if response.status == 404:
#             print(f"Data for number {number} not found.")
#             return None
#         try:
#             data = await response.json()
#             return data.get('data', None)
#         except Exception as e:
#             print(f"Error processing data for number {number}: {e}")
#             return None
#
# async def process_card_data(number):
#     async with aiohttp.ClientSession() as session:
#         card_data = await fetch_card_data(session, number)
#         if card_data:
#             card_number = card_data.get('number', None)
#             exists_async = sync_to_async(Card.objects.filter(numbers=card_number).exists)
#             exists = await exists_async()
#             if not exists:
#                 card = Card(
#                     numbers=card_number,
#                     name=card_data.get('name', None),
#                     subtypes=', '.join(card_data.get('subtypes', [])),
#                     rules=', '.join(card_data.get('rules', [])),
#                     attack_names=', '.join([attack['name'] for attack in card_data.get('attacks', [])])
#                 )
#                 try:
#                     await sync_to_async(card.save)()
#                     print(f"Data for number {number} inserted successfully.")
#                 except Exception as e:
#                     print(f"Error saving data for number {number}: {e}")
#             else:
#                 print(f"Skipping insertion because number {number} already exists.")
#
# async def fetch_and_insert_data():
#     tasks = []
#     for number in range(1, 151):
#         tasks.append(process_card_data(number))
#     await asyncio.gather(*tasks)
#
# # To run the fetch and insert process
# async def main():
#     await fetch_and_insert_data()
#
# if __name__ == "__main__":
#     asyncio.run(main())
