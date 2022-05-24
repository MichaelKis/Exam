"""
Авторизация пользователя
Проверяется логин и пароль
"""
login = 'KiselevMY'
password = '12345678'

def user_authorization(l, p):

    if l != login:
        print('Вы не зарегистрированы в интернет-магазине')
        raise Exception('Вы не зарегистрированы в интернет-магазине')
    elif p != password:
        print('Введен неверный пароль')
        raise Exception('Введен неверный пароль')
    else:
        print(f'Поздравляем {login}, Вы успешно авторизовались  ')

