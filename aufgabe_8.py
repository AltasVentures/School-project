# Aufgabe 8 - Potenzberechnung

# Eingabe von Basis und Exponent
a_str = input("Gib die Basis (a > 0) ein: ")
b_str = input("Gib den Exponenten (b > 0) ein: ")
a = int(a_str)
b = int(b_str)

# Überprüfung der Eingaben
if a <= 0 or b <= 0:
    print("Fehler: Basis und Exponent müssen größer als 0 sein.")
else:
    # Berechnung der Potenz mit einer for-Schleife
    potenz = 1
    for _ in range(b):
        potenz *= a

    # Ausgabe des Ergebnisses
    print(f"{a} hoch {b} ist: {potenz}")
