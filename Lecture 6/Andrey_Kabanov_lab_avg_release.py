students_grades = {}

def avg(score):
    """Функция вычисления среднего балла студента.
     :argument score - tuple - набор оценок
     :returns flat - средний балл, 2 знака после запятой
    """
    return round((sum(score)) / len(score), 2)


def new_grade(student_name, grade):
    """Функция для добавления новой оценки студенту
    :argument student_name - str - имя студента, не менее 2-х символов
    :argument grade - int - оценка
    :returns
    True - если оценка добавлена успешно
    False - если имя меньше 2-х символов.
    """

    if len(student_name) < 2:
        return False

    student_name = student_name.title()


    if student_name in students_grades:
        students_grades.update(
            {student_name: students_grades.get(student_name) + (grade,)})

    else:
        students_grades.update({student_name: (grade,)})

    return True

def show_grades():
    print('Show grades')
    for key, value in students_grades.items():
        print('name', key)
        print('grade', value)


def show_avg():
    print('Show avg')
    for key, value in students_grades.items():
        print('name', key)
        print('avg', avg(value))

def main():
   msg = """"
    Эта программа для вычисления средней оценки студентов
    Введите номер операции:
    1 - ввести новую оценку
    2 - показать среднюю оценку
    3 - показать оценки
    quit - выйти из программы
    """
   operation = input(msg)
   while operation != 'quit':
        match operation:
            case '1':
                name = input("Введите имея студента: ")
                grade = int(input("Введите оценку: "))
                new_grade(name, grade)
            case '2':
                show_avg()
            case '3':
                show_grades()
            case _:
                print("Вы ввели неизвестную команду")

        operation = input(msg)

main()




