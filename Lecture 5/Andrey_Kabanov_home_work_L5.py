# # Home work Lab 5.0
#
# # Эта функция складывает 2 числа.
# def plus(num_1, num_2):
#     print(f'Plus: {num_1} + {num_2} = {num_1 + num_2}')
#
# # Эта функция вычитает 2 числа.
# def mines(num_1, num_2):
#     print(f'Mines: {num_1} - {num_2} = {num_1 - num_2}')
#
# # Эта функция умножает 2 числа.
# def multiplication(num_1, num_2):
#     print(f'Multiplication: {num_1} * {num_2} = {num_1 * num_2}')
#
# # Эта функция делит 2 числа.
# def division(num_1, num_2):
#     if num_2 == 0:
#         print("Zero division error")
#     else:
#         print(f'Division: {num_1} / {num_2} = {round(num_1 / num_2, 2)}')
#
#
# def main():
#
#     print('''
#     #####################################################
#     # Author: A K                                       #
#     # Date: Today                                       #
#     # Task: input +, -, *, / or 'exit' to end program   #
#     #####################################################
#     ''')
#
#     operation = input('enter math operation + - / * '
#                       'or "exit" to end program: ').strip()
#
#     # В цикле просим ввести два числа и выполнить над ним математические операции.
#     while operation != 'exit':
#         num_1 = float(input('Input first number: ').strip())
#         num_2 = float(input('Input second number: ').strip())
#         if operation == '+':
#             plus(num_1, num_2)  # Вызов фунции сложения двух чисел.
#         elif operation == '-':
#             mines(num_1, num_2)  # Вызов фунции вычитания двух чисел.
#         elif operation == '*':
#             multiplication(num_1, num_2)  # Вызов фунции умножения двух чисел
#         elif operation == '/':
#             division(num_1, num_2)  # Вызов фунции деления двух чисел
#         else:
#             print('Error operatio. Operation must be + - * /')
#
#         operation = input('enter math operation + - / * '
#                           'or "exit" to end program: ')
#
# main()


# Home work 5.1

# def is_year_leap(year):
#     """Проверить, является ли год високосным.
#
#     :param year: Год для проверки.
#     :type year: int
#     :return: True, если год високосный, иначе False.
#     :rtype: bool
#     """
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False
#
# # Тестовые данные.
# test_data = [1500, 1900, 2000, 2016, 1987]
#
# test_results = [False, False, True, True, False]
#
# # Проверка результатов работы функции в цикле.
# for year, result in zip(test_data, test_results):  # Объединяет два списка
#     if is_year_leap(year) == result:
#         print(f'{year} is leap --> {result}')
#     else:
#         print(f'{year} from your fanc --> {is_year_leap(year)}')
#         print(f'but expected --> {result}')

# Home work (lab BMI)

def bmi(weight, height):
    """Вычислить индекс массы тела.

    :param weight: Масса тела в килограммах.
    :type weight: float
    :param height: Рост в метрах.
    :type height: float
    :return: Индекс массы тела.
    :rtype: float
    """
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return round((weight / height ** 2), 1)

print(bmi(80, 1.78))

# def main():
#



