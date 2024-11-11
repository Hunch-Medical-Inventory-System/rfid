from flask import Flask, request
from supabase import create_client, Client
from dotenv import dotenv_values
import Database as db


app = Flask(__name__)

# Load environment variables
config = dotenv_values(".env")
url = config.get("SUPABASE_URL")
anon_key = config.get("SUPABASE_ANON_KEY")
secret_key = config.get("SUPABASE_SECRET_KEY")

# Create a secret and anonymous Supabase client
supabase_client_secret: Client = create_client(url, secret_key)
supabase_client_anon: Client = create_client(url, anon_key)


# Define the API routes
@app.route(rule='/<table_name>', methods=['GET'])
def read(table_name: str):
    """
    This function reads data from the specified table in the database
    and returns the data that is not marked as deleted.

    Args:
        supabase_client_anon (Client): The Supabase client used to interact with the database
        table_name (str): The name of the table to read data from

    Returns:
        dict: The data from the specified table that is not marked as deleted
    """
    data = db.read_data_from_table(supabase_client_anon, table_name)
    return data

@app.route(rule='/<table_name>/<entry_id>', methods=['PUT'])
def update(table_name: str, entry_id: int):
    """
    This function takes a table name, an entry ID, and an entry data dictionary
    and updates the entry in the specified table in the database.

    Args:
        supabase_client_secret (Client): The Supabase client used to interact with the database
        table_name (str): The name of the table to update data in
        entry_id (int): The ID of the entry to be updated
        entry_data (dict): The updated data for the entry

    Returns:
        str: A success message
    """
    db.update_entry_in_table(supabase_client_secret, table_name, entry_id, request.get_json())
    return '200 OK'

@app.route(rule='/<table_name>', methods=['POST'])
def insert(table_name: str):
    """
    This function takes a table name and a list of entries and adds them to the
    specified table in the database.

    Args:
        supabase_client_secret (Client): The Supabase client used to interact with the database
        table_name (str): The name of the table to insert data into
        entries (list): The data to be inserted into the specified table

    Returns:
        str: A success message
    """
    db.add_entries_in_table(supabase_client_secret, table_name, request.get_json())
    return '200 OK'

@app.route(rule='/<table_name>/<entry_id>', methods=['DELETE'])
def delete(table_name: str, entry_id: int):
    """
    This function takes a table name and an entry ID and marks the entry as deleted in the
    specified table in the database.

    Args:
        supabase_client_secret (Client): The Supabase client used to interact with the database
        table_name (str): The name of the table to delete data from
        entry_id (int): The ID of the entry to be deleted

    Returns:
        str: A success message
    """
    db.delete_entry_from_table(supabase_client_secret, table_name, entry_id)
    return '200 OK'


if __name__ == '__main__':
    app.run()
