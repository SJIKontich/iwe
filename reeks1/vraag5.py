# Tel het aantal stappen om het doolhof op te lossen
# Voeg nu toe om alle linkse en rechtse bochten te tellen

from doolhof import *

# Right-hand rule
laadDoolhof("doolhof4.txt")
steps = 0
while not foundExit():
    steps = steps + 1
    if freeRight():  # right is free
        turnRight()
        goForward()
    elif freeForward():  # not right, but forward is free
        goForward()
    elif freeLeft():  # not right, not forward, but left free
        turnLeft()
        goForward()
    else:  # neither right, nor forward, nor left are free
        turnLeft()
        turnLeft()
        goForward()

print("Aantal stappen:", steps)

#sluit venster pas als op 'close' geklikt wordt
wait_for_click()
