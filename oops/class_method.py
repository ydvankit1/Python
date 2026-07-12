class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):  # cls refer to the class student
        cls.school = new_school

# Before change
print(Student.school)

# Change class variable
Student.change_school("XYZ School")

print(Student.school)