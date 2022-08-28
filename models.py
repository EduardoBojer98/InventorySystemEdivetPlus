from dataclasses import dataclass
import string

@dataclass
class UserModel:
    ID: int
    UserName: string
    Password: string


@dataclass
class ItemModel:
    ID: int
    Name: string
    Price: float
    Quantity: int
    Manufacturer: string