# # 17-04-2026
# # Наследование
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
#
#     def __repr__(self):
#         return f'| name: {self.name} | age: {self.age}'
#
# class Terrier(Dog):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def __repr__(self):
#         return super().__repr__() + f' | color: {self.color} |'
#
# kelly = Terrier('kelly', 15, 'red')
#
# print(kelly)


# # Полиморфизм
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
#
#     def __repr__(self):
#         return f'| name: {self.name} | age: {self.age}'
#
#     def __add__(self, another_dog):
#         return self.age + another_dog.age
#
# d1 = Dog('Dan', 20)
# d2 = Dog('HHH', 18)
#
# print(d1 + d2)

# stack

class Stack:

    def __init__(self):
        self.__storage = []

    def push(self, value):
        self.__storage.append(value)
        print("Добавляю:", value)

    def pop(self):
        try:
            res = self.__storage.pop()
            print('удалил', res)
        except IndexError:
            print('Склад пуст')
        except:
            print('Ошибочка')

sklad1 = Stack()
sklad1.push(1456)
print(sklad1)
sklad1.pop()
print(sklad1)


