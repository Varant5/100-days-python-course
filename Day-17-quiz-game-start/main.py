class User:
    def __init__(self, name):
        self.name = name
        self.legs = 2

    def cut_leg(self):
        self.legs -= 1

user_1 = User("lukas")
print(user_1.name)

print(user_1.legs)
user_1.cut_leg()
print(user_1.legs)

