# a = 10
# print(a)
#
# z = x = c = 8
#
# print(z, x, c)
#
# print(type(a))
#
# st = 'asadaasasaa'
#
# print(len(st))
#
# a, b = 6, 3
#
# print(a**b)
#
# li = [2, 2, 4, 6, 7]
#
# b = li*2
#
# print(b*10)
#
# def hhhh():
#     name = 777
#
#
# print(hhh())

# 08-04-2026
# Котрежи

# li = (1, 2, 3, 4, 5)
#
# a = 1
#
# aa = 1.
#
# tp1 = 1,
#
# tp = (1,2,3,5,4,6,9,7)
#
# print(tp1, tp)
#
# myList = 0.1, 4, 9.
#
# print(myList)
#
# for i in tp:
#     print(i)
#
# def useful(n):
#     tt = ()
#     for i in range(4):
#         tt = tt + (i,)
#     return tt
# a,b,c,d = useful(4)
# a, b, *c = useful(4)
# _,b,c,_ = useful(4)
# print(useful(4))
# print(a, b, c, d)
#
#
# print(tp.count(5))
# print(tp.index(2))

# Словари. Имеют кличи и значения. Ключи уникальные

# di = {}
#
# print(di)
#
# di = {
#     "name": "a",
#     "age": 155,
#     "phone":"112334545",
#
#     }
#
# print(di)
#
# print(di["name"])
#
# print(di.get("name"))
#
# print(di.get("dsdsdsdsd", -1))
#
# print(di.values())
#
# print(di.keys())
#
# print(di.items())
#
# for k, v in di.items():
#     print(k, v)
#
# di.update({"ageeee":19})
#
# print(di)
#
# di.pop("ageeee")
#
# print(di)
#
# di = {i**2 for i in range(5)}
#
# print(di)

# lab 6 TO DO LIST

# {
#     "id": 1,
#     "todo": "Do something nice for someone you care about",
#     "completed": false,
#     "userId": 152
# },
# {
#     "id": 2,
#     "todo": "Memorize a poem",
#     "completed": true,
#     "userId": 13
# },
# {
#     "id": 3,
#     "todo": "Watch a classic movie",
#     "completed": true,
#     "userId": 68
# }

# CRUD
# менюшка
# общая функция

# task = {
#     "id": 2,
#     "todo": "Memorize a poem",
#     "completed": True,
#     "userId": 13,
#     "priority": 5,
#
# }
#
# print(task)
#
# todos = {
#     1:{
#     "todo": "Do something nice for someone you care about",
#     "completed": False,
#     "userId": 152,
#     'priority': 5
#         },
#     2: {
#     "todo": "Memorize a poem",
#     "completed": True,
#     "userId": 13,
#     'priority': 5
#         },
#     3: {
#     "todo": "Watch a classic movie",
#     "completed": True,
#     "userId": 68,
#     'priority': 5
#         },
# }
#
# def create_task(max_id):
#     auto_id = max_id + 1
#
#     todo = input("todo:")
#     completed = bool(input("completed:"))
#     userId = int(input("userId:"))
#     priority = int(input("priority:"))
#
#     new_task = {auto_id:{
#         "todo": todo,
#         "completed": completed,
#         "userId": userId,
#         "priority": priority,
#             }
#         }
#
#     return new_task
#
#
# # CRUD
# # хранить задачи - ок
# # добавить задачу - ок create
# # печатать задачи - ок read
# # Обновляем +- update
# # удалить - ок delete
#
# # менюшка
# # общая функция с циклом внутри и тп
#
#
# def create_task(max_id):
# auto_id = max_id + 1
#
# todo = input("todo:")
# completed = bool(input("completed (1 Для True, пустой ввод для False):"))
# userId = int(input("userId:"))
# priority = int(input("priority:"))
#
# new_task = {auto_id:{
# "todo": todo,
# "completed": completed,
# "userId": userId,
# "priority": priority,
# }
# }
#
# return new_task
#
#
# def read_tasks():
# for tk, tdi in todos.items():
#
# print("Task id:", tk)
#
# for k, v in tdi.items():
# print(" ", k, ":", v)
# print("__________________________________")
#
#
# def read_task(tid):
# res_task = todos.get(tid, -1)
#
# if res_task == -1:
# print("задача не найдена с id:", tid)
# return
#
# print("Task id:", tid)
#
# for k, v in res_task.items():
# print(" ", k, ":", v)
#
# print("__________________________________")
#
#
# def delete_task(tid):
# res_task = todos.get(tid, -1)
#
# if res_task == -1:
# print("задача не найдена с id:", tid)
# return
#
# print("Task id:", tid)
# todos.pop(tid)
#
# print("задача с id:", tid, "удалена.")
# print("__________________________________")
#
#
# todos = {
# 1:{
# "todo": "Do something nice for someone you care about",
# "completed": False,
# "userId": 152,
# 'priority': 5
# },
# 2: {
# "todo": "Memorize a poem",
# "completed": True,
# "userId": 13,
# 'priority': 5
# },
# 3: {
# "todo": "Watch a classic movie",
# "completed": True,
# "userId": 68,
# 'priority': 5
# },
# }
#
#
# def main():
# print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")
# operation = int(input("-->"))
#
# while operation != 5:
# if operation == 1:
# task = create_task(max(todos.keys()))
# todos.update(task)
# elif operation == 2:
# tid = int(input("Введи таск id:"))
# read_task(tid)
# elif operation == 3:
# read_tasks()
# elif operation == 4:
# tid = int(input("Введи таск id:"))
# delete_task(tid)
# else:
# print("я не понял попробуй ещё раз.")
#
# print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")
# operation = int(input("-->"))
#
# print("пока пока")
#
#
# main()



