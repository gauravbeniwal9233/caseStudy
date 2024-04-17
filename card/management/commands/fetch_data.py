from django.core.management.base import BaseCommand
from card.utils import fetch_and_insert_data

class Command(BaseCommand):
    help = 'Fetches data from API and inserts into the database'

    def handle(self, *args, **options):
        fetch_and_insert_data()
        self.stdout.write(self.style.SUCCESS('Data fetching and insertion completed successfully'))
