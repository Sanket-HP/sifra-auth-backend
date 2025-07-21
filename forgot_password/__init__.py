import azure.functions as func
from utils.email_utils import send_reset_email

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        email = data["email"]

        send_reset_email(email)
        return func.HttpResponse("Reset email sent", status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
