# Aufgabe 22
import random

# Teil a: Funktion, die die größte Zahl und ihren ersten Index findet

def finde_grosste_zahl_einfach(zahlen_liste):
    """
    Sucht die größte Zahl in einer Liste und gibt sie zusammen mit ihrem
    ERSTEN Index zurück.
    Rückgabe: [größte_zahl, erster_index]
    """
    # Fall für eine leere Liste abfangen
    if not zahlen_liste:
        return [None, -1]

    grosste_zahl = zahlen_liste[0]
    erster_index = 0

    # enumerate() gibt uns den Index und den Wert
    for i, zahl in enumerate(zahlen_liste):
        if zahl > grosste_zahl:
            grosste_zahl = zahl
            erster_index = i
            
    # grosste_zahl = max(zahlen_liste)
    # erster_index = zahlen_liste.index(grosste_zahl)

    return [grosste_zahl, erster_index]


# Teil b: Funktion, die die größte Zahl und ALLE ihre Indizes findet

def finde_grosste_zahl_erweitert(zahlen_liste):
    """
    Sucht die größte Zahl in einer Liste und gibt sie zusammen mit einer
    Liste ALLER ihrer Indizes zurück.
    Rückgabe: [größte_zahl, [index1, index2, ...]]
    """
    if not zahlen_liste:
        return [None, []]

    # Finde zuerst die größte Zahl
    grosste_zahl = max(zahlen_liste)
    
    indizes = []
    for i, zahl in enumerate(zahlen_liste):
        if zahl == grosste_zahl:
            indizes.append(i)
    
    return [grosste_zahl, indizes]


# Hauptprogramm

# Erzeuge eine Liste mit 30 Zufallszahlen zwischen -10 und 10
test_liste = [random.randint(-10, 10) for _ in range(30)]

print("--- Testprogramm für Aufgabe 22 ---")
print("Generierte Zufallsliste:")
print(test_liste)
print(f"(Länge der Liste: {len(test_liste)})")

print("\n--- Ergebnis von Teil a) ---")
ergebnis_a = finde_grosste_zahl_einfach(test_liste)
print(f"Funktion 'finde_grosste_zahl_einfach' gibt zurück: {ergebnis_a}")
if ergebnis_a[0] is not None:
    print(f"Die größte Zahl ist {ergebnis_a[0]} und kommt zuerst am Index {ergebnis_a[1]} vor.")

print("\n--- Ergebnis von Teil b) ---")
ergebnis_b = finde_grosste_zahl_erweitert(test_liste)
print(f"Funktion 'finde_grosste_zahl_erweitert' gibt zurück: {ergebnis_b}")
if ergebnis_b[0] is not None:
    print(f"Die größte Zahl ist {ergebnis_b[0]} und kommt an den folgenden Indizes vor: {ergebnis_b[1]}")
