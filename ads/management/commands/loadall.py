import os

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = 'fixtures'
    loaddata_command = 'loaddata'
    filenames = [
        'ad.json',
        'category.json',
        'location.json',
        'user.json'
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(self.loaddata_command, os.path.join(self.fixtures_dir, fixture_filename))
