from django.core.management import BaseCommand
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class Command(BaseCommand):
    help = "Send example email hello"
    
    def handle(self, *args, **options):
        self.stdout.write("Send complex email")
    
        # send_mail(
        # "Welcom Subject",
        # "This is message body! Glad to see you.",
        # "admin@admin.com",
        # ["recipient@example.com"],
        # fail_silently=False,
        # )
        name = "John Smith"
        subject = f"Welcom, {name}!" 
        sender = "admin@admin.com"
        recipient = "john@example.com"
        context = {
            "name": name,
        }
        text_content = render_to_string(
            template_name="email_newslatters/welcom_messsage.txt",
            context=context 
            )
        html_content = render_to_string(
            template_name="email_newslatters/welcom_messsage.html",
            context=context,
            )
        
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=sender,
            to=[recipient],
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
        )
        
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        self.stdout.write(self.style.SUCCESS("Complex email send"))





