from random import random

class ForceWielder:
    def __init__(self, name):
         self.power = random.randint(1, 16),
         self.wisdow = random.randint(1, 16)

    def train(self):
        pass

    def fight_method(self, ForceWielder1, ForceWielder2):
        pass
    def jedi(self):
        pass

class ChildJedi:
    def light_saber(self, color, wisdom):
        lightsaber = ''
        if self.wisdow > self.power:
            self.lightsaber = 'green'

        if self.power > self.wisdow:
            self.lightsaber = 'blue'

        else:
            self.power == self.wisdow
            self.lightsaber = 'Violet'
            print(self.lightsaber)

    def train(self):
        self.wisdom += random.randint(10,21)
        self.power += random.randint(5,15)

    def isJedi(self):
        return True

class ChildSith:
    def rename(self):
        self.name = 'Darth' +self.name

    def lightsaber(self, color):
        self.color = "red"
        self.power += 10

    def train(self):
        self.wisdom += random.randint(5,15)
        self.power += random.randint(10,20)

    def isJedi(self):
        return False









# Write a class called ForceWielder which has the following attributes:
# # - name (string) accept it as an argument from the user
# # - power (an integer) randomly generated between 1 and 15
# # # - wisdom (an integer) randomly generated between 1 and 15
# and the following method:
# ​
# - train (implement it as an abstract method)
# - fight method, two ForceWielder can fight, the winner is the one with the highest harmonic mean between power and wisdom (check out the definition of harmonic mean !)
# - is_jedi method (also abstract method)
# 2) Write a two child class (they inherit from ForceWielder) Jedi and Sith:

# - Jedi has new features:
# - Lightsaber color attribute: if wisdom is higer than power then it is green, if power is higher than wisdom then blue, if they are equal then violet
# - wisdom goes up 10 points
# - the train method when called adds randomly between 10 and 20 points to wisdom and between 5 and 15 points of power
