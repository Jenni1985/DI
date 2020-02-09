# ) Create a class Dog
#
# 2) In this class, create a method __init__, that takes two parameter : nameDog
# and heightDog. This function initialises two attributes with the values of the parameters.
# 3. Create a method talk that print wouaf
#4. Create a method jump that multiplies by two the height of the dog. Print the height of the dog when he jumps.
#5. Create an object Davids_dog. His dog’s name is “Rex” and his height is 50cm.
#
# class Dog:
#     def init_(self, name, height):
#         self.name = name
#         self.height = height
#         self.winner = False
#
#     def talk_(self):
#          print('Wouaf')
#
#     def jump(self):
#     self.height *=2
#     print(self.height)
#
#     def.fight(self, another dog):
#         if self.height > another_dog.height:
#             return self
#         else:
#             return another_dog
#
# Davids_dog = Dog('Rex', 50)
# Sarahs_dog = Dog('Teacup', 20)
# print(Davids_dog)
#
# if Davids_dog.height> Sarah_dog.height:
#     Davids_dog.winner= True
# else:
#     Sarahs_dog.winner = True
#
# def fight(dog1, dog 2)
#     (dog1.height > dog2.height)

#2. Create a class Zoo
# ) In this class create a method __init__, that takes one parameter zooName
# It initialiazes two attributes: animals that is an empty list, name that is the name of the zoo.
#3. Create a method addAnimal that takes one parameter newAnimal. Only if the new animal doesn’t exist in the zoo, add it to the list.
#4.  Create a method getAnimals that prints all the animals in the zoo.
#5. Create a method sellAnimal says goodbye to the animal and removes it from the list.
#6) Create a method sortAnimal that sorts the animals. Each animal, depending on its first letter should be placed inside a pen. { 1: "Ape", 2: ["Baboon", Bear"]}


class Zoo:
    def init (self, zooname):
        self.zooname = zooname
        self.animals = [('Giraffe', 'Monkey', 'cocodrile')]


    def add_new_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(self.animals)

    def sell_animal(self, new_animal):
        self.animals.remove(new_animal)
        print(self.animals)

    def sort_animal(self, animals):
        sorted_animals = self.animals.sort()
        print(sorted_animals)
        temp = 0
        pen = {}
        for x,y in zip(animals[::], animals[1::]):
         if x [0] == y[0]:
        else:
                temp += 1
                pen[temp] = (x)
                pen[temp] = (y)
        print(pen)



















    