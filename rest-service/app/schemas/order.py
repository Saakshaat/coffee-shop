from enum import Enum
from dataclasses import dataclass

class Item(str, Enum):
    expresso = 'Expresso'


@dataclass
class OrderPost:
    item: Item

@dataclass
class OrderGet:
    id: int
    wait_time: int # seconds
