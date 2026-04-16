# # Home work 3.1
# hat_list = [1, 2, 3, 4, 5]
# print(f'Исходный список: {hat_list}')
#
# # Step 0: length of list.
# len_hat_list = len(hat_list)
#
# print(f'Длина исходного списка: {len_hat_list} ')
#
# # Look for middle element of the list
# middle_index = len_hat_list // 2
#
# print(f'Значение среднего элемента списка: {hat_list[middle_index]}')
#
# # Step 1: replace the middle number entered by the user.
# hat_list[middle_index] = int(input
#                ('Введите целое число для замены среднего элемента списка: '))
#
#
# # Step 2: remove the last element from the list.
# hat_list.pop()
#
# # Step 3: length of the existing list.
# print(f'Длина списка после удаленя последнего элемента: {len(hat_list)}')
#
# print(f'Список после изменений: {hat_list}')

#  Home work 3.3.
# The bubble sort.

# #  Original list.
# li = [3, 5, 2, 0]
#
# swapped = True  # This flag shows changes between list's elements.
#
# print(li)
#
# #  Sort elements in loop.
# while swapped:
#     swapped = False
#     for i in range(len(li) - 1):
#         if li[i] > li[i+1]:
#             li[i], li[i+1] = li[i+1], li[i]
#             swapped = True
#
# #  Print sorted list.
# print(li)

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
#
#
# Home work 3.5
# li = input('Введите целые числа через пробел: ').split()
#
# # Convert str to int type.
# li_int = [int(i) for i in li]
#
# print(f'Сумма введенных чисел: {sum(li_int)}')
