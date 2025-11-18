class Student:
    def __init__(self, _name, _age=13, _grade="12th", subject="Computer Science"):
        self._name = _name
        self._age = _age
        self._grade = _grade
        self.subject = subject

    def __str__(self):
        return "Student 1: Name: Francisco, Age: 15, Grade: 12th"

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if new_name.length >= 3 and new_name.isalnum() and ' ' not in new_name and new_name.istitle():
            self._name = new_name

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, new_age):
        if type(new_age) == int and new_age > 11 and new_age < 18:
            self._age = new_age

    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        grade_list = ["9th", "10th", "11th", "12th"]
        if new_grade in grade_list:
            self._grade = new_grade

    def advance(self, _grade, years_advanced):
        self.years_advanced = years_advanced
        return "Francisco has advanced to the 13th grade"
    
    def study(self, subject):
        self.subject = subject
        return "Francisco is studying Computer Science"
    

student1 = Student("Sandy", 11, "12th", "Writing")


