def send_email( message, recepient, sender = "university.help@gmail.com"):
    print(message, recepient, sender)

    def send_email(email):
        verify = send_email(email)
        if verify == recepient:
            print(f'{email} is a valid email address')
        recepient = (r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')



my_email = input('Введите адрес почты: ')

send_email('Невозможно отравить письмо на ', recepient= 'pochtasony@gmail c',
           sender = "university.help@gmail.com")
send_email('Нельзя отправить сообщение самому себе ', recepient="university.help@gmail.com",
           sender="university.help@gmail.com")
send_email('Не стандартный отправитель. Письмо отправлено с ', sender="university.help@gmail.com",
           recepient = 'на poctasony2906@gmail.uk')
send_email('Письмо успешно отправлено ', 'pochtasony2906@gmail.com, от',)