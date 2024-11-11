SENDER_DEFAULT = 'university.help@gmail.com'
DOMAINS_VALID = ('.net', '.com', '.ru')


def validate_email(email: str) -> bool:
    if email.__contains__('@') and not email.__contains__(' '):
        if DOMAINS_VALID.__contains__(email[-4:]) or DOMAINS_VALID.__contains__(email[-3:]):
            return True
    return False


def send_email(message: str, recipient: str, *, sender: str = 'university.help@gmail.com'):
    if not validate_email(sender) or not validate_email(recipient):
        print(
            f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        elif sender != SENDER_DEFAULT:
            print(
                f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(
                f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


# Для проверки задания:
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
