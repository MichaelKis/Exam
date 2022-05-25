class Basket:
    counter = 0
    def __init__(self, goods =None, count=None):

        self.goods = goods
        self.count = count
        self.amount = goods.price * self.count
        Basket.counter += 1




    def __str__(self):
        return f'Название товара: {self.goods.name}, \t Цена товара: {self.goods.price}, \t Количество: {self.count}, \t Итого: {self.amount}'