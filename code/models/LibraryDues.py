from ..helper import db_connector as dbc

class LibraryDues:
    def __init__(self, roll_no, book_id, start_date, return_date, amount_due):
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS LIB_DUES (roll_no varchar(50),
                                        book_id varchar(50),
                                        start_date varchar(25),
                                        return_date varchar(25),
                                        amount_due varchar(25)); 
                                                                ''')
        
    def insert(self, data):
        db = dbc.register_database()
        query = "INSERT INTO LIB_DUES("
        for i in data:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in data:
            query += "'" + str(data[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)
        print("Successfully inserted lib_dues")
        
    def select(self, roll_no, book_id):
        db = dbc.register_database()
        query = "SELECT * FROM LIB_DUES WHERE rollNo = '" + roll_no + "' AND book_id = '" + book_id + "';"
        row = db.select(query, None)
        
        s = { "roll_no": row[0], "book_id": row[1], "start_date": row[2], "return_date" : row[3], "amount_due" : row[4]}
        
    
    
