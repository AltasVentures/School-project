# Aufgabe 7

# a) Summe der Zahlen von 1 bis 10
summe_1_bis_10 = 0
for i in range(1, 11):
    summe_1_bis_10 += i
print(f"Die Summe der Zahlen von 1 bis 10 ist: {summe_1_bis_10}")

print("\n--------------------\n")

# b) Summe bis zu einer eingegebenen Zahl

# Eingabe der Obergrenze
limit_str = input("Gib eine natürliche Zahl größer als 1 ein: ")
limit = int(limit_str)

# Prüfung der Eingabe
if limit <= 1:
    print("Fehler: Die Zahl muss größer als 1 sein.")
else:
    # Hinweis bei großer Zahl
    if limit > 100:
        print("Hinweis: Die eingegebene Zahl ist größer als 100!")

    # Berechnung der Summe
    summe_benutzer = 0
    for i in range(1, limit + 1):
        summe_benutzer += i

    # Ausgabe des Ergebnisses
    print(f"Die Summe der Zahlen von 1 bis {limit} ist: {summe_benutzer}")
