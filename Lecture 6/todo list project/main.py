import useful_funcs as u


todos = {
    1:{
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
    print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")
    operation = int(input("-->"))
    
    while operation != 5:
        if operation == 1:
            task = u.create_task(max(todos.keys()))
            todos.update(task)
        elif operation == 2:
            tid = int(input("Введи таск id:"))
            u.read_task(tid)
        elif operation == 3:
            u.read_tasks()
        elif operation == 4:
            tid = int(input("Введи таск id:"))
            u.delete_task(tid)
        else:
            print("я не понял попробуй ещё раз.")

        print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")
        operation = int(input("-->"))
    
    print("пока пока")


main()