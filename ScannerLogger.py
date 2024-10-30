from dotenv import dotenv_values
from supabase import create_client, Client
import time
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
        # Database.add_entries_in_table(supabase_client_secret, "inventory", {"crew_member_id": int(data[1])})


if __name__ == '__main__':
    main()
