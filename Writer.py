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

    def __init__(self, card_id_number, supply_id: int):
        self.ci: int = card_id_number
        self.si: int = supply_id


while True:
    sleep(1)
    card_id = read()
    print(card_id[0])
    test = Card(1, 1)
    json_card = json.dumps(test.__dict__)
    print(json.dumps(test.__dict__))
    # write(json_card)
