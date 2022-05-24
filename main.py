import cls
import generator
import goods
import user
from category import Category
from goods import Goods


# print('Добро пожаловать в интернет-магазин продуктов питания!')
# print('Просим Вас авторизоваться')
# login = input('Введите Ваш Логин: ')
# password = input('Введите Ваш Пароль: ')
#
# user.user_authorization(login, password)
#
# anykey = input('Нажмите любую клавишу для продолжения')
#
# while anykey is None:
#     print()
#
# cls.clear()

#generator.gen_goods_category()

# Список товаров [id, name, price, category]
goods_list = [[1, 'milk', 100.00, 1], [2, 'solt', 10.05, 4], [3, 'sugar', 15.35, 4], [4, 'kofee', 11.75, 3],[5, 'tea', 5.15, 2]]

# Cписок категорий товаров в формате: [id, name, [goods]]
category_list = [[1, 'Milk', []], [2, 'Tea', []], [3, 'Kofee',[]],[4, 'Other', []]]

vars_good = []  # создаем переменную для товаров

vars_category = []  # создаем переменную для категории товаров

for i in range(len(goods_list)):  # генерируем товары
        vars_good.append(f'goods{i}')
        vars_good[i] = Goods(goods_list[i][0], goods_list[i][1], goods_list[i][2], goods_list[i][3])

for i in range(len(category_list)):  # генерируем категории товаров
        vars_category.append(f'category{i}')
        vars_category[i] = Category(category_list[i][0], category_list[i][1])

for i in range(len(goods_list)):  # связываем товары и категории товаров
    for n in range(len(category_list)):
        if vars_good[i].category == vars_category[n].id:
            vars_category[n].goods.append(vars_good[i].id)

# Вывести список категорий
print(80*'-')
for i in range(Category.counter):
    print(vars_category[i])
print(80*'-')

select_category = int(input('Выбирите категорию товара :'))


print(f'Вы выбрали категорию : {vars_category[select_category-1]}')


# Создадим список товаров для i - категории


select_goods = []
count = 0

# for i in range(Goods.counter):
#     if vars_good[i].category == select_category:
#         count += 1
#         select_goods.append(f'goods{count}')
#         print(count,goods)
#         select_goods[count] = goods.Select_goods(1,'sdc',1)

select_goods = goods.Select_goods(1,'sdc',1)
print(select_goods)

