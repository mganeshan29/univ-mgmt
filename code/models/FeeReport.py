from ..helper import db_connector as dbc

class FeeReport:    
    def __init__(self):
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS FEEREPORT (roll varchar(50),
                                        receipt varchar(25)  NOT NULL PRIMARY KEY,
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
        rows = db.selectAll(query)
        return rows
    
    def selectReceipt(self, receipt):
        db = dbc.register_database()
        query = "SELECT * FROM FEEREPORT WHERE receipt = '" + receipt + "';"
        rows = db.selectAll(query)
        return rows
    
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
        
    def selectAll(self):
        db = dbc.register_database()
        query = "SELECT * FROM FEEREPORT;"
        rows = db.selectAll(query)
        return rows
    
    def deleteReceipt(self, receipt):
        db = dbc.register_database()
        query = "DELETE FROM FEEREPORT WHERE receipt = '" + receipt + "';"
        db.delete(query, None)
        print("Deletion was successful");