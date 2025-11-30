# Aufgabe 21
import sys

# --- Teil a) und b): Funktionen für die Grundrechenarten ---

# --- Addition ---
def add(a, b):
    """Führt eine Addition aus und gibt die Rechnung auf dem Bildschirm aus."""
    print(f"{a} + {b} = {a + b}")

def add_R(a, b):
    """Führt eine Addition aus und gibt das Ergebnis zurück."""
    return a + b

# --- Subtraktion ---
def subtract(a, b):
    """Führt eine Subtraktion aus und gibt die Rechnung auf dem Bildschirm aus."""
    print(f"{a} - {b} = {a - b}")

def subtract_R(a, b):
    """Führt eine Subtraktion aus und gibt das Ergebnis zurück."""
    return a - b

# --- Multiplikation ---
def multiply(a, b):
    """Führt eine Multiplikation aus und gibt die Rechnung auf dem Bildschirm aus."""
    print(f"{a} * {b} = {a * b}")

def multiply_R(a, b):
    """Führt eine Multiplikation aus und gibt das Ergebnis zurück."""
    return a * b

# --- Division ---
def divide(a, b):
    """Führt eine Division aus und gibt die Rechnung auf dem Bildschirm aus."""
    if b == 0:
        print("Fehler: Division durch Null ist nicht erlaubt.")
    else:
        print(f"{a} / {b} = {a / b}")

def divide_R(a, b):
    """Führt eine Division aus und gibt das Ergebnis zurück. Gibt None bei Division durch Null."""
    if b == 0:
        return None
    return a / b

# --- Test der Funktionen (wie in Teil a gefordert) ---
print("--- Test der definierten Funktionen ---")
add(7, 9)
ergebnis_add = add_R(7, 9)
print(f"Rückgabewert von add_R(7, 9): {ergebnis_add}\n")

subtract(10, 5)
ergebnis_sub = subtract_R(10, 5)
print(f"Rückgabewert von subtract_R(10, 5): {ergebnis_sub}\n")

multiply(3, 4)
ergebnis_mult = multiply_R(3, 4)
print(f"Rückgabewert von multiply_R(3, 4): {ergebnis_mult}\n")

divide(10, 2)
ergebnis_div = divide_R(10, 2)
print(f"Rückgabewert von divide_R(10, 2): {ergebnis_div}")
divide(10, 0) # Test für Division durch Null
ergebnis_div_null = divide_R(10, 0)
print(f"Rückgabewert von divide_R(10, 0): {ergebnis_div_null}\n")


# --- Teil c): Interaktives Programm ---
print("\n--- Interaktiver Rechner ---")
while True:
    # Eingabe der ersten Zahl
    try:
        num1_str = input("Gib die erste Zahl ein (oder 'exit' zum Beenden): ")
        if num1_str.lower() == 'exit':
            break
        num1 = float(num1_str)
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
        continue

    # Eingabe der Rechenart
    operator = input("Gib die Rechenart ein (+, -, *, /): ")
    if operator not in ['+', '-', '*', '/']:
        print("Ungültige Rechenart.")
        continue

    # Eingabe der zweiten Zahl
    try:
        num2 = float(input("Gib die zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
        continue

    # Ausführung der passenden Funktionen
    print("\n--- Ergebnisse ---")
    if operator == '+':
        add(num1, num2)
        ergebnis = add_R(num1, num2)
        print(f"Die Funktion mit Rückgabewert liefert: {ergebnis}")
    elif operator == '-':
        subtract(num1, num2)
        ergebnis = subtract_R(num1, num2)
        print(f"Die Funktion mit Rückgabewert liefert: {ergebnis}")
    elif operator == '*':
        multiply(num1, num2)
        ergebnis = multiply_R(num1, num2)
        print(f"Die Funktion mit Rückgabewert liefert: {ergebnis}")
    elif operator == '/':
        divide(num1, num2)
        ergebnis = divide_R(num1, num2)
        if ergebnis is not None:
            print(f"Die Funktion mit Rückgabewert liefert: {ergebnis}")
        else:
            print("Die Funktion mit Rückgabewert liefert: Nichts (wegen Division durch Null)")
            
    print("-" * 20 + "\n")

print("Programm beendet.")
