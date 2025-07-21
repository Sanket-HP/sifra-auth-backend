import logging
from azure.data.tables import TableServiceClient
import os
import uuid

try:
    conn_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    table_client = TableServiceClient.from_connection_string(conn_str).get_table_client("Users")
    logging.info("Connected to Azure Table Storage")
except Exception as e:
    logging.error(f"Failed to connect to Table Storage: {str(e)}")

def user_exists(email):
    try:
        entities = table_client.query_entities(f"PartitionKey eq 'User' and email eq '{email}'")
        return any(entities)
    except Exception as e:
        logging.error(f"user_exists error: {str(e)}")
        return False

def create_user(full_name, email, role, hashed_pw):
    try:
        entity = {
            "PartitionKey": "User",
            "RowKey": str(uuid.uuid4()),
            "full_name": full_name,
            "email": email,
            "role": role,
            "hashed_password": hashed_pw
        }
        table_client.create_entity(entity)
        logging.info(f"User {email} created")
    except Exception as e:
        logging.error(f"create_user error: {str(e)}")
        raise
