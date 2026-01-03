class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if other.age > self.age:
            return f"{other.name} is older than me"
        elif other.age < self.age:
            return f"{other.name} is younger than me"
        else:
            return f"{other.name} is the same age as me"
    
p1 = Person("Ishak", 16)
p2 = Person("Anes", 12)
p3 = Person("Anfel", 7)
print(p3.compare_age(p1))

