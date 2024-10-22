import os
import json
from supabase import create_client, Client

# os.environ["SUPABASE_KEY"] ='https://xowegfmkiindptpnsscg.supabase.co'
# os.environ["SUPABASE_URL"] ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhvd2VnZm1raWluZHB0cG5zc2NnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg0OTE0MzksImV4cCI6MjA0NDA2NzQzOX0._rrgcRNIZYDMqdQaqEWgrHNvFp4jGkk-dFF4ohxroq0'

url ='https://xowegfmkiindptpnsscg.supabase.co'
key ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhvd2VnZm1raWluZHB0cG5zc2NnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyODQ5MTQzOSwiZXhwIjoyMDQ0MDY3NDM5fQ.8E6Yl8_5HuqGhB08e9FSZAAnDmXKjXnBgkK6c_GIE5E'
# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")

print(url)
print(key)

supabase_client: Client = create_client(url, key)
response = supabase_client.table("test").select("*").execute()
print(response.data)

inserted_data = {'id': 20, 'supply_name': 'Advil2', 'crew_member_id': 2, 'dosage_taken': 6, 'units_per_package': 48, 'quantity': 48, 'exp_date': '2024-10-25', 'created_at': '2024-10-14T15:15:06.515179+00:00', 'crew_member_name': 'Justin Time', 'location': 'B6'}

response2 = (
    supabase_client.table("Inventory")
    .insert(inserted_data)
    .execute()
)

# data = {"test": "test4"}
# print(data)
#
# response2 = (
#     supabase_client.table("test")
#     .insert(data)
#     .execute()
# )

print(response2)
