# Aufgabe 4

# a) Zwei Zahlen einlesen
a_str = input("Gib die erste natürliche Zahl ein: ")
b_str = input("Gib die zweite natürliche Zahl ein: ")
a = int(a_str)
b = int(b_str)

# b) Rechenart einlesen
eingabe = input("Gib eine der folgenden Rechenarten ein (add, sub, mult, div): ")

# c) Berechnung und Ausgabe
if eingabe == 'add':
    print(f"Die Summe ist: {a + b}")
elif eingabe == 'sub':
    print(f"Die Differenz ist: {a - b}")
elif eingabe == 'mult':
    print(f"Das Produkt ist: {a * b}")
elif eingabe == 'div':
    # d) Fehler bei Division durch Null abfangen
    if b == 0:
        print("Fehler: Division durch Null ist nicht erlaubt!")
    else:
        print(f"Der Quotient ist: {a / b}")
else:
    print("Falsche Eingabe bei der Grundrechenart!")
