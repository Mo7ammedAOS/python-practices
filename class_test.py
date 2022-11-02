class Player_Charcter:
    def __init__ (self, name, age):
        self.name = name 
        self.age = age 
    def shout(self):
        print(f'hello {self.name}')
        return 'done'
    
player_1 = Player_Charcter('Ali', 25)

print(player_1.shout())
