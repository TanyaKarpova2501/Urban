def send_email( message, recepient, sender = "university.help@gmail.com"):
    print(message, recepient, sender)

send_email('Невозможно отравить письмо на ', recepient= 'pochtasony@gmail c',
           sender = "university.help@gmail.com")
send_email('Нельзя отправить сообщение самому себе ', recepient="university.help@gmail.com",
           sender="university.help@gmail.com")
send_email('Не стандартный отправитель. Письмо отправлено с ', sender="university.help@gmail.com",
           recepient = 'на poctasony2906@gmail.uk')
send_email('Письмо успешно отправлено ', 'pochtasony2906@gmail.com, от',)