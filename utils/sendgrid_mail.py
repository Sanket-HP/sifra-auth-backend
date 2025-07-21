import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_reset_email(email, token):
    message = Mail(
        from_email='no-reply@sifraai.me',
        to_emails=email,
        subject='Sifra AI: Reset Your Password',
        html_content=f'<p>Click <a href="https://sifraai.com/reset-password?token={token}">here</a> to reset your password.</p>'
    )
    sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
    sg.send(message)
