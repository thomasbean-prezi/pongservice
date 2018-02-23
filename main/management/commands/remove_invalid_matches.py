from django.core.management.base import BaseCommand, CommandError
from main.models import Match
from main.helpers import remove_invalid_matches, get_invalid_matches


class Command(BaseCommand):
    help = "Removes invalid matches"

    def add_arguments(self, parser):
        parser.add_argument('--dry-run',
                            action='store_true',
                            dest='dry_run',
                            default=False,
                            help='Returns what matches would be deleted if this managemment command would run')

    def handle(self, *args, **options):
        if options['dry_run']:
            invalid_match_ids = get_invalid_matches()
            self.stdout.write("Match.objects.get(pk=<id>).delete() will be called on each of these ids: %s" % invalid_match_ids)
        else:
            invalid_match_ids = remove_invalid_matches()
            self.stdout.write("Successfully removed invalid matches with these ids: %s" % invalid_match_ids)
