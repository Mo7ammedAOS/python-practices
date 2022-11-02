class PlayerCharcter:
    def __init__ (self, name, age):                   # in Genearal class allow us to write code for once
        self.name = name  #this is attributes                       # and make it daynamic in pramiters
        self.age = age    #'they are somthing dyamic and Changable   

    def run (self):
        print('run')
        return 'Thats perfect'
    def out (self):
        print(f'my name is {self.name}')

player1 = PlayerCharcter('Amro',12)  #this is instantiate
player2 = PlayerCharcter('Asim',12)
print(player1.out())
