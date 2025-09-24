# Aufgabe 5
import random

# Vier Zufallszahlen zwischen 1 und 10 erzeugen
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)

# Werte auf dem Bildschirm ausgeben
print(f"Die vier Zufallszahlen sind: {a}, {b}, {c}, {d}")

# Überprüfen, ob mindestens zwei Zahlen gleich sind
if a == b or a == c or a == d or b == c or b == d or c == d:
    print("Was für ein Zufall!")
else:
    print("War zu erwarten!")
