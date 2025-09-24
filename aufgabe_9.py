# Aufgabe 9 - Fakultätsberechnung

# Eingabe der Zahl
n_str = input("Gib eine natürliche Zahl (n >= 1) ein, um die Fakultät zu berechnen: ")
n = int(n_str)

# Überprüfung der Eingabe
if n < 1:
    print("Fehler: Die Zahl muss größer oder gleich 1 sein.")
else:
    # Berechnung der Fakultät mit einer for-Schleife
    fakultaet = 1
    for i in range(1, n + 1):
        fakultaet *= i

    # Ausgabe des Ergebnisses
    print(f"Die Fakultät von {n} (also {n}!) ist: {fakultaet}")
