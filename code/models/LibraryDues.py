class LibraryDues:
    def __init__(self, roll_no, book_id, start_date, return_date, amount_due):
        self.roll_no = roll_no
        self.book_id = book_id
        self.start_date = start_date
        self.return_date = return_date
        self.amount_due = amount_due
        db = dbc.register_database()
        db.createTable('''
            CREATE TABLE IF NOT EXISTS LIB_DUES (roll_no varchar(50),
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
        
    
