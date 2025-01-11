##########
## Gebruik volgende functies om te bewegen in de doolhof:
## 
## goForward():
##   Beweeg één vakje vooruit
##
## turnRight():
##   Draai een kwartslag naar rechts
##
## turnLeft():
##   Draai een kwartslag naar links
##
## foundExit():
##   Kijkt na of je op de uitgang staat
##
## freeForward():
##   Kijkt na of er recht voor je een open vakje is (=geen muur)
##
## freeRight():
##   Kijkt na of er rechts van je een open vakje is
##
## freeLeft():
##   Kijkt na of er links van je een open vakje is
##
## vooruit/links/rechts wordt altijd vanuit het oogpunt van het pijltje bekeken
##
## while conditie:
## 	code
##	code
##    Zolang de conditie waar is voer je de lijnen code uit
##
## if conditie1:
##	code1
##	code1
## elif conditie2:
## 	code2
## 	code2
## else:
## 	codea
## 	codea
##    Voer de lijnen code1 uit als coditie 1 waar is, 
##			     code2 als conditie1 niet en conditie2 wel waar zijn,
##                   codea in alle andere gevallen
##########

from doolhof import *

# Vraag 3: Los doorhof 4 op
laadDoolhof("doolhof4.txt")    
# laadDoolhof("doolhof5.txt") # 4 gelukt? vervang vorige regel dan door deze!

    
        
#sluit venster pas als op 'close' geklikt wordt
wait_for_click()