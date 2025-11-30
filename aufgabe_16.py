# Aufgabe 16
import random

# Teil b: Einlesen der Zahlen aus einer einzigen Zeile
print("--- Aufgabe 16b ---")
try:
    with open('aufgabe_16_ab.txt', 'r') as datei:
        # Lese die eine Zeile und entferne führende/folgende Leerzeichen
        text_zeile = datei.readline().strip()
        # Teile den Text am Komma, um eine Liste von Text-Zahlen zu erhalten
        zahlen_als_text = text_zeile.split(',')
        # Wandle jede Text-Zahl in eine echte Zahl (Integer) um
        zahlen_liste_b = [int(num) for num in zahlen_als_text]
        print("Erstellte Liste aus 'aufgabe_16_ab.txt':")
        print(zahlen_liste_b)
except FileNotFoundError:
    print("Fehler: 'aufgabe_16_ab.txt' nicht gefunden.")
except ValueError:
    print("Fehler: Die Datei enthält ungültige Zeichen, die nicht in Zahlen umgewandelt werden können.")

print("\n" + "="*20 + "\n")

# Teil c: Einlesen der Zahlen aus mehreren Zeilen
print("--- Aufgabe 16c ---")
zahlen_liste_c = []
try:
    with open('aufgabe_16_c.txt', 'r') as datei:
        # Lese den gesamten Inhalt der Datei
        gesamter_text = datei.read()
        # Ersetze die Zeilenumbrüche durch ein Komma, um eine lange, durch Kommas getrennte Zeichenkette zu erhalten
        gesamter_text = gesamter_text.replace('\n', ',')
        # Teile den Text am Komma
        zahlen_als_text_c = gesamter_text.split(',')
        # Wandle Text in Zahlen um. Wir filtern auch leere Einträge heraus, falls welche entstehen.
        for num_text in zahlen_als_text_c:
            if num_text: # Stellt sicher, dass der String nicht leer ist
                zahlen_liste_c.append(int(num_text))
        print("Erstellte Liste aus 'aufgabe_16_c.txt':")
        print(zahlen_liste_c)

    # Teil d: Zwei zufällige Zahlen auswählen und addieren
    print("\n--- Aufgabe 16d ---")
    if len(zahlen_liste_c) >= 2:
        # Wähle zwei zufällige Zahlen aus der Liste von Teil c
        zahl1 = random.choice(zahlen_liste_c)
        zahl2 = random.choice(zahlen_liste_c)

        # Addiere die Zahlen
        summe = zahl1 + zahl2

        print(f"Zufallszahl 1: {zahl1}")
        print(f"Zufallszahl 2: {zahl2}")
        print(f"Summe: {zahl1} + {zahl2} = {summe}")
    else:
        print("Nicht genügend Zahlen in der Liste für die Zufallsauswahl.")

except FileNotFoundError:
    print("Fehler: 'aufgabe_16_c.txt' nicht gefunden.")
except ValueError:
    print("Fehler: Die Datei enthält ungültige Zeichen, die nicht in Zahlen umgewandelt werden können.")
