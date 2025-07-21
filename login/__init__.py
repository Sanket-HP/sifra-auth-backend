import azure.functions as func
import json
from utils.user_utils import verify_user

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        email = data['email']
        password = data['password']

        result = verify_user(email, password)
        return func.HttpResponse(json.dumps(result), mimetype="application/json")

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
