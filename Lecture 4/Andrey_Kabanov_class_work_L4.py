# a = 4
#
# b, c, d = 3, 6, 9
#
# st = 'dffdfffdf'
# print(st)
# print(len(st))
#
# li = []
#
# li.append(6666)
#
# print(li)
#
# print(id(li))
#
# li1 = li
#
# li1[0] = 88
#
# print(id(li), id(li1))
#
# li2 = li1.copy()
#
# print(li2, id(li2))
# #
# li = [1, 2, 3, 4, 5, 6, 7]
#
# print(li[1:3])
#
# li2 = ['dddfdf', 'ddfdfdfdfd', 12, 13, 14, 'ggfegrg']
#
# print(li2[0:2])
#
# for i in range(1, 8, 2):
#     print('hi', end=' ')
#
# print()
#
# for i in range(1, 8, 2):
#     print('hi', i, end=' ')

# deep copy

# inner_list = [1,2,3, 456]
#
# outer_list = [4,5,6, inner_list]
#
# import copy
#
# li2 = copy.deepcopy(outer_list)
# print(inner_list)
# print(outer_list)
# print(li2)
#
# import calendar
#
# a = calendar.isleap(2028)
#
# print(a)

# Strings

# имя = '1232'
#
# print(имя)

# s = 'khjkjkjkjj'
# print(s)
# print(len(s))
# print(isinstance(s, str))
#
# for i in s:
#     print(i)
#
# f = ''
#
# print(len(f))
#
# g = 'fdf"f"df'
#
# print(g)
#
# s = 'dddfdffddf'      'dfdfddfdddfdf'
#
# print(s)
#
# print(s*7)

# alf = 'aAbBcCsdsdsfSDFGHJM,WERTYUIKL;'
#
# for char in alf:
#     print(char, ord(char))
#
# for char in range(1,450):
#     print(chr(char), end=' ')
#
# Шифр сдвига

# message = 'это строка, которую надо закодировать и раскодировать обратно'
#
# for i in message:
#     print(i, ord(i), " | ", chr(ord(i)+5), ord(i)+5)
#
# sec_message = ''
#
# key = 5
#
# for i in secured_message:
#     print(chr(ord(i)-key), end="")
#
# print(ord('a'))

# message = "Привет! это послание из прошлого, передай его!"
# key = 5
# print(message)
#
# secured_message = ""
#
# for i in message:
#     secured_message += chr(ord(i)+key)
#
# print(secured_message)
#
# print("Дешивровка....")
# for i in secured_message:
#     print(chr(ord(i)-key), end="")

# Срезы

# s = 'hello'

# text = 'HELLOO'
#
# new_Hello =  s[:2] + text + s[4:]
#
# print(new_Hello)
#
# # in not in

# s = 'hello'
#
# print(list(s))
# print(s.upper())
#
# name = 'STAS'
#
# print(name.capitalize())
#
# print(name.lower())

# c = 'c'
#
# print(c.isalpha())
#
# print(c.isdigit())


# url = 'hotmail.*'
#
# li = ['ru', 'by', 'com']
#
# url_list = []
#
# for i in li:
#     url_list.append(url.replace('*', i))
#
# print(url_list)

s = '            hjkhkhhj kjjkjjk    kjkjjjjjjjjjjkj          '

print(s.strip())
print(s.lstrip())
print(s.rstrip())

# 01.04.2026