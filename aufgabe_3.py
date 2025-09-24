# Aufgabe 3

# a) Namen einlesen
name = input("Bitte gib deinen Namen ein: ")

# b) Zwei ganze Zahlen einlesen
zahl1_str = input("Gib die erste ganze Zahl ein: ")
zahl2_str = input("Gib die zweite ganze Zahl ein: ")

# Umwandlung der Eingabe in Zahlen
zahl1 = int(zahl1_str)
zahl2 = int(zahl2_str)

# c) Summe berechnen und ausgeben
summe = zahl1 + zahl2
print(f"Hallo, {name}! Die beiden eingegebenen Zahlen haben die Summe {summe}.")
