import random

class Survivor:
    names = ["Roland", "Cullen", "Brian", "Austin", "Haiden", "Alvin", "Bryce", "Turner", "Yusuf", "Cruz", "Sergio",
              "Jane", "Tanya", "Giselle", "Mary", "Yasmin", "Sophia", "Ava", "Ashlynn", "Payten", "Elizabeth", "Shyla"]                                  #kILL YOURSELF

    def __init__(self,):
        self.attack = random.randint(1, 4)
        self.strength = random.randint(1, 4)
        self.charm = random.randint(1, 4)
        self.smarts = random.randint(1, 4)
        self.luck = 20 * random.randint(1, 4)
        self.food = 5
        self.water = 5
        self.inventory = []
        self.name = random.choice( Survivor.names )

#    def foodloss(self):
#        if Surivors <= 0:
#            sys.exit(0)
#        if Surivors<= 10:
#            self.Food = self.Food -1
#        if Surivors > 10 and Surivors < 15:
#            self.Food = self.Food - 2
#        elif Surivors >= 15:
#            self.Food = self.Food - 3

    def additem(self,item):
        self.inventory.append(item)

    def removeitem(self,item):
        self.inventory.remove(item)

    def displayProfile(self):
        print("|+++" + self.name + "+++|")
        print("|+++" + str(self.attack) + "Attack+++|")
        print("|+++" + str(self.strength) + "Strength+++|")
        print("|+++" + str(self.charm) + "Charm+++|")
        print("|+++" + str(self.smarts) + "Smarts+++|")
        print("|+++" + str(self.luck) + "Luck+++|")

        print("|+++" + str(self.food) + "Food+++|")
        print("|+++" + str(self.water) + "Water+++|")
        for i in self.inventory:
            print (i)