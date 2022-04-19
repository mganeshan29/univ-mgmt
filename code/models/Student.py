from ..helper import db_connector as dbc

class Student:
    def __init__(self):
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS STUDENT (name varchar(50),
                                        rollNo varchar(25) NOT NULL PRIMARY KEY,
                                        father_name varchar(25),
                                        mother_name varchar(25),
                                        phone_no varchar(25),
                                        address varchar(25),
                                        email varchar(50),
                                        dob varchar(10),
                                        gender varchar(15), 
                                        password varchar(40)); 
                                                                ''')

    # def __repr__(self) -> str:
    #     return (self.rollNo + ' ' + self.name)

    def insert(self, data):
        db = dbc.register_database()
        query = "INSERT INTO STUDENT("
        for i in data:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in data:
            query += "'" + str(data[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)
        print("Successfully inserted student")

    def select(self, rollNo):
        db = dbc.register_database()
        query = "SELECT * FROM STUDENT WHERE rollNo = '" + rollNo + "';"
        row = db.select(query, None)
        # s = { 
        # rollNo = row[0], father_name=row[1], mother_name=row[2], phone_no=row[3],
        #             address=row[4], email=row[5], dob=row[6], gender=row[7], password=row[8]}
        s = {}
        s["name"] = row[0]
        s["rollNo"] = row[1]
        s["father_name"] = row[2]
        s["mother_name"] = row[3]
        s["phone_no"] = row[4]
        s["address"] = row[5]
        s["email"] = row[6]
        s["dob"] = row[7]
        s["gender"] = row[8]
        s["password"] = row[9]
        return s

    def authenticate(self, rollNo, password):
        db = dbc.register_database()
        query = "SELECT * FROM STUDENT WHERE rollno = '" + rollNo +"' and password = '" + password + "';"
        row = db.select(query, None)
        if row:
            s = {}
            s["name"] = row[0]
            s["rollNo"] = row[1]
            s["father_name"] = row[2]
            s["mother_name"] = row[3]
            s["phone_no"] = row[4]
            s["address"] = row[5]
            s["email"] = row[6]
            s["dob"] = row[7]
            s["gender"] = row[8]
            s["password"] = row[9]
            return s
        else:
            return None
