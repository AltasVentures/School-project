# Aufgabe 14, Teil e
import random

def print_matrix(matrix, title):
    """Hilfsfunktion zur formatierten Ausgabe der Matrix."""
    print(f"\n--- {title} ---")
    if not matrix or not matrix[0]:
        print("[]")
        return
    max_len = max(len(str(item)) for row in matrix for item in row)
    for row in matrix:
        print("  ".join(f"{item:<{max_len}}" for item in row))

# Abfrage der Dimensionen vom Benutzer
try:
    zeilen = int(input("Gib die Anzahl der Zeilen ein: "))
    spalten = int(input("Gib die Anzahl der Spalten ein: "))
    if zeilen <= 0 or spalten <= 0:
        raise ValueError("Zeilen und Spalten müssen positiv sein.")
except ValueError as e:
    print(f"Ungültige Eingabe: {e}")
else:
    # a) Matrix mit Nullen erstellen (benutzerdefinierte Größe)
    matrix = []
    for _ in range(zeilen):
        matrix.append([0] * spalten)
    print_matrix(matrix, f"a) {zeilen}x{spalten}-Matrix mit Nullen")

    # b) Der Eintrag an der Adresse [i][j] soll als neuen Wert die Summe i+j erhalten.
    for i in range(zeilen):
        for j in range(spalten):
            matrix[i][j] = i + j
    print_matrix(matrix, "b) Matrix mit i+j")

    # c) Nun soll jeder Eintrag eine zufällige ganze Zahl zwischen 0 und 20 sein.
    for i in range(zeilen):
        for j in range(spalten):
            matrix[i][j] = random.randint(0, 20)
    print_matrix(matrix, "c) Matrix mit Zufallszahlen (0-20)")
