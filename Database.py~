from dotenv import dotenv_values
from supabase import create_client, Client


def read_data_from_table(supabase_client: Client, table_name: str):
    """
    This function reads data from the specified table in the database
    and returns the data that is not marked as deleted.

    Args:
        supabase_client (Client): The Supabase client used to interact with the database
        table_name (str): The name of the table to read data from

    Returns:
        dict: The data from the specified table that is not marked as deleted
    """
    data = supabase_client.table(table_name).select("*").eq("is_deleted", False).execute()
    return data.data


def add_entries_to_inventory_table(supabase_client: Client, entries: dict):
    """
    This function takes a list of entries and adds them to the inventory table in the database.

    Args:
        supabase_client (Client): The Supabase client used to interact with the database
        entries (list): The data to be inserted into the inventory table

    Returns:
        list: The data inserted into the inventory table
    """
    data = supabase_client.table('inventory').insert(entries).execute()
    return data.data


def add_entries_to_crew_table(supabase_client: Client, entries: dict):
    """
    This function takes a list of entries and adds them to the crew table in the database.

    Args:
        supabase_client (Client): The Supabase client used to interact with the database
        entries (list): The data to be inserted into the crew table

    Returns:
        list: The data inserted into the crew table
    """
    data = supabase_client.table('crew').insert(entries).execute()
    return data.data


def update_entry_in_table(supabase_client: Client, table_name: str, entry_id: int, entry_data: dict):
    """
    This function takes a table name, an entry ID, and an entry data dictionary
    and updates the entry in the specified table in the database.

    Args:
        supabase_client (Client): The Supabase client used to interact with the database
        table_name (str): The name of the table to update data in
        entry_id (int): The ID of the entry to be updated
        entry_data (dict): The updated data for the entry

    Returns:
        list: The data updated in the specified table
    """
    data = supabase_client.table(table_name).update(entry_data).eq("id", entry_id).execute()
    return data.data


def delete_entry_from_table(supabase_client: Client, table_name: str, entry_id: int):
    """
    This function takes a table name and an entry ID and marks the entry as deleted in the
    specified table in the database.

    Args:
        supabase_client (Client): The Supabase client used to interact with the database
        table_name (str): The name of the table to delete data from
        entry_id (int): The ID of the entry to be deleted

    Returns:
        list: The data deleted from the specified table
    """
    data = supabase_client.table(table_name).update({"is_deleted": True}).eq("id", entry_id).execute()
    return data.data


def main():
    """
    This function tests the functions in the Database class by creating a secret and anonymous
    Supabase client, reading data from the inventory table, adding a dummy entry, and then deleting it.
    """

    config = dotenv_values(".env")
    url = config.get("SUPABASE_URL")
    anon_key = config.get("SUPABASE_ANON_KEY")
    secret_key = config.get("SUPABASE_SECRET_KEY")

    # Create a secret and anonymous Supabase client
    supabase_client_secret: Client = create_client(url, secret_key)
    supabase_client_anon: Client = create_client(url, anon_key)

    # Read data from the inventory table using the anonymous client
    data1 = read_data_from_table(supabase_client_anon, 'inventory')
    print(data1)

    # Create a dummy entry to add to the inventory table
    dummy_data = {
        'supply_name': 'Advil2', 'crew_member_id': 2, 'dosage_taken': 6,
        'units_per_package': 48, 'quantity': 48, 'exp_date': '2024-10-25',
        'location': 'B6'
    }
    # Add the dummy entry to the inventory table using the secret client
    add_entries_to_inventory_table(supabase_client_secret, dummy_data)
    # Delete the dummy entry from the inventory table using the secret client
    delete_entry_from_table(supabase_client_secret, 'inventory', 20)


if __name__ == '__main__':
    main()
