from Scanner import write, read
from time import sleep
import json


class Supply:

    def __init__(self, category, item, strength_volume, route_use, pack_quantity, side_effects, location):
        self.category: str = category
        self.item: str = item
        self.strength_volume: str = strength_volume
        self.route_use: str = route_use
        self.pack_quantity: int = pack_quantity
        self.side_effects: str = side_effects
        self.location: str = location


class Card:

    def __init__(self, supply_id: int, expiry_date: str, ):
        self.si: int = supply_id
        self.ed: str = expiry_date


while True:
    sleep(1)
    card_id = read()
    print(card_id[0])
    print(card_id[1])
    print(json.loads(card_id[1])["si"])
    test_card = Card(1, "2022-01-01")
    json_card = json.dumps(test_card.__dict__)
    write(json_card)
