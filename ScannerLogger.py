from dotenv import dotenv_values
from supabase import create_client, Client
import time
import json
import Scanner
import Database


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
        print(data[0])
        print(data[1])
        supply_id, expiry_date = json.loads(data[1])["si"], json.loads(data[1])["ed"]
        Database.add_entries_in_table(supabase_client_secret,
                                      "inventory",
                                      {"card_id": int(data[0]), "supply_id": int(supply_id), "expiry_date": expiry_date})


if __name__ == '__main__':
    main()
