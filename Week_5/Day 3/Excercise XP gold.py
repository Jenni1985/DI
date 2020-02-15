import random
import statistics

class ForceWielder:

    def __init__(self, name):
        self.name = name
        self.power = random.randint(1, 16)
        self.wisdom = random.randint(1, 16)

    def train(self):
        pass

    def fight(self, other):
        if statistics.harmonic_mean([self.power, self.wisdom]) > statistics.harmonic_mean([other.power, other.wisdom]):
            print(f'{self.name} you won')
        else:
            print(f'{other.name} you won')

class Jedi(ForceWielder):
    def lightsaber_color(self):
        if self.wisdom > self.power:
            self.saber_color ='green'
        elif self.power > self.wisdom :
            self.saber_color = 'blue'
        else:
            self.saber_color = 'violet'
            self.wisdom = self.wisdom + 10
            print(self.lightsaber_color)

    def train(self):
        self.wisdom = random.randint(10, 20)
        self.power = random.randint(5, 15)
        print(self.widom, self.power)

    def is_jedi(self):
        return True

class Sith(ForceWielder):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Darth" + name
        print(self.name)

        self.lightsaber_color = 'red'
        print(self.lightsaber_color)

        self.power = self.power + 10
        print(self.power)

    def train(self):
        self.wisdom = self.wisdom + random.randint(5, 15)
        self.power = self.power + random.randint(10, 120)
        print(self.wisdom, self.power)

    def is_jedi(self):
        return False

p1 = ForceWielder("Jenni")
p2 = ForceWielder("Topogigo")
p1.fight(p2)
jedi = Jedi("Daff")
jedi.train()
print(jedi.is_jedi())

p3 = Sith(" Mitch")
p3.train()
print(p3.is_jedi())







