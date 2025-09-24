# Aufgabe 14, Teile a-d
import random

def print_matrix(matrix, title):
    """Hilfsfunktion zur formatierten Ausgabe der Matrix."""
    print(f"\n--- {title} ---")
    if not matrix or not matrix[0]:
        print("[]")
        return
    # Finde die maximale Breite für die Spaltenausrichtung
    max_len = max(len(str(item)) for row in matrix for item in row)
    for row in matrix:
        # Formatiere jede Zahl mit der maximalen Breite
        print("  ".join(f"{item:<{max_len}}" for item in row))

# a) Erstelle eine 5x5-Matrix, deren Einträge alle 0 sind.
matrix = []
for _ in range(5):
    matrix.append([0] * 5)
print_matrix(matrix, "a) 5x5-Matrix mit Nullen")

# b) Der Eintrag an der Adresse [i][j] soll als neuen Wert die Summe i+j erhalten.
for i in range(5):
    for j in range(5):
        matrix[i][j] = i + j
print_matrix(matrix, "b) Matrix mit i+j")

# c) Nun soll jeder Eintrag eine zufällige ganze Zahl zwischen 0 und 20 sein.
for i in range(5):
    for j in range(5):
        matrix[i][j] = random.randint(0, 20)
print_matrix(matrix, "c) Matrix mit Zufallszahlen (0-20)")

# d) Matrix symmetrisch machen
for i in range(5):
    for j in range(5):
        if j < i:
            matrix[i][j] = matrix[j][i]
print_matrix(matrix, "d) Symmetrische Matrix")
