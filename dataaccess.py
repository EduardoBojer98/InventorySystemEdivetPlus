import sqlite3
from models import ItemModel, UserModel


class UserRepository:
    def __init__(self):
        self.con = sqlite3.connect(database=r'ims.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS korisnici(ID INTEGER PRIMARY KEY AUTOINCREMENT, KorisnickoIme text, Lozinka text)")
        self.con.commit()
        
    def add_user(self, user: UserModel):
        try:
            self.cur.execute("Insert into korisnici (KorisnickoIme,Lozinka) values(?,?)", (
                user.UserName,
                user.Password
            ))
            self.con.commit()
        except Exception as e:
            raise Exception(f"Greska prilikom dodavanja korisnika: {str(e)}")

    def login(self, user: UserModel):
        try:
            self.cur.execute("select * from korisnici where KorisnickoIme=? AND Lozinka=?", (user.UserName, user.Password))
            user = self.cur.fetchone()
        except Exception as e:
            raise Exception(f"Greska prilikom prijave korisnika: {str(e)}")
        assert user != None, "Pogresni kredencijali"


class ItemRepository:
    def __init__(self):
        self.con = sqlite3.connect(database=r'ims.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS proizvodi(ID INTEGER PRIMARY KEY AUTOINCREMENT, Ime text, Cena real, Kolicina integer, Proizvodjac text)")
        self.con.commit()

    def add_item(self, item: ItemModel):
        try:
            self.cur.execute("Insert into proizvodi (Ime,Cena,Kolicina,Proizvodjac) values(?,?,?,?)", (
                item.Name,
                item.Price,
                item.Quantity,
                item.Manufacturer
            ))
            self.con.commit()
        except Exception as e:
            raise Exception(f"Greska prilikom dodavanja proizvoda: {str(e)}")

    def get_all(self):
        self.cur.execute("select * from proizvodi")
        rows = self.cur.fetchall()
        for row in rows:
            yield ItemModel(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
            )

    def search(self, searchType, query):
        self.cur.execute("select * from proizvodi where " + searchType + " LIKE ?", ('%'+query+'%',))
        rows = self.cur.fetchall()
        for row in rows:
            yield ItemModel(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
            )
    
    def update(self, item: ItemModel):
        try:
            self.cur.execute("Update proizvodi set Ime=?, Cena=?, Kolicina=?, Proizvodjac=? where ID=?", (
                item.Name,
                item.Price,
                item.Quantity,
                item.Manufacturer,
                item.ID
            ))
            self.con.commit()
        except Exception as e:
            raise Exception(f"Greska prilikom azuriranja proizvoda: {str(e)}")

    def delete(self, id):
        try:
            self.cur.execute('delete from proizvodi where ID=?', (id,))
            self.con.commit()
        except Exception as e:
            raise Exception(f"Greska prilikom brisanja proizvoda: {str(e)}")