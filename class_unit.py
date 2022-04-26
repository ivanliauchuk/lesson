# class Lion:
#     def roar(self):
#        print("Rrrrrrr!!!")
#
# simba = Lion()
# simba.roar()

# class Counter:
#     def start_from(self, x = 0):
#         self.x = x
#     def increment(self):
#         self.x += 1
#     def display(self):
#         print(f"Текущее значение счетчика = {self.x}")
#     def reset(self):
#         self.x = 0
#
# # c1 = Counter()
# # c1.start_from()
# # c1.increment()
# # c1.display()  # печатает "Текущее значение счетчика = 1"
# # c1.increment()
# # c1.display()  # печатает "Текущее значение счетчика = 2"
# # c1.reset()
# # c1.display()

# class Point:
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def get_distance(self, arg):
#         if isinstance(arg, Point):
#             return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
#         else:
#             print(f'Передана не точка')
#
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"
# class Laptop:
#
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{brand} {model}'
#
#
# laptop1 = Laptop('Apple', 'Macbook Air', 974)
# laptop2 = Laptop('Apple', 'Macbook Pro', 1220)
#
# print(laptop1.laptop_name)

# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: - {self.assists}')
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"

# class Zebra:
#
#     def __init__(self):
#         self.a = 0
#
#     def which_stripe(self):
#         if self.a == 0:
#             self.a += 1
#             print('Полоска белая')
#         else:
#             self.a -= 1
#             print('Полоска черная')
#
#
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"

# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         return f'{self.last_name} {self.first_name}'
#
#     def is_adult(self):
#         return True if self.age >= 18 else False
#
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult()) # выводит "True"

class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        if self.values:
             return False
        else:
            return True

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.is_empty() is False:
            return self.values.pop()
        else:
            print("Empty Stack")

    def peek(self):
        if self.is_empty() is False:
            return self.values[-1]
        else:
            print("Empty Stack")
            return None

    def size(self):
        return len(self.values)

s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2