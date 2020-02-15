# class Writer:
#
#     def __init__(self, name, n_books, genre):
#         self.name = name
#         self.n_books = n_books
#         self.genre = genre
#
#     def write(self):
#         self.n_books +=1
#         print(f'{self.name}wrote a book')
#
#
#
#     if __name__ == '_main__':
#         albert = Writter(name= 'Albert Camus', n_books = 25, genre = ['Philosopy', 'Roman'])
#         print(albert.name)
#         print(albert.n_books)

# class Circle:
#     def __init__(self):
#         return math.pi * self.radius **2
#
#     #@staticmethod se entiende que r es mi atributo sin necesidad de ocupar funcion
#     def compute_area(r):
#         return math.pi * r ** 2
#
# if __name__= "__main__"
#     c = Circle(radius = 2)
#     print(c.area())
#     print(c.compute_area(r=5))

#Decorators
import time
def decorator(func):
    def wrapper():
        print(f'running{func}')
        func()
        print('done')

    return wrapper

@decorator
def talk():
    print('some talk')

def timeit(func):
    def wrapper():
        start = time.perf_counter()
        end = time.perf_counter() - start
        print(f'function took:{end}')
        return wrapper

def compute():
    return 2**5

if __name__= "__main__":
    compute()
