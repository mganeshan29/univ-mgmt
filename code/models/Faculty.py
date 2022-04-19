from ..helper import db_connector as dbc

class Faculty:
    def __init__(self):
      db = dbc.register_database()
      db.createTable('''
            CREATE TABLE IF NOT EXISTS FACULTY (name varchar(50),
                                        id varchar(25) NOT NULL PRIMARY KEY,
                                        roles varchar(25),
                                        phone_no varchar(25),
                                        address varchar(25),
                                        email varchar(50),
                                        dob varchar(10),
                                        gender varchar(15), 
                                        password varchar(40)); 
                                                                ''')

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
      print("Successfully inserted the teacher")

    def authenticate(self, id, password):
      db = dbc.register_database()
      query = "SELECT * FROM FACULTY WHERE id = '" + id + "' AND password = '" + password + "';"
      row = db.select(query, None)
      if row:
        s = {}
        s["name"] = row[0]
        s["id"] = row[1]
        s["roles"] = row[2]
        s["phone_no"] = row[3]
        s["address"] = row[4]
        s["email"] = row[5]
        s["dob"] = row[6]
        s["gender"] = row[7]
        s["password"] = row[8]
        return s
      else:
        return None
      
    def select(self, id):
        db = dbc.register_database()
        query = "SELECT * FROM FACULTY WHERE id = '" + id + "';"
        row = db.select(query, None)
        s = {}
        s["name"] = row[0]
        s["id"] = row[1]
        s["roles"] = row[2]
        s["phone_no"] = row[3]
        s["address"] = row[4]
        s["email"] = row[5]
        s["dob"] = row[6]
        s["gender"] = row[7]
        s["password"] = row[8]
        return s
      
    
    

    
    
