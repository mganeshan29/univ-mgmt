from ..helper import db_connector as dbc

class Student:
    def __init__(self, name = "", rollNo = "", father_name = "", mother_name = "", phone_no = "", address = "", email = "", dob = "", gender = "", password = ""):
        self.name = name
        self.rollNo = rollNo
        self.father_name = father_name
        self.mother_name = mother_name
        self.phone_no = phone_no
        self.address = address
        self.email = email
        self.dob = dob
        self.gender = gender
        self.password = password

        self.createTable() # Creates table if it doesn't exist
        self.insert() # Inserts the values of the object to the table

    def __repr__(self) -> str:
        return (self.rollNo + ' ' + self.name)

    def createTable(self):
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

    def insert(self):
        db = dbc.register_database()
        items = self.__dict__
        query = "INSERT INTO STUDENT("
        for i in items:
            query += i + ","
        query = query[:-1] + ") VALUES("
        for i in items:
            query += "'" + str(items[i]) + "',"
        query = query[:-1] + ");"
        db.insert(query)

    def select(self, rollNo):
        db = dbc.register_database()
        query = "SELECT * FROM STUDENT WHERE rollNo = '" + rollNo + "';"
        row = db.select(query, None)
        s = Student(rollNo = row[0], father_name = row[1] ,mother_name = row[2], phone_no = row[3], address = row[4], email = row[5], dob = row[6], gender = row[7], password=row[8])
        return s