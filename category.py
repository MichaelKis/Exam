
class Category:
    counter = 0
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.goods = []
        Category.counter +=1

    def __str__(self):
        return f'Код категории: {self.id},\t Название категории: {self.name}'
