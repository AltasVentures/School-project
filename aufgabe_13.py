# Aufgabe 13 - Matrizenaddition
import random

def print_matrix(matrix, name):
    """Hilfsfunktion, um eine Matrix formatiert auszugeben."""
    print(f"\nMatrix: {name}")
    for zeile in matrix:
        print("  ".join(map(str, zeile)))

# a) Zwei 3x3-Matrizen mit Zufallszahlen füllen
matrix_1 = []
for _ in range(3):
    zeile = [random.randint(0, 9) for _ in range(3)]
    matrix_1.append(zeile)

matrix_2 = []
for _ in range(3):
    zeile = [random.randint(0, 9) for _ in range(3)]
    matrix_2.append(zeile)

# b) Dritte 3x3-Matrix mit Nullen erstellen
matrix_summe = []
for _ in range(3):
    matrix_summe.append([0, 0, 0])

# c) Summe der Matrizen berechnen
# Durchlaufe die Zeilen
for i in range(3):
    # Durchlaufe die Spalten
    for j in range(3):
        matrix_summe[i][j] = matrix_1[i][j] + matrix_2[i][j]

# d) Alle drei Matrizen ausgeben
print_matrix(matrix_1, "Matrix_1")
print_matrix(matrix_2, "Matrix_2")
print_matrix(matrix_summe, "Summe")
