# Home work Lab 5.0

# Эта функция складывает 2 числа.
def plus(num_1, num_2):
    print(f'Plus: {num_1} + {num_2} = {num_1 + num_2}')

# Эта функция вычитает 2 числа.
def mines(num_1, num_2):
    print(f'Mines: {num_1} - {num_2} = {num_1 - num_2}')

# Эта функция умножает 2 числа.
def multiplication(num_1, num_2):
    print(f'Multiplication: {num_1} * {num_2} = {num_1 * num_2}')

# Эта функция делит 2 числа.
def division(num_1, num_2):
    if num_2 == 0:
        print("Zero division error")
    else:
        print(f'Division: {num_1} / {num_2} = {round(num_1 / num_2, 2)}')


def main():

    print(''' 
    #####################################################
    # Author: A K                                       #
    # Date: Today                                       #
    # Task: input +, -, *, / or 'exit' to end program   #
    #####################################################
    ''')

    operation = input('enter math operation + - / * '
                      'or "exit" to end program: ').strip()

    # В цикле просим ввести два числа и выполнить над ним математические операции.
    while operation != 'exit':
        num_1 = float(input('Input first number: ').strip())
        num_2 = float(input('Input second number: ').strip())
        if operation == '+':
            plus(num_1, num_2)  # Вызов фунции сложения двух чисел.
        elif operation == '-':
            mines(num_1, num_2)  # Вызов фунции вычитания двух чисел.
        elif operation == '*':
            multiplication(num_1, num_2)  # Вызов фунции умножения двух чисел
        elif operation == '/':
            division(num_1, num_2)  # Вызов фунции деления двух чисел
        else:
            print('Error operatio. Operation must be + - * /')

        operation = input('enter math operation + - / * '
                          'or "exit" to end program: ')

main()