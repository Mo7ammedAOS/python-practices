class User():
    def logging(self):
        print('Your are logged in')
    def attack(self):
        print('Do nothing')
class Wizard(User):
    def __init__(self, name, power):
        self.name = name 
        self.power = power 
    def attack(self):
        User.attack(self)
        print(f'you are attacking with power of {self.power}')
class Archer(User):
    def __init__(self, name , arrows):
        self.name = name 
        self.arrows = arrows 
    def attack(self):
        print(f'you are attacking with number of Arrows {self.arrows}')


wizard_1 = Wizard('Mohamed',30)
archer_1 = Archer('Hasan',300)

def Player_attack(char):
    char.attack()
Player_attack(wizard_1)

# Player_attack(wizard_1)  # This is Polymorphism
# Player_attack(archer_1)

# for non in [wizard_1 , archer_1]:   # This is Polymorphism
#     non.attack()
