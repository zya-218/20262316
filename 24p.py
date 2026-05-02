class Animal:
    def __init__(self, name):
        self.name= name
    def speak(self):
        return "animal sound"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
class Elephant(Animal):
    def speak(self):
        return f"{self.name} says Phuu!"
my_dog = Dog(name= "buddy")
my_cat = Cat(name="whiskers")
my_elephant = Elephant(name="tom")

print(my_dog.speak())
print(my_cat.speak())
print(my_elephant.speak())