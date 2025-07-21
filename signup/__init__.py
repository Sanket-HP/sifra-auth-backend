import logging
import azure.functions as func
import json
from utils import db  # Make sure 'utils' is inside the SignupFunction folder

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Signup function triggered")

    try:
        req_body = req.get_json()
        full_name = req_body.get("full_name")
        email = req_body.get("email")
        password = req_body.get("password")
        role = req_body.get("role", "user")

        if not all([full_name, email, password]):
            return func.HttpResponse(
                json.dumps({"error": "Missing required fields"}),
                status_code=400,
                mimetype="application/json"
            )

        if db.user_exists(email):
            return func.HttpResponse(
                json.dumps({"error": "User already exists"}),
                status_code=409,
                mimetype="application/json"
            )

        db.create_user(full_name, email, role, password)

        return func.HttpResponse(
            json.dumps({"message": "User created successfully!"}),
            status_code=201,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Signup error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Internal Server Error", "details": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
