class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says '
    def reply(self):
        return self.speak()

class Mammal(Animal):
    def speak(self):
        return f'{self.name} says hello'
class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"
class Dog(Mammal):
    def speak(self):
        return f'{self.name} says Woooooo!'
class Primate(Mammal):
    def speak(self):
        return f'{self.name} says hi!'
class ComputerScientist(Primate):
    pass
