from django.core.management.base import BaseCommand
from userauth.models import SignUp


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not SignUp.objects.filter(username="admin").exists():
            SignUp.objects.create_superuser("admin", "admin@admin.com", "admin")
