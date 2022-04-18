from ..helper import db_connector as dbc
 

class Course:
    def __init__(self):
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS COURSE (courseid varchar(50),
                                        rollNo varchar(25) NOT NULL PRIMARY KEY,
                                        exam varchar(25)); 
                                                        ''')
    def insert(self, data):
        db = dbc.register_database()
        query = "INSERT INTO COURSE("
        for i in data:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in data:
            query += "'" + str(data[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)
        print("Successfully inserted COURSE")