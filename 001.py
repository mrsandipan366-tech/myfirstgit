class chocolate:
    count=0
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
        chocolate.count+=1
    def name(self):
        return self.name


    @staticmethod
    def calories():
        return "high"

    def date(self):
        return "summer"


class dark_chocolate(chocolate):
    def __init__(self,name,price,dark_persent):
        super().__init__(name,price)
        self.dark_persent=dark_persent
    
    def date(self):
     return "winter"

# sandi=chocolate("kitkat", 10)
# print(sandi.name)
# print(sandi.price)

# rahul=chocolate("dairy milk", 50)
# print(rahul.name)
# print(rahul.price)


rishav=dark_chocolate("ddk", 100, 20)
print(rishav.name)
print(rishav.price)
print(rishav.dark_persent)

game=chocolate("smooth",30)
print(game.name)
# print(game.name())

# game1=chocolate("smooth",30)
# print(game1.calories())

# g3=chocolate("smooth",30)
# print(g3.date())

# g4=dark_chocolate("smooth",30,70)
# print(g4.date())

print(chocolate.count)
