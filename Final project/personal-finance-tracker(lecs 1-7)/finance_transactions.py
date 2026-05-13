def create_transaction(transactions):
    """
    Создает новую финансовую транзакцию.

    Запрашивает у пользователя тип транзакции, сумму, категорию,
    дату и комментарий. Проверяет, что тип транзакции равен
    "доход" или "расход", а сумма является положительным числом.
    После успешного ввода добавляет транзакцию в словарь transactions.

    :param transactions: Словарь с финансовыми транзакциями.
    :type transactions: dict
    :return: None
    """

    print('-----------------------------------------------')

    print('Выбрано: создание новой транзакции')

    print()

    # Создание идентификатора транзации.
    transaction_id = max(transactions.keys(), default=0) + 1

    transaction_type = input("Введите тип (доход/расход): ").strip().lower()

    # Проверка на ввод типа транзакции: доход/расход.
    while transaction_type not in ('доход', 'расход'):
        print('Ошибка. Требуется ввести "доход" или "расход"')
        transaction_type = input("Введите категорию (доход/расход): ").strip().lower()

    # Проверка на ввод суммы: сумма должна быть числом и должна быть больше 0.
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

    # Сохранение введенных данных в словарь.
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
          f'Тип: {transactions[transaction_id]["type"]}\n'
          f'Сумма: {transactions[transaction_id]["amount"]}\n'
          f'Категория: {transactions[transaction_id]["category"]}\n'
          f'Дата: {transactions[transaction_id]["date"]}\n'
          f'Описание: {transactions[transaction_id]["comment"]}\n')

    print('---------------------------------------------')


def get_transaction_by_id(transactions, transaction_id):
    """
    Выводит на экран финансовую транзакцию по ее идентификатору.

    Функция проверяет наличие транзакции с указанным идентификатором
    в словаре transactions. Если транзакция найдена, выводит ее данные:
    идентификатор, тип, сумму, категорию, дату и описание. Если транзакция
    не найдена, выводит сообщение об ошибке.

    :param transactions: Словарь с финансовыми транзакциями.
    :type transactions: dict
    :param transaction_id: Идентификатор транзакции для поиска.
    :type transaction_id: int
    :return: None
    """

    print('-----------------------------------------------')

    print('Выбрано: вывести на экран транзакцию по идентификатору')

    print()

    if transaction_id not in transactions.keys():
        print(f'Транзакции с идентификатором {transaction_id} не существует')

    else:
        print(f'ID: {transaction_id}\n'
              f'Тип: {transactions[transaction_id]["type"]}\n'
              f'Сумма: {transactions[transaction_id]["amount"]}\n'
              f'Категория: {transactions[transaction_id]["category"]}\n'
              f'Дата: {transactions[transaction_id]["date"]}\n'
              f'Описание: {transactions[transaction_id]["comment"]}\n')

        print('-----------------------------------------------')


def get_list_of_transactions(transactions):
    """
    Выводит на экран финансовую транзакцию по ее идентификатору.

    Функция проверяет, существует ли транзакция с указанным
    идентификатором в словаре transactions. Если транзакция найдена,
    выводит ее данные на экран. Если транзакция не найдена,
    выводит сообщение об ошибке.

    :param transactions: Словарь с финансовыми транзакциями.
    :type transactions: dict
    :param transaction_id: Идентификатор транзакции для поиска.
    :type transaction_id: int
    :return: None
    """

    print('-----------------------------------------------')

    print('Выбрано: вывести на экран список транзакций')

    print()

    # Перебор списка транзакций в словаре через цикл и вывод каждой записи.
    for transaction_id in transactions.keys():
        print(f'transaction id: {transaction_id} |'
              f'type: {transactions[transaction_id]["type"]} |'
              f'amount: {transactions[transaction_id]["amount"]} |'
              f'category: {transactions[transaction_id]["category"]} |'
              f'date: {transactions[transaction_id]["date"]} |'
              f'comment: {transactions[transaction_id]["comment"]} |')

        print('-----------------------------------------------')


def delete_transaction_by_id(transactions, transaction_id):
    """
    Удаляет финансовую транзакцию по ее идентификатору.

    Функция проверяет, существует ли транзакция с указанным
    идентификатором в словаре transactions. Если транзакция найдена,
    удаляет ее из словаря. Если транзакция не найдена, выводит
    сообщение об ошибке.

    :param transactions: Словарь с финансовыми транзакциями.
    :type transactions: dict
    :param transaction_id: Идентификатор транзакции для удаления.
    :type transaction_id: int
    :return: None
    """

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
    """
    Частично обновляет финансовую транзакцию по ее идентификатору.

    Функция проверяет наличие транзакции с указанным идентификатором
    в словаре transactions. Если транзакция найдена, пользователь может
    изменить тип, сумму, категорию, дату и комментарий.

    Для каждого поля показывается текущее значение. Если пользователь
    вводит новое значение, оно сохраняется в транзакции. Если пользователь
    нажимает Enter без ввода значения, поле остается без изменений.

    Тип транзакции должен быть равен "доход" или "расход".
    Сумма должна быть положительным числом.

    :param transactions: Словарь с финансовыми транзакциями.
    :type transactions: dict
    :param transaction_id: Идентификатор транзакции для обновления.
    :type transaction_id: int
    :return: None
    """

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
                f'Прежнее значение "Тип" "{transactions[transaction_id]["type"]}", '
                f'введите новое: '
            ).strip().lower()

            if new_type == "":
                break

            if new_type in ("доход", "расход"):
                transactions[transaction_id]["type"] = new_type
                break

            print('Ошибка. Требуется ввести "доход" или "расход"')


        while True:

            new_amount_text = input(f'Прежнее значение "Сумма" '
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

        new_category = input(f'Прежнее значение "Категория"'
                             f'"{transactions[transaction_id]["category"]}", введите новое: ')

        new_date =  input(f'Прежнее значение "Дата"'
                          f'"{transactions[transaction_id]["date"]}", введите новое: ')

        new_comment = input(f'Прежнее значение "Комментарий"'
                            f'"{transactions[transaction_id]["comment"]}", введите новое: ')


        if new_type:
            transactions[transaction_id]["type"] = new_type

        if new_category:
            transactions[transaction_id]["category"] = new_category

        if new_date:
            transactions[transaction_id]["date"] = new_date

        if new_comment:
            transactions[transaction_id]["comment"] = new_comment

        print('-----------------------------------------------')
