from . import register_database

class populate_db:
    TABLES = ['student', 'faculty', 'course', 'book', 'mark', 'library_dues', 'librarian', 'teacher', 'admin', 'fee_report', 'library']

    def __init__(self):
        self.conn = register_database()