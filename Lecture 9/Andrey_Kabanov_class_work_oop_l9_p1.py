# OOP
# 15 04 2026

class Car:
    pass


class Wallet:
    pass

# Укаждого пользователя есть имя, телефон, почта
class User:
    def __init__(self, user_name, user_phone, user_email):
        self.name = user_name
        self.phone = user_phone
        self.email = user_email


stas = User("Stas", "375222222", "stas@m.ru")

print(stas.name)

print(stas.phone)

stas.phone = '99999999'

print(stas.phone)

class Animal:
    pass


mycar = Car()

mywallet = Wallet()

