from django.core.management import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = "Send example email hello"
    
    def handle(self, *args, **options):
        self.stdout.write("Send email")
    
        send_mail(
        "Welcom Subject",
        "This is message body! Glad to see you.",
        "admin@admin.com",
        ["recipient@example.com"],
        fail_silently=False,
        )
        self.stdout.write(self.style.SUCCESS("Email send"))