import time
import sys
import random
import Survivor
import Building


#   Attack = zombies - each attack increase by 50% - % of zombies


# each survivor has 1 action so they can kill zombies, salavage, recuit, build, and scout.
# 1attack =  20% to kill all the zombies
# 1charm = 20% to gain a new surivor
# 1smarts = 1 less turn to discover science
# 1luck = 20% to find something
# 1strength = 1 turn less to build something

# Types & Classes
# integer (2, 3, 4, 6), strings ("Kyle","Y","Z"), float (3.14), Boolean (True, False)
# This a progress bar utility


def update_progress(progress, kind):
    barLength = 10  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength * progress))
    text = "\r" + kind + ": [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block),
                                                   progress * 100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


def doLoadingBar():
    # Do loading bar
    print("")
    print("progress : 0->1")
    for i in range(5):
        time.sleep(0.1)
        update_progress(i / 10.0, "Percent Loading Game")
    print("")


def pickSurvivor(survivors):
    theChosen = survivors[0]
    print("Which survivor would you like to pick,(Type in their name)")
    n = input("Survivor Name: ")
    for s in survivors:
        print("Debug: s.name" + s.name + "Against input name: " + n)
        if n in s.name:
            theChosen = s
            break
    return theChosen


def doPlay():
    print(
        "The rules are very simple, your job is to build a town by building 18 buildings before the zombies eat you up.")
    print()
    print("You begin with 2 survivors each have different stats, each survivor has each 1 action ")
    print()
    time.sleep(0.1)
    print("There is strength which helps you build more buildings faster or upgrade them.")
    print()
    time.sleep(0.1)
    print("There is attack which helps in killing zombies or people... ")
    print()
    time.sleep(0.1)
    print("There is charm which helps you recruit people ")
    print()
    time.sleep(0.1)
    print("There is Smarts which helps if you wanna do some science shit.")
    print()
    time.sleep(0.1)
    print("There is Luck which helps to find objects,such as water and food.")
    print()
    time.sleep(0.1)
    print("You have a random chance of events happening, such as hordes of zombies, disease or a bumper crop. ")
    print()
    time.sleep(0.1)
    print("Thats all it for the rules Good luck.")
    print()
    time.sleep(0.1)
    basename = input("Before we begin what do you wanna call your Town")
    print("+-+-+-+-+-+-+-+-+-+")
    print("Welcome to " + basename + " ")
    print()
    time.sleep(0.1)
    print("" + basename + " ")

    print("")
    for i in range(Food):
        time.sleep(0.1)
        update_progress(i / 100.0, "Food")

    print("")
    for i in range(Water):
        time.sleep(0.1)
        update_progress(i / 100.0, "Water")

    print("")

    for s in gSurvivors:
        s.displayProfile()
        print()

    print()
    print()
    currentPlace.displayBuilding()
    print()

    availableSurvivors = gSurvivors

    while len(availableSurvivors) > 0:
        F = input("Do you wish to (A)ttack, (S)alavage or (R)ecuit.")
        if 'S' in F or 's' in F:
            s = pickSurvivor(availableSurvivors)
            # Pick up all the food and water
            s.food = s.food + currentPlace.food
            s.water = s.water + currentPlace.water
            currentPlace.food = 0
            currentPlace.water = 0

            # See if they are lucky enough to find some items
            dice = random.randint(1, 100)
            print("DEBUG: Item check: Rolled " + str(dice) + "Against a luck score of " + str(s.luck))
            if dice <= s.luck:
                item = random.choice(currentPlace.inventory)
                s.inventory.append(item)
                currentPlace.inventory.remove(item)

        if 'a' in F or 'A' in F:
            s = pickSurvivor(availableSurvivors)
            currentPlace.zombie = currentPlace.zombie - s.attack + 5
            if currentPlace.zombie > s.attack:
                print()
                print("Still more zombies to go you have " + str(currentPlace.zombie) + "left")

        for s2 in availableSurvivors:
            print("DEBUG: s2.name" + s2.name)
        print("DEBUG: s.namep" + s.name)
        availableSurvivors.remove(s)
        for s2 in availableSurvivors:
            print("DEBUG: s2.name" + s2.name)


def doSurvivorDisplay():
    for s in gSurvivors:
        print()
        s.displayProfile()
        time.sleep(1)


def main():
    quit = False
    while not quit:
        # Display Menu of Choices & Get Choice
        d = input("""
        Welcome To cheesy zombie game made by a Asshole.
        [D]isplay
        [P]lay
        [Q]uit
        """)

        # Render Initial Survivor Status
        if 'D' in d or 'd' in d or 'Display' in d or 'display' in d:
            doSurvivorDisplay()

        elif 'Play' in d or 'play' in d or 'p' in d or 'P' in d:
            doPlay()

        # Check for Quit
        elif 'Kill' in d or 'q' in d or 'Q' in d:
            quit = True

    return quit


###############################
# Begin Main Code

# Do the loading Bar
doLoadingBar()

# Setup World TODO move this to a function
currentPlace = Building.Building()
Food = 10
Water = 10
Housing = 5
InitialSurvivors = 2

gSurvivors = []
for x in range(InitialSurvivors):
    gSurvivors.append(Survivor.Survivor())

# s is a dead survivor
# gSurvivors.remove(s)


# Enter main game loop
quit = main()

if quit:
    # Do shutdown stuff
    print("Why the fuck you quit, WHY ARE YOU HERE THEN?!.")
    sys.exit(0)


###############
# NOTES & PLANS
###############
# while Tue
#   show progress of last day
#    food - water
#    do ur game stuff
#    if q in resp :
#        end day
