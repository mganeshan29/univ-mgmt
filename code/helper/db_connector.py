import mysql.connector

class register_database:
    def __init__(self):
        self.con1=mysql.connector.connect(host='localhost', user='admin', password='password',database='univmgmt')
        self.cursor1=self.con1.cursor()

    def createTable(self, query):
        self.cursor1.execute(query)
        self.con1.commit()

    def insert(self,query):
        self.cursor1.execute(query)
        self.con1.commit()

    def select(self,query,values):
        self.cursor1.execute(query,values)
        row=self.cursor1.fetchone()
        self.con1.commit()
        return row

    def update(self,query,value):
        self.cursor1.execute(query,value)
        self.con1.commit()

    def delete(self,query,value):
        self.cursor1.execute(query,value)
        self.con1.commit()

    def selectAll(self,query):
        self.cursor1.execute(query)
        row = self.cursor1.fetchall()
        self.con1.commit()
        return row
