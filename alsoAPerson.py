# A Student is Also a Person
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print("Name =", self.name)
        print("Age =", self.age)



class Student(Person):
    def __init__(self, name, age, ID, major):
        super().__init__(name, age)
        self.ID= ID
        self.major = major
    def show_info(self):
        super().show_info()
        print("ID =", self.ID)
        print("Major= ", self.major)

person = Person("Sung Choon-hyang", 20)
person.show_info()
student = Student("Lee Mong-ryong", 22, "202055526", "Computer Engineering")
student.show_info()

