from finance_transactions import create_transaction as c_t
from finance_transactions import update_transaction_by_id as u_t
from finance_transactions import get_transaction_by_id as t_id
from finance_transactions import get_list_of_transactions as l_t
from finance_transactions import delete_transaction_by_id  as d_t

transactions = {
    1: {
        "type": "income",
        "amount": 3000.00,
        "category": "salary",
        "date": "2026-05-01",
        "comment": "Monthly salary"
    },
    2: {
        "type": "expense",
        "amount": 45.50,
        "category": "food",
        "date": "2026-05-01",
        "comment": "Lunch"
    }
}

def main():
    """Функция предназначена для операций с транзакциями: добавить транзакцию, изменить транзакцию
     удалить транзакцию, вывести список транзакций, вывести транзакцию по ее идентификатору"""

    start_message = '''
Выберите действие из списка:
1 - добавить новую транзакцию
2 - вывести на экран список транзакций
3 - вывести на экран транзакцию по идентификатору 
4 - изменить транзакцию по идентификатору
5 - удалить транзакцию по идентификатору
0 - выход из программы
--->>: '''


    while True:

        try:
            operation = int(input(start_message))

        except ValueError:
            print("Ошибка.Введите целое число")
            continue

        match operation:

            case 1:
                c_t(transactions)

            case 2:
                l_t(transactions)

            case 3:
                try:
                    transaction_id = int(input('Введите идентификатор транзакции: ').strip())

                except ValueError:
                    print("Ошибка.Введите целое число")
                    continue

                t_id(transactions,transaction_id)

            case 4:
                try:
                    transaction_id = int(input('Введите идентификатор транзакции: ').strip())

                except ValueError:
                    print("Ошибка.Введите целое число")
                    continue

                u_t(transactions,transaction_id)

            case 5:
                try:
                    transaction_id = int(input('Введите идентификатор транзакции: ').strip())

                except ValueError:
                    print("Ошибка.Введите целое число")
                    continue

                d_t(transactions,transaction_id)


            case 0:
                print('Вы вышли из программы')
                break

            case _:
                print("Неизвестная команда")





        # operation = int(input(start_message))

main()





