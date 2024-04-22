from django.core.management.base import BaseCommand
from card.utils import fetch_and_insert_data

class Command(BaseCommand):
    help = 'Fetches data from API and inserts into the database'

    def handle(self, *args, **options):
        fetch_and_insert_data()
        self.stdout.write(self.style.SUCCESS('Data fetching and insertion completed successfully'))






# from django.core.management.base import BaseCommand
# from card.utils import fetch_and_insert_data
#
# class Command(BaseCommand):
#     help = 'Fetches and inserts card data'
#
#     def handle(self, *args, **kwargs):
#         async def run_async():
#             await fetch_and_insert_data()
#
#         import asyncio
#         asyncio.run(run_async())
#
#         self.stdout.write(self.style.SUCCESS('Data fetching and insertion completed successfully'))
