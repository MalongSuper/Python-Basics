# Python Classes and Objects

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")


# Derived class
class Student(Person):
    def __init__(self, name, age, city, major):
        super().__init__(name, age, city)
        self.major = major

    def display(self):
        super().display()
        print(f"Major: {self.major}")


class Test:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")


class Bird:
    def sound(self):
        print("Chirp")


class Human:
    def sound(self):
        print("Hello")


def make_sound(obj):
    obj.sound()


# Example usage
student1 = Student("Alice", 20, "New York",
                   "Computer Science")
student1.display()
test = Test()
make_sound(Bird())
make_sound(Human())
