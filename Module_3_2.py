from main import check


def send_email( message, recepient, sender = "university.help@gmail.com"):
    import re

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def check(email):
        if (re.send_email(regex, email)):
            print("Valid Email")
        else:
            print("Invalid Email")

my_email = input('Введите адрес почты: ')


send_email('Невозможно отравить письмо на ',recepient = my_email, sender="university.help@gmail.com")
send_email('Нельзя отправить сообщение самому себе ', recepient="university.help@gmail.com",
                 sender="university.help@gmail.com")
send_email('Письмо успешно отправлено ', "от ")
