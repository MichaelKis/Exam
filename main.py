import goods
import user
from category import Category
from goods import Goods
from goods import Select_goods
from basket import Basket
import random


print('Добро пожаловать в интернет-магазин продуктов питания!')
print('Просим Вас авторизоваться')
login = input('Введите Ваш Логин: ')
password = input('Введите Ваш Пароль: ')

user.user_authorization(login, password)

anykey = input('Нажмите любую клавишу для продолжения')

while anykey is None:
     print()

# Список товаров [id, name, price, category]

goods_list = [[1, 'Филе куриное', 100.00, 1],[2, 'Окорок свиной', 100.00, 1],[3, 'Колбаса вареная', 100.00, 1],[4, 'Колбаса сырокопченая', 100.00, 1],[5, 'Шашлык из свиной лопатки', 100.00, 1],[6, 'Картофель фри', 100.00, 2],[7, 'Смесь овощная', 100.00, 2],[8, 'Укроп', 100.00, 2],[9, 'Томаты желтые', 100.00, 2],[10, 'Яблоки Ред Делишес', 100.00, 2],[11, 'Лосось Атлантический', 100.00, 3],[12, 'Форель потрошеная', 100.00, 3],[13, 'Камбала потрошеная', 100.00, 3],[14, 'Хлеб АРНАУТ', 100.00, 4],[15, 'Хлебцы FAZER', 100.00, 4],[16, 'Батон ЛЕНТА', 100.00, 4],[17, 'Кекс ХЛЕБНЫЙ ДОМ', 100.00, 4],[18, 'Кофе растворимый', 100.00, 5],[19, 'Чай черный', 100.00, 5],[20, 'Какао-напиток', 100.00, 5],[21, 'Молоко пастеризованное', 100.00, 6],[22, 'Сырок творожный', 100.00, 6],[23, 'Сыр HEIDI', 100.00, 6],[24, 'Йогурт', 100.00, 6],[25, 'Яйцо куриное', 100.00, 6]]

# Cписок категорий товаров в формате: [id, name, [goods]]

category_list = [[1, 'Мясо,птица,колбаса', []], [2, 'Овощи', []], [3, 'Рыба и морепродукты', []] , [4, 'Хлеб и хлебобулочные изделия', []], [5, 'Чай, кофе', []] , [6, 'Молоко, сыр, яйцо ', []]]

# создаем переменную для товаров

vars_good = []

# создаем переменную для категории товаров

vars_category = []

# Генератор товаров

for i in range(len(goods_list)):
        vars_good.append(f'goods{i}')
        vars_good[i] = Goods(goods_list[i][0], goods_list[i][1], round(random.uniform(100.00,1000.00),2), goods_list[i][3])

# Генератор категории товаров

for i in range(len(category_list)):
        vars_category.append(f'category{i}')
        vars_category[i] = Category(category_list[i][0], category_list[i][1])

# Связываем товары и категории товаров

for i in range(len(goods_list)):
    for n in range(len(category_list)):
        if vars_good[i].category == vars_category[n].id:
            vars_category[n].goods.append(vars_good[i].id)

# Вывести список категорий

print('Список категорий')
print(80*'-')
for i in range(Category.counter):
    print(vars_category[i])
print(80*'-')

# Запрос категории

select_category = int(input('Выбирите категорию товара :'))

if select_category>Category.counter:
    raise Exception ('Не верно указана категория товаров')

print(f'\nВы выбрали категорию товаров: {vars_category[select_category-1]}\n')

# Создадим список товаров для i - категории

select_goods = []
count = 0

for i in range(Goods.counter):
    if vars_good[i].category == select_category:
        select_goods.append(f'select_goods{count}')
        select_goods[count] = goods.Select_goods(count+1,vars_good[i].name,vars_good[i].price)
        count += 1


# Вывести список товаров для i - категории

print('Список товаров')
print(80*'-')
for i in range(Select_goods.counter):
    print(select_goods[i])
print(80*'-')

# Работа с корзиной

step = 0
count_basket = 0

# ! В корзину можно поместить не более 100 товаров, здесь создаем переменные

basket = []
for i in range(100):
    basket.append(f'basket{i}')

# Добавляем товар в корзину, пока пользователь не нажмет 0. Если неверно указан код товара или кол-во возвращаем Exeption с остановкой

while True:

    id_basket = int(input('\nУкажите код товара для добавления в корзину, или 0 для завершения заказа :'))

    if id_basket > Select_goods.counter:
        raise Exception('Неверно указан код товара')
    else:
        if id_basket != 0:
            count_basket = int(input('\nУкажите количество выбранного товара :'))
            if count_basket == 0:
                raise Exception('Неверно указано количество товара')
            else:
                print(f'\nДобавляем товар: {select_goods[id_basket-1].name} в количестве {count_basket} в корзину')
                basket[step] = Basket(select_goods[id_basket-1],count_basket)
                print('В корзине сейчас :')
                print(80 * '-')
                for x in range (Basket.counter):
                    print(basket[x])
                print(80 * '-')
                step += 1
        else:
            break

# Считаем кол-во товаров и итоговую сумму

sum = round(sum(basket[x].amount for x in range(Basket.counter)),2)
print('\n')
print(80*'*')
print(f'Итоговая сумма заказа {sum} , товаров в корзине : {Basket.counter} ')
print(80*'*')

# Оплата или выход

while True:
    pay = input('Оплатить "Y" или выйти "N" :')
    if str.upper(pay) == 'Y':
        print('Спасибо за покупку!')
        break
    elif str.upper(pay) == 'N':
        print('Можно оплатить позднее')
        break
    else:
        print('Уточните ?')







