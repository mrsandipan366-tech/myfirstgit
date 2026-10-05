# class chocolate:
#     count=0
    
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         chocolate.count+=1
#     def name(self):
#         return self.name

#     def price(self):
#         return self.price

#     @staticmethod
#     def calories():
#         return "high"

#     def date(self):
#         return "summer"


# class dark_chocolate(chocolate):
#     def __init__(self,name,price,dark_persent):
#         super().__init__(name,price)
#         self.__dark_persent=dark_persent

#     @property
#     def dark_persent(self):
#         return self.dark_persent
    
#     def date(self):
#      return "winter"



# g5=dark_chocolate("smooth",30,70)
# g5.__dark_persent=48000
# print(g5.dark_persent)



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
# print(game.name)
# print(game.name())

# game1=chocolate("smooth",30)
# print(game1.calories())

# g3=chocolate("smooth",30)
# print(g3.date())

# g4=dark_chocolate("smooth",30,70)
# print(g4.date())

# print(chocolate.count)



# class car:
#     print("this is car class")
# class bike:
#     print("this is bike class")
# class vehicle(car,bike):
#     pass

# my=vehicle()

# g6=dark_chocolate("smooth",30,70)
# g7=chocolate("smooth",30)

# print(isinstance(g6,dark_chocolate))
# print(isinstance(g7,dark_chocolate))


