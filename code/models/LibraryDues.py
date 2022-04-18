from ..helper import db_connector as dbc

class LibraryDues:
    # Sample 
    # l = LibraryDues(roll_no = 1, book_id = 1, start_date = '2022-03-11', return_date='2022-03-19', amount_due = '123')
    # l.insert()
    # l.select(1)

    def __init__(self, roll_no, book_id, start_date, return_date, amount_due):
        self.roll_no = roll_no
        self.book_id = book_id
        self.start_date = start_date
        self.return_date = return_date
        self.amount_due = amount_due

        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS LIB_DUES (roll_no varchar(50),
                                        book_id varchar(50),
                                        start_date date,
                                        return_date date,
                                        amount_due varchar(25)); 
                                                                ''')
        
    def insert(self):
        db = dbc.register_database()
        items = self.__dict__
        query = "INSERT INTO LIB_DUES("
        for i in items:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in items:
            query += "'" + str(items[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)
        
    def select(self, roll_no, book_id):
        db = dbc.register_database()
        query = "SELECT * FROM LIB_DUES WHERE rollNo = '" + str(roll_no) + "' AND book_id = '" + str(book_id) + "';"
        row = db.select(query, None)
        
        s = { "roll_no": row[0], "book_id": row[1], "start_date": row[2], "return_date" : row[3], "amount_due" : row[4]}
        
    
    
