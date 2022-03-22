class Student:
    def __init__(self, name, rollNo, father_name, mother_name, phone_no, address, email, dob, gender):
        self.name = name
        self.rollNo = rollNo
        self.father_name = father_name
        self.mother_name = mother_name
        self.phone_no = phone_no
        self.address = address
        self.email = email
        self.dob = dob
        self.gender = gender

    def __repr__(self) -> str:
        return (self.rollNo + ' ' + self.name)
