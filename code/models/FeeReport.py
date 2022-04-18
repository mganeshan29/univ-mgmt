from ..helper import db_connector as dbc

class FeeReport:    
    def __init__(self):
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS FEEREPORT (roll varchar(50) NOT NULL PRIMARY KEY,
                                        receipt varchar(25) ,
                                        date varchar(25),
                                        branch varchar(25),
                                        sem DOUBLE,
                                        total_amt DOUBLE,
                                        paid_amt DOUBLE,
                                        due_amt DOUBLE); 
                                                        ''')

    def select(self, roll_no):
        db = dbc.register_database()
        query = "SELECT * FROM FEEREPORT WHERE roll = '" + roll_no + "';"
        row = db.select(query, None)
        print(query)
        s = {"roll": row[0], "receipt" : row[1], "date" : row[2], "branch" : row[3], "sem" : row[4], "total_amt" : row[5], "paid_amt" : row[6], "due_amt" : row[7]}
        return s
    def insert(self, data):
        db = dbc.register_database()
        query = "INSERT INTO FEEREPORT("
        for i in data:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in data:
            query += "'" + str(data[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)
        print("Successfully inserted FEEREPORT")