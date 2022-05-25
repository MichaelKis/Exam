
class Goods:
    counter = 0
    def __init__(self, id: int, name: str, price: int, category: int):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        Goods.counter +=1


    def __str__(self):
        return f'Код товара: {self.id},\t Название товара: {self.name}, \t Цена товара: {self.price}'


class Select_goods:
        counter = 0
        def __init__(self,id:int, name: str, price: int):
            self.id = id
            self.name = name
            self.price = price
            Select_goods.counter += 1

        def __str__(self):
            return f'Код товара: {self.id},\t Название товара: {self.name}, \t Цена товара: {self.price}'



#if __name__ == '__main__':

