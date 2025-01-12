# Rekenen in Python

Python kan gebruikt worden als rekenmachine. 

```python
print(2 + 3)
```

Dit zal 5 afdrukken. 

De meeste operaties zijn hetzelfde als op je rekentoestel. Enkel de machtsverheffing is anders. I.p.v. `^` gebruik je `**`.

```python
print(2 ** 3)
```

Dit zal 8 afdrukken.

# Variabelen

Een variabele is een naam die je aan een waarde kan geven. Je kan een variabele maken door de naam van de variabele te schrijven gevolgd door een isgelijkteken en de waarde die je aan de variabele wilt geven. 

```python
a = 5
```

Dit zal de waarde 5 aan de variabele `a` geven.

Je kan de waarde van een variabele afdrukken door de naam van de variabele te schrijven. 

```python
print(a)
```

Dit zal 5 afdrukken.

Je kan de waarde van een variabele veranderen door de naam van de variabele te schrijven gevolgd door een isgelijkteken en de nieuwe waarde die je aan de variabele wilt geven. 

```python
a = 10
```

Dit zal de waarde van de variabele `a` veranderen naar 10.

Je kan de waarde van de variabele aanpassen op basis van zijn eigen waarde. Zo verhoog je de variabele met 2 als volgt:

```python
a = a + 2
```

Dit zal de waarde van de variabele `a` verhogen met 2.

Wil je die vermenigvuldigen met 2, dan doe je dit:

```python
a = a * 2
```

Geef je variabelen een goede naam. Zo weet je later nog wat ze betekenen.

Niet goed:

```python
x = 5
```

Wel goed:

```python
aantal_studenten = 5
```

# De for-lus en range

De for-lus is een lus die een bepaald aantal keer herhaald wordt. De for-lus heeft de volgende structuur. 

```python
for i in range(5):
    print(i)
```

Dit zal de getallen van 0 tot 4 afdrukken. Merk op dat we dus altijd van 0 beginnen te tellen en dat we TOT 5 gaan en niet TOT EN MET 5.

```python 
0
1
2
3
4
```

De functie `range` maakt een reeks getallen aan. De functie `range` heeft de volgende structuur. 

```python
range(start, stop, stap)
```

De functie `range` maakt een reeks getallen aan van `start` tot `stop` met een stapgrootte van `stap`. De `start` is optioneel en is standaard 0. De `stap` is optioneel en is standaard 1. 

```python
for i in range(1, 6, 2):
    print(i)
```

Dit zal de getallen van 1 tot 5 afdrukken met een stapgrootte van 2. 

```python
1
3
5
```

De stapgrootte kan ook negatief zijn. 

```python
for i in range(5, 0, -1):
    print(i)
```

Dit zal de getallen van 5 tot 1 afdrukken. 

```python
5
4
3
2
1
```

# Lijsten

## Lijsten manipuleren

Een lijst is een verzameling van elementen. Deze elementen kunnen van verschillende types zijn. Een lijst kan je maken door de elementen tussen vierkante haken te zetten en te scheiden door komma's. 

```python
lijst = [1, 2, 3, 4, 5]
```

De positie van elk element in de lijst wordt de index genoemd. De index begint bij 0. 

```python
print(lijst[0])
```

Dit zal het eerste element van de lijst afdrukken. 

```python
1
``` 

Elementen toevoegen aan een lijst doe je met append.

```python
lijst.append(6)
print(lijst)
```

Dit zal het getal 6 toevoegen aan de lijst en geeft dus als output

```python
[1, 2, 3, 4, 5, 6]
```
   
## Lijsten doorlopen

Je kan over een lijst loopen met een for-lus. 

```python
for element in lijst:
    print(element)
```

Dit zal elk element van de lijst afdrukken.

```python
1
2
3
4
5
```

In veel gevallen heb je de positie van het element nodig. Dit kan je doen door de functie `range` te gebruiken. 

```python
for i in range(len(lijst)):
    print("op positie", i, "staat het element", lijst[i])
```

Dit zal de index en het element afdrukken.

```python
op positie 0 staat het element 1
op positie 1 staat het element 2
op positie 2 staat het element 3
op positie 3 staat het element 4
op positie 4 staat het element 5
```

# Functies

Een functie is een stukje code dat je kan hergebruiken. Een functie heeft de volgende structuur. 

```python
def plus(argument1, argument2):
    resultaat = argument1 + argument2
    return resultaat
```

Vergelijk dit met een wiskundige functie. Vergeet niet dat een functie meestal een waarde teruggeeft. Dit doe je met het `return`-statement. Wanneer je een nieuwe functie schrijft, start je best van een vast formaat.

```python
def goede_functie_naam(goede_argument1_naam, goede_argument2_naam, ...):
    # zet de variabele resultaat op een logische startwaarde
    resultaat = 0
    
    # hier komt je code
    
    return resultaat
```

Op die manier vermijd je een hoop bugs (return vergeten, resultaat niet gedefinieerd, ...).

## Ingebouwde functies

Er bestaan een aantal ingebouwde functies die je kan gebruiken voor lijsten. 

```python
lijst = [1, 2, 3, 4, 5]
print(sum(lijst))
print(max(lijst))
print(min(lijst))
print(len(lijst))
```

In de math library zitten nog een hoop andere wiskundige functies. 

```python
import math
print(math.sqrt(16))
print(math.factorial(5))
```