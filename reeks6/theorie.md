# Files

Werken met files is ongeveer hetzelfde als werken met een lijst. 
In Python wordt een file als een lijst van strings beschouwd. 
Je kan een file lezen met de `open()` functie. 

Als je een bestand opent, moet je het ook sluiten met de `close()` functie.

Een regel inlezen doe je met de `readline()` functie.

```python
file = open('bestand.txt', 'r')
line = file.readline()
print(line)
```

Je kan meerdere regels inlezen met een `for` lus, net zoals een lijst.

```python
file = open('bestand.txt', 'r')
for line in file:
    print(line)
file.close()
```

Er is 1 nadeel. Een regel wordt ingelezen met een newline karakter (`\n`, d.w.z. een enter). 
Je kan dit verwijderen met de `strip()` functie.

```python
file = open('bestand.txt', 'r')
for line in file:
    line = line.strip()
    print(line)
file.close()
```

Soms staan er meerdere waarden op een regel, gescheiden door een spatie. 
Als je een regel inleest, kan je deze opsplitsen met de `split()` functie.
Die geeft dan een lijst terug met de waarden.

```python
file = open('bestand.txt', 'r')
for line in file:
    line = line.strip()
    values = line.split(' ')
    print(values)
file.close()
```

Je kan ook een file schrijven. Denk eraan als je een nieuwe regel wil schrijven, moet je een newline karakter toevoegen.

```python
file = open('bestand.txt', 'w')
file.write('Hello, world!\n')
file.close()
```

Als je schrijft naar een bestand, moet je altijd een string meegeven. Je kan een getal omzetten naar een string met de `str()` functie.

```python
file = open('bestand.txt', 'w')
file.write(str(42) + '\n')
file.close()
```
