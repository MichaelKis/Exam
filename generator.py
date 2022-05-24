from goods import Goods
from category import Category

def gen_goods_category():

    # Список товаров [id, name, price, category]
    goods_list = [[1, 'milk', 100.00, 1], [2, 'solt', 10.05, 4], [3, 'sugar', 15.35, 4], [4, 'kofee', 11.75, 3],
                      [5, 'tea', 5.15, 2]]

    # Cписок категорий товаров в формате: [id, name, [goods]]
    category_list = [[1, 'Milk', []], [2, 'Tea', []], [3, 'Kofee', []],
                         [4, 'Other', []]]

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


    # проверяем создание товаров
    print(20*'-' + 'товары' + 80*'-')

    for n in range(len(goods_list)):
        print(vars_good[n].id, vars_good[n].name, vars_good[n].price,vars_good[n].category)

    print(20*'-' + 'категории товаров' + 80*'-')

    # проверяем наполнение категорий товаров
    for n in range(len(category_list)):
        print(vars_category[n].id, vars_category[n].name, vars_category[n].goods)

    print(80*'-')

