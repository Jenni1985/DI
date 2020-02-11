class animal :
    def __init__(self, l, c, h, n):
        self.legs = l
        self.color = c
        self.height = h
        self.name = n
        self.sleeping = False

    def sleep(self):
        self.sleeping = True
        return f"{self.name} is sleeping"

    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def bark(self):
            return f'{self.name} barks!!'

class Shark(Animal):
	def sleep(self):
		return 'Sharks do not sleep'

dog = Dog(4, 'red', '50cm', 'sparky')
shark = Shark(0, 'white', '50cm', 'Elvis')

print(dog.sleep())
print(shark.sleep())
