class chocolate:
    def __init__(self,name,price):
        self.__name=name
        self.price=price
    def name(self):
        return self.__name

class dark_chocolate(chocolate):
    def __init__(self,name,price,dark_persent):
        super().__init__(name,price)
        self.dark_persent=dark_persent

# sandi=chocolate("kitkat", 10)
# print(sandi.name)
# print(sandi.price)

# rahul=chocolate("dairy milk", 50)
# print(rahul.name)
# print(rahul.price)


# rishav=dark_chocolate("ddk", 100, 20)
# print(rishav.name)
# print(rishav.price)
# print(rishav.dark_persent)

# game=chocolate("smooth",30)
# print(game.__name)
# print(game.name())