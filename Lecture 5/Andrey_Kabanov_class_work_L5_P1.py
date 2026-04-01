# Functions
# message = "Привет! это послание из прошлого, передай его!"
# key = 1000
# print(message)
#
# secured_message = ""
#
# for i in message:
#     secured_message += chr(ord(i)+key)
#
# print(secured_message)
#
# print("Дешивровка....")
# for i in secured_message:
#     print(chr(ord(i)-key), end="")


def give_me_message(text):
    message = input(text)
    return message

res = give_me_message("Введите текст: ")

print(res)