# Grading System with a Class
class Student:
    def __init__(self, name, midScore, finalScore):
        self.name = name
        self.midScore = int(midScore)
        self.finalScore = int(finalScore)

    def calc(self):
        self.sum = self.midScore + self.finalScore
        self.ave = self.sum / 2

    def get_name(self):
        return self.name

    def get_sum(self):
        return self.sum

    def get_ave(self):
        return self.ave

name = input("Name: ")
midScore = int(input("Midterm exam score: "))
finalScore = int(input("Final exam score: "))
student1 = Student(name, midScore, finalScore)
student1.calc()

print("Name:", student1.get_name())
print("Sum of the midterm and final exam score:", student1.get_sum())
print("Average:", student1.get_ave())

