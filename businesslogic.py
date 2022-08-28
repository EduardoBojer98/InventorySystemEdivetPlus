from dataaccess import ItemRepository, UserRepository
from models import ItemModel, UserModel


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def login(self, username, password):
        assert username != "", "Ime je obavezno"
        assert password != "", "Lozinka je obavezna"
        self.user_repository.login(UserModel(0, username, password))

    def add_user(self, username, password):
        assert username != "", "Korisnicko me je obavezno"
        assert password != "", "Lozinka je obavezna"
        self.user_repository.add_user(UserModel(0, username, password))


class ItemService:
    def __init__(self) -> None:
        self.item_repository = ItemRepository()

    def get_all(self):
        yield from self.item_repository.get_all()
    
    def add_item(self, name, price, quantity, manufacturer):
        assert name != "", "Ime je obavezno"
        assert price != "", "Cena je obavezna"
        assert quantity != "", "Kolicina je obavezna"
        assert manufacturer != "", "Proizvodjac je obavezan"

        price_value = 0.0
        try:
            price_value = float(price)
        except:
            raise Exception("Cena mora biti realna vrednost")
        
        quantity_value = 0
        try:
            quantity_value = int(quantity)
        except:
            raise Exception("Kolicina mora biti broj")
        
        self.item_repository.add_item(ItemModel(
            0,
            name,
            price_value,
            quantity_value,
            manufacturer
        ))
    
    def update(self, id, name, price, quantity, manufacturer):
        assert name != "", "Ime je obavezno"
        assert price != "", "Cena je obavezna"
        assert quantity != "", "Kolicina je obavezna"
        assert manufacturer != "", "Proizvodjac je obavezan"

        price_value = 0.0
        try:
            price_value = float(price)
        except:
            raise Exception("Cena mora biti realna vrednost")
        
        quantity_value = 0
        try:
            quantity_value = int(quantity)
        except:
            raise Exception("Kolicina mora biti broj")
        
        self.item_repository.update(ItemModel(
            id,
            name,
            price_value,
            quantity_value,
            manufacturer
        ))

    def delete(self, id):
        self.item_repository.delete(id)

    def search(self, searchType, query):
        yield from self.item_repository.search(searchType, query)
