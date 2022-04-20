from ..helper import db_connector as dbc

class Book:
    # Sample 
    # b = Book(title = "Maths", author = "Bharani", id = 19, edition = "1st", publisher = "Britannica", publishDate = "2001-10-20")
    # b.insert()
    # b.select(19)
    
    def __init__(self, title = '', author= '', id = '', edition = '', publisher = '', publishDate = ''):
        self.title = title
        self.author = author
        self.id = id
        self.edition = edition
        self.publisher = publisher
        self.publishDate = publishDate

        self.createTable()
    
    def __repr__(self) -> str:
        return f"{self.title} by {self.author}"

    def createTable(self):
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS BOOKS (title varchar(50),
                                        author varchar(50),
                                        id varchar(25) NOT NULL PRIMARY KEY,
                                        edition varchar(25),
                                        publisher varchar(25),
                                        publishDate date);
                                                        ''')

    def select(self):
        db = dbc.register_database()
        query = "SELECT * FROM BOOKS WHERE id = '" + str(self.id) + "';"
        row = db.select(query, None)
        b = Book(title = row[0], author = row[1] ,id = row[2], edition = row[3], publisher = row[4], publishDate = row[5])
        return b
    
    def selectAll(self):
        db = dbc.register_database()
        query = "SELECT * FROM BOOKS;"
        rows = db.selectAll(query)
        return rows
    
    def insert(self):
        db = dbc.register_database()
        items = self.__dict__
        query = "INSERT INTO BOOKS("
        for i in items:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in items:
            query += "'" + str(items[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)
    
    def deleteBook(self, id):
        db = dbc.register_database()
        query = "DELETE FROM BOOKS WHERE id = '" + id + "';"
        db.delete(query)
        print("Successfully deleted BOOK")