from enum import Enum
from dataclasses import dataclass

class Type(str, Enum):
    coffee = 'Coffee'

class Item(str, Enum):
    expresso = 'Expresso'


@dataclass
class OrderPost:
    item: Item
    type: Type

@dataclass
class OrderGet:
    id: int
    item: Item
    type: Type
    wait_time: int # seconds
