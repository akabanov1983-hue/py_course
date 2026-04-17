# class Stack:
#
#     def __init__(self):
#         self.__storage = []
#
#     def push(self, value):
#         self.__storage.append(value)
#         print("Добавляю:", value)
#
#     def pop(self):
#         try:
#             res = self.__storage.pop()
#             print('удалил', res)
#         except IndexError:
#             print('Склад пуст')
#         except:
#             print('Ошибочка')