from todolist_pkg import useful_funcs as u
from todolist_pkg import stats as s
from todolist_pkg import backup as bb

##import useful_funcs as u
##import statka as s
##import backup as bb
##

todos = {
    1: {
        "todo": "Do something nice for someone you care about",
        "completed": False,
        "userId": 152,
        'priority': 5
    },
    2: {
        "todo": "Memorize a poem",
        "completed": True,
        "userId": 13,
        'priority': 5
    },
    3: {
        "todo": "Watch a classic movie",
        "completed": True,
        "userId": 68,
        'priority': 5
    },
}


def main():
    print("""1 - create, 2 read task by id,
            3 reat all tasks, 4 delete task by id,
            5 статка, 6 бэкап
            0 exit""")
    operation = int(input("-->"))

    while operation != 0:
        if operation == 1:
            task = u.create_task(max(todos.keys()))
            todos.update(task)
        elif operation == 2:
            tid = int(input("Введи таск id:"))
            u.read_task(tid, todos)
        elif operation == 3:
            u.read_tasks(todos)
        elif operation == 4:
            tid = int(input("Введи таск id:"))
            u.delete_task(tid, todos)
        elif operation == 5:
            s.statisics()
        elif operation == 6:
            bb.backup()
        else:
            print("я не понял попробуй ещё раз.")

        print("""1 - create, 2 read task by id,
            3 reat all tasks, 4 delete task by id,
            5 статка, 6 бэкап
            0 exit""")
        operation = int(input("-->"))

    print("пока пока")


main()
