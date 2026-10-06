class Student:

    def __init__(self):
        self.__marks = 80

    def show_marks(self):
        print("Marks =", self.__marks)


s = Student()

s.show_marks()