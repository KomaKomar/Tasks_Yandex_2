#Задачка Абстрактный коТ
#Создаем абстрактного кота, от которого наследуется котенок, от которого наследуется мама Кошка. Пока все логично...
class AbstractCat: #Абстрактный кот будет есть и расти: 10 еды к 1 единице роста
    def __init__(self, size=0, food_ost=0):
        self.size = size
        self.food_ost = food_ost

    def eat(self, eda=0):
        self.size = self.size + (eda + self.food_ost) // 10
        self.food_ost = eda % 10
        if self.size > 100: #после 100 единиц, кот не толстеет
            self.size = 100
    def __repr__(self):
        return f'{self.__class__.__name__} ({self.size})'

class Kitten(AbstractCat): #котенок умеет спать и мяукать, больше ничего, т.к. он еще маленький
    def sleep(self):
        return 'Snope'*(self.size//5) #чем больше котенок, тем слаще спит

    def meow(self):
        return 'meow'

class Cat(Kitten): #Кошка умеет тоже самое, что котенок, а еще ловит мышей и выговаривает свое имя
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name

    def get_name(self):
        return self.name

    def catch_mice(self):
        return 'Got it!'

    def meow(self):
        return 'MEOW'

abscat = AbstractCat()
abscat.eat(125)
abscat.eat(125)
abscat.eat(17)
print(abscat)
kit = Kitten(10)
print(kit.sleep())
cat = Cat(83, 'Molly')
print(cat.meow())
print(cat.sleep())
print(cat.get_name())