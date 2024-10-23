from dotenv import dotenv_values
from supabase import create_client, Client
import Scanner
import Database
import time


def main():
    config = dotenv_values(".env")
    url = config.get("SUPABASE_URL")
    anon_key = config.get("SUPABASE_ANON_KEY")
    secret_key = config.get("SUPABASE_SECRET_KEY")

    supabase_client_secret: Client = create_client(url, secret_key)
    supabase_client_anon: Client = create_client(url, anon_key)

    while True:
        time.sleep(1)
        data = Scanner.read()
        print(data)
        # Database.add_entries_to_inventory_table(supabase_client_secret, data)
        Scanner.cleanup()

if __name__ == '__main__':