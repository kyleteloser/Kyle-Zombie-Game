import random
class Building:
    buildingNames = ["Walmart", "Gas station", "Graveyard", "Field", "Hotel", "Police station"]

    def __init__(self, ):
        self.zombie = random.randint(1, 15)
        self.people = random.randint(1, 3)
        self.food = random.randint(1, 10)
        self.water = random.randint(1, 10)
        self.stuff = random.randint(1, 2)
        self.inventory = ["Rusty shotgun", "Shotgun", "Knife", "Butcher Knife", "Pocket Knife", "Science Weekly",
                          "First Aid Kit", "Hammer", "Bow tie", "Travel backpack"]

    def displayBuilding(self):
        building = random.choice( Building.buildingNames)
        print("|+++" + building + "+++|")
        print("|+++" + str(self.zombie) + "Zombies+++|")
        print("|+++" + str(self.people) + "People+++|")
        print("|+++" + str(self.food) + "Food+++|")
        print("|+++" + str(self.water) + "Water+++|")
        print("|+++" + str(self.stuff) + "Stuff++|")

# This a progress bar utility



