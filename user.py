import time

"""
Авторизация пользователя
Проверяется логин и пароль, неуспешная авторизация фиксируется в файл userlog.txt
"""

login = 'User'
password = '12345678'

def user_authorization(l, p):

    if l != login:
        print('Вы не зарегистрированы в интернет-магазине')
        f = open('userlog.txt', 'w')
        write = str(f'{time.ctime()}: login: {l},  Error: Пользователь не существует')
        f.write(write)
        f.close()
        raise ValueError('Вы не зарегистрированы в интернет-магазине')

    elif p != password:
        print('Введен неверный пароль')
        f = open('userlog.txt', 'w')
        write = str(f'{time.ctime()}: login: {login},  Error: Ошибка ввода пароля')
        f.write(write)
        f.close()
        raise ValueError('Введен неверный пароль')

    else:
        print(f'Поздравляем {login}, Вы успешно авторизовались  ')


class Users:
    def __init__(self,login:str=None,password:str=None):
        self.login = login
        self.password = password

    def add_user(self,l,p):
        f = open('userlog.txt', 'w')
        list = l,p
        f.write(list)
        f.close()



#if __name__ == '__main__':
