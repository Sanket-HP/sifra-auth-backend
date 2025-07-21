from azure.data.tables import TableServiceClient, TableEntity
import os
import uuid

conn_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
table_client = TableServiceClient.from_connection_string(conn_str).get_table_client("Users")

def user_exists(email):
    entities = table_client.query_entities(f"PartitionKey eq 'User' and email eq '{email}'")
    return any(entities)

def create_user(full_name, email, role, hashed_pw):
    entity = {
        "PartitionKey": "User",
        "RowKey": str(uuid.uuid4()),
        "full_name": full_name,
        "email": email,
        "role": role,
        "hashed_password": hashed_pw
    }
    table_client.create_entity(entity)