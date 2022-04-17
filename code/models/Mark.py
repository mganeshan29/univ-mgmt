class Mark:
    def __init__(self, exam, role_no, marks, pass_marks, total):
        self.exam = exam
        self.role_no = role_no
        self.marks = marks
        self.pass_marks = pass_marks
        self.total = total
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS MARKS (name varchar(50),
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

        