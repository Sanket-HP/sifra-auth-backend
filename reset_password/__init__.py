import azure.functions as func
import json
import bcrypt
from utils.db import users_collection

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        email = data.get("email")
        new_password = data.get("new_password")

        hashed_pw = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        users_collection.update_one({"email": email}, {"$set": {"password": hashed_pw}})

        return func.HttpResponse("Password reset successfully", status_code=200)

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
