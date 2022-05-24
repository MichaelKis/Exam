class Basket:
    counter = 0
    def __init__(self, goods =None, count=None):

        self.goods = goods
        self.count = count
        Basket.counter +=1


    def amount(self):
        return self.goods.price * self.count

    def __str__(self):
        return f'Название товара: {self.goods.name}, \t Цена товара: {self.goods.price}, \t Количество: {self.count}'