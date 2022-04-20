from ..helper import db_connector as dbc

class Mark:
    def __init__(self):
        # self.exam = exam
        # self.role_no = role_no
        # self.marks = marks
        # self.pass_marks = pass_marks
        # self.total = total
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS MARKS (exam varchar(50),
                                        rollNo varchar(25) NOT NULL PRIMARY KEY,
                                        marks numeric,
                                        passMarks numeric,
                                        total numeric); 
                                                        ''')

    def insert(self, data):
        db = dbc.register_database()
        query = "INSERT INTO MARKS("
        for i in data:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in data:
            query += "'" + str(data[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)
        print("Successfully inserted MARKS")
        
    def select(self, rollNo):
        db = dbc.register_database()
        query = "SELECT * FROM MARKS WHERE rollNo = '" + rollNo + "';"
        row = db.select(query, None)
        
        s = {"exam": row[0], "rollNo" : row[1], "marks" : row[2],"passMarks": row[3], "total" : row[4]}
        return s 

    def selectAll(self):
        db = dbc.register_database()
        query = "SELECT * FROM MARKS;"
        rows = db.selectAll(query)
        listOfMarks = []
        for row in rows:
            s = {"exam": row[0], "rollNo" : row[1], "marks" : row[2],"passMarks": row[3], "total" : row[4]}
            listOfMarks.append(s)
        return listOfMarks

        