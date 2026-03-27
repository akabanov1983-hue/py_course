# # List
#
# numbers = [1, 2, 3, 4, 5]  # Сам список не сортированный и может изменяться
#
# print(numbers)
#
# print(numbers[0]) # обращение к первому элементу
#
# print(numbers[4])
#
# print(numbers[-1]) # индексация с конца списка
#
# print(type(numbers))
#
# numbers.append(1000)  # добавление в конец списка значения
#
# print(numbers)
#
# li = [1, 2, 3, 4, 5]
#
# print(len(li))
#
# li.append(45)
#
# print(li)
#
# li.insert(2, 333)
#
# print(li)
#
# li.reverse()
#
# print(li)
#
# li.remove(4)
#
# print(li)
#
# li = li*2
#
# print(li)
#
# print(li.count(5))

# li = [1, 2, 3, 4, 5]

# 27-03-2026
# print(li)

# li[2] = 77  # замена/перезапись значения

# print(li)

# newli = li.copy()  # копировать список
#
# print(li)
# print(newli)
#
# li2 = li  #  переназначаем список, но получим один и тот же набор значений,
#           # при изменении одного - будет изменяться второй
#
# print(id(li))  # Получить идентификатор объекта
# print(id(li2))  # Идентификаторы совпадают
# li3 = li2.copy()  # Делаем копию через метод копировая
# print(id(li3))  # Получаем новый идентификатор

# li = [888, 2, 0, 9999, 4]
#
# removal = li.pop()  # удаляет последний элемент
# print(removal)
# print(li)
# li.pop(1)
# print(li)
#
# del li[-1]
# print(li)
# li.clear()
# print(li)

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]

# n = int(input('Сколько чисел ввести: '))
#
# user_list = []
#
# for i in range(n):
#     user_list.append(int(input('Введите число:')))
# else:
#     result_s = sum(user_list)
#     print(user_list)
#     user_list.sort()
#     print('Отсортированный список', user_list)
#     user_list.reverse()
#     print('Перевенутый список', user_list)
#     print('Длина списка', len(user_list))
#     print('Сумма элекментов списка', result_s)

#  действия со списками в циклах

#  по значению

# li = [1, 2, 3, 4, 5, 8, 8]
#
# for elem in li:
#     print(elem, end=' ')
# print('\n-------------------------')
#
#
# # по индексу
#
# for index in range(len(li)):
#     print('Номер индекса', index)
#     print('Значение в индексе', li[index])

# enumerate

# li = ['Блокнот', 'Ручка', 'Степлер', 'Карандаш']
#
# for i, value in enumerate(li):
#     print(i, value, end=' ')

#  zip - склеивает несколько списков

# currency = ['BYN', 'RUB', 'USD', 'EUR']
# country = ['Belarus', 'Russia', 'USA', 'Germany']
#
# zip(currency, country)
#
# list(zip(currency, country))
#
# print(list(zip(currency, country)))
#
# for curr, coun in list(zip(currency, country)):
#     print(curr, coun)

# Сортировка

# li = [1, 3, 5, 2]
#
# # 5 - индекс 2
# # 2 - индекс 3
#
# tmp = li[2]
# li[2] = li[3]
# li[3] = tmp
# print(li)
#
# li[2],

# Срезы (slices)

# li = [3, 5, 6, 2, 8, 6, 4]

# Цель - получить новый список [6, 2, 8]

# [startIndex:endIndex]

# [3, 5, 6, 2, 8, 6, 4]
# [6, 2, 8]

# print(li)
# print(li[2:5])
# print(li[:6])
# print(li[2:])

# Поиск значения внутри списка

# li = [3, 5, 6, 2, 8, 6, 4]
#
# print(5 in li)
# print(99 in li)

# li = [3, 5, 6, 2, 8, 6, 4]
# print(sum(li))

# Множества

# моножества хранят тольк уникальные значения
#
# li = [1,2,3,1,2,3,1,2,3]
#
# se = {1,2,3,1,2,3,1,2,3}
#
# print(li)
# print(se)
#
# neSet = set(li)
#
# print(neSet)

# se = {1,2,3}
#
# se.add(2222)
# se.add(3)
#
# print(se)
#
# se.remove(2)  # удаление значения, если его нет - будет ошибка
# print(se)
#
# se.discard(2)  # Безопасное удаление
#
# for i in se:
#     print(i)
#
# print(len(se))

# Lab 3.4

# my_list = [1,2,3,4,5,6,6,6,7,8,8,8]

# однострочники циклы

# st = 'asdfdjkfmdkjhjjljljtttteeeejmc'
# li = []
# for char in st:
#     if char in 'aei':
#         li.append(char.upper())
#     else:
#         li.append(char*3)
# print(li)
#
# st = 'asdfdjkfmdkjhjjljljtttteeeejmc'
#
# li = [li.append(char.upper()) for char in st if char not in 'aei']
# # for char in st:
# #     if char in 'aei':
# #         li.append(char.upper())
# #     else:
# #         li.append(char*3)
# print(li)

# # # 1 4 7 9 10
# sep = ' '
# number = input()
# #
# # number.split(sep)
# #
# # print(number.split(sep))
# #
# li= [int(i) for i in number.split(sep)]
#
# print(li)

# Многомерные списки

li = [[1,2,3], [4,5], [6,7]]

print(li[0][2])  # доступ к элементу многомерного массива