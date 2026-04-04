# # Home work 3.1
#
# hat_list = [1, 2, 3, 4, 5]
#
# # Step 0: length of list
# a = len(hat_list)
#
# print(a)
#
# # Step 1: replace the middle number entered by the user.
# hat_list[2] = int(input
#                ('Введите целое число для замены среднего элемента списка: '))
#
#
# # Step 2: remove the iast element from the list.
# hat_list.pop()
#
# # Step 3: length of the existing list
# print(len(hat_list))
#
# print(hat_list)


# # Home work 3.4 (lab)
# # Make a new list with unique numbers only.
#
# # original list
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# res_list = []
#
# for elem in my_list:
#     if elem not in res_list:
#         res_list.append(elem)
#
# print(res_list)


# # Home work 3.5
#
# li = input('Введите целые числа через пробел: ').split()
#
# li_int = [int(i) for i in li]
#
# print(f'Сумма введенных чисел: {sum(li_int)}')
