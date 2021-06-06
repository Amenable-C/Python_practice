# A student is also a person

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, id, major):
        super().__init__(name, age)
        self.id = id
        self.major = major

    def show_info(self):
        super().show_info()
        print(self.id, self.major)



person = Person("Sung Choon-hyang", 20)
person.show_info()
student = Student("Lee Mong-ryong", 22, "202055526", "Computer Engineering")
student.show_info()




