from django.core.mail import send_mail


def send_hello(email):
    send_mail(
        'Вас приветствует крутой сайт', # title
        'привет как дела?', # body
        'vladislav001015@gmail.com', # from
        [email] # to
    )


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        full_link,
        'vladislav001015@gmail.com',
        [email]
    )


def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'vladislav001015@gmail.com',
        [email]
    )