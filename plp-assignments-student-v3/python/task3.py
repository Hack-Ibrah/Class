# Task 3: Functions & OOP Basics
# Shows a function, a simple class, and usage examples

def add(a, b):
    """Return sum of a and b"""
    return a + b

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        return f"My name is {self.name} and I study {self.course}."

if __name__ == "__main__":
    print(add(5, 7))
    s = Student("Hack-Ibrah", "Software Development")
    print(s.introduce())
