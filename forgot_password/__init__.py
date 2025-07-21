import azure.functions as func
from utils.email_utils import send_verification_email

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        email = data["email"]

        # Construct the reset link
        reset_link = f"https://sifra-app.com/reset-password?email={email}"

        # Send the email
        send_verification_email(
            to_email=email,
            subject="Sifra AI - Reset Your Password",
            html_content=f"<p>Click <a href='{reset_link}'>here</a> to reset your password.</p>"
        )

        return func.HttpResponse("Reset email sent", status_code=200)

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
