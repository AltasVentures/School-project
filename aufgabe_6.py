# Aufgabe 6 - Ein kleines Glücksspiel
import random

# a) Zufallszahl des Computers
computer_zahl = random.randint(0, 100)

# b) Zufällige Kommazahl für die Entscheidung
entscheidung = random.random()

# c) Benutzereingabe
benutzer_zahl_str = input("Gib eine ganze Zahl zwischen 0 und 100 ein: ")
benutzer_zahl = int(benutzer_zahl_str)

# d) Bereichsprüfung
if not (0 <= benutzer_zahl <= 100):
    print("Zahl nicht im geforderten Bereich.")
else:
    # e) Spielauswertung
    print(f"Meine Zahl ist {computer_zahl}, deine ist {benutzer_zahl}.")
    if entscheidung <= 0.5: # Kleinere Zahl gewinnt
        print("Die kleinere Zahl gewinnt heute.")
        if computer_zahl < benutzer_zahl:
            print("Ich gewinne!")
        elif benutzer_zahl < computer_zahl:
            print("Du gewinnst!")
        else:
            print("Unentschieden!")
    else: # Größere Zahl gewinnt
        print("Die größere Zahl gewinnt heute.")
        if computer_zahl > benutzer_zahl:
            print("Ich gewinne!")
        elif benutzer_zahl > computer_zahl:
            print("Du gewinnst!")
        else:
            print("Unentschieden!")
