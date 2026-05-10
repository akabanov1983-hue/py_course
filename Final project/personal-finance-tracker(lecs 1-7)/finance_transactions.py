def create_transaction(transactions):
    """Функция создает финансовую транзакцию"""

    print('-----------------------------------------------')

    print('Выбрано: создание новой транзакции')

    print()

    transaction_id = max(transactions.keys(), default=0) + 1

    transaction_type = input("Введите категорию (доход/расход): ").strip().lower()

    while transaction_type not in ('доход', 'расход'):
        print('Ошибка. Требуется ввести "доход" или "расход"')
        transaction_type = input("Введите категорию (доход/расход): ").strip().lower()

    while True:
        amount_text = input("Введите сумму: ").strip()

        try:
            amount = float(amount_text)
        except ValueError:
            print("Ошибка. Сумма должна быть числом.")
            continue

        if amount <= 0:
            print("Ошибка. Сумма должна быть больше 0.")
            continue

        break


    category = input("Введите категорию: ").strip()

    date =  input("Введите дату в формате гггг-мм-дд: ").strip()

    comment = input("Введите комментарий: ").strip()




    transactions[transaction_id] = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "date": date,
        "comment": comment
        }

    print()
    print(f'Транзакция успешно создана:\n'
          f'ID: {transaction_id}\n'
          f'Тип {transactions[transaction_id]["type"]}\n'
          f'Сумма: {transactions[transaction_id]["amount"]}\n'
          f'Категория: {transactions[transaction_id]["category"]}\n'
          f'Дата {transactions[transaction_id]["date"]}\n'
          f'Описание: {transactions[transaction_id]["comment"]}\n')

    print('-----------------------------------------------')


def get_transaction_by_id(transactions, transaction_id):
    """Функция возвращает транзакцию по ее идентификатору"""

    print('-----------------------------------------------')

    print('Выбрано: вывести на экран транзакцию по идентификатору')

    print()

    if transaction_id not in transactions.keys():
        print(f'Транзакции с идентификатором {transaction_id} не существует')

    else:
        print(f'ID: {transaction_id}\n'
              f'Тип {transactions[transaction_id]["type"]}\n'
              f'Сумма: {transactions[transaction_id]["amount"]}\n'
              f'Категория: {transactions[transaction_id]["category"]}\n'
              f'Дата {transactions[transaction_id]["date"]}\n'
              f'Описание: {transactions[transaction_id]["comment"]}\n')

        print('-----------------------------------------------')


def get_list_of_transactions(transactions):
    """Функция возвращает список всех транзакций"""

    print('-----------------------------------------------')

    print('Выбрано: вывести на экран список транзакций')

    print()

    for transaction_id in transactions.keys():
        print(f'transaction id: {transaction_id} |'
              f'type: {transactions[transaction_id]["type"]} |'
              f'amount: {transactions[transaction_id]["amount"]} |'
              f'category: {transactions[transaction_id]["category"]} |'
              f'date: {transactions[transaction_id]["date"]} |'
              f'comment: {transactions[transaction_id]["comment"]} |')

        print('-----------------------------------------------')


def delete_transaction_by_id(transactions, transaction_id):
    """Функция удаляет транзакцию по ее идентификатору"""

    print('-----------------------------------------------')

    print('Выбрано: удалить транзакцию по идентификатору')

    print()

    if transaction_id not in transactions.keys():
        print(f'Транзакции с идентификатором {transaction_id} не существует')
    else:
        del transactions[transaction_id]
        print(f'Транзакция с идентификатором {transaction_id} успешно удалена')

        print('-----------------------------------------------')


def update_transaction_by_id(transactions, transaction_id):
    """Функция частично обновляет транзакцию по ее идентификатору"""

    print('-----------------------------------------------')

    print('Выбрано: изменить транзакцию по идентификатору')

    print()

    if transaction_id not in transactions:
        print(f'Транзакция с идентификатором {transaction_id} не существует')
        return

    else:
        print('Введите новое значение поля или нажмите "Enter" '
              'для пропуска и перехода к следующему полю')

        while True:

            new_type = input(
                f'Прежнее значение "{transactions[transaction_id]["type"]}", '
                f'введите новое: '
            ).strip().lower()

            if new_type == "":
                break

            if new_type in ("доход", "расход"):
                transactions[transaction_id]["type"] = new_type
                break

            print('Ошибка. Требуется ввести "доход" или "расход"')


        while True:

            new_amount_text = input(f'Прежнее значение '
                           f'"{transactions[transaction_id]["amount"]}", введите новое:').strip()

            if new_amount_text == "":
                break

            try:
                new_amount = float(new_amount_text)

            except ValueError:
                print("Ошибка. Сумма должна быть числом.")
                continue

            if new_amount <= 0:
                print("Ошибка. Сумма должна быть больше 0.")
                continue

            transactions[transaction_id]["amount"] = new_amount

            break

        new_category = input(f'Прежнее значение '
                             f'"{transactions[transaction_id]["category"]}", введите новое: ')

        new_date =  input(f'Прежнее значение '
                          f'"{transactions[transaction_id]["date"]}", введите новое: ')

        new_comment = input(f'Прежнее значение '
                            f'"{transactions[transaction_id]["comment"]}", введите новое: ')

        new_type = input(f'Прежнее значение '
                            f'"{transactions[transaction_id]["type"]}", введите новое: ')

        if new_type:
            transactions[transaction_id]["type"] = new_type

        if new_category:
            transactions[transaction_id]["category"] = new_category

        if new_date:
            transactions[transaction_id]["date"] = new_date

        if new_comment:
            transactions[transaction_id]["comment"] = new_comment

        print('-----------------------------------------------')
