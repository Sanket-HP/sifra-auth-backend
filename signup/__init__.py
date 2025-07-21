import azure.functions as func
import logging
import bcrypt
import uuid
import os
import sys

# Ensure custom path is included
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from utils.db import create_user, user_exists

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("✅ Signup endpoint triggered")

    try:
        data = req.get_json()
        logging.info(f"📦 Received data: {data}")

        full_name = data.get('full_name')
        email = data.get('email')
        role = data.get('role')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Validate inputs
        if not all([full_name, email, role, password, confirm_password]):
            logging.warning("⚠️ Missing fields in request")
            return func.HttpResponse("All fields are required", status_code=400)

        if password != confirm_password:
            logging.warning("❌ Passwords do not match")
            return func.HttpResponse("Passwords do not match", status_code=400)

        if user_exists(email):
            logging.warning(f"❗User already exists: {email}")
            return func.HttpResponse("User already exists", status_code=409)

        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        create_user(full_name, email, role, hashed_pw)

        logging.info(f"✅ User '{email}' created successfully")
        return func.HttpResponse("Signup successful", status_code=201)

    except ValueError as ve:
        logging.error(f"❌ ValueError: {str(ve)}")
        return func.HttpResponse(f"Invalid input: {str(ve)}", status_code=400)

    except Exception as e:
        logging.exception("🔥 Internal server error")
        return func.HttpResponse(f"Internal Server Error: {str(e)}", status_code=500)
