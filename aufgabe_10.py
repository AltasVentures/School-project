# Aufgabe 10 - Zahlen raten
import random

def zahlenraten_spiel():
    spielen = True
    while spielen:
        # Schwierigkeitsgrad für den Computergegner wählen
        print("\nWähle den Schwierigkeitsgrad für den Computergegner:")
        print("1) Leicht (rät zufällig)")
        print("2) Mittel (grenzt den Bereich ein)")
        print("3) Schwer (gewinnt nach deinem 10. Versuch)")
        schwierigkeit = input("Deine Wahl (1, 2 oder 3): ")

        geheime_zahl = random.randint(1, 100)
        versuche = 0
        geraten = False
        comp_min = 1
        comp_max = 100

        print("\nIch habe mir eine Zahl zwischen 1 und 100 ausgedacht. Versuche sie zu erraten!")

        while not geraten and versuche < 30:
            # Benutzer ist an der Reihe
            try:
                tipp_str = input(f"Dein {versuche + 1}. Versuch: ")
                tipp = int(tipp_str)
                versuche += 1

                if tipp == geheime_zahl:
                    print(f"Glückwunsch! Du hast die Zahl {geheime_zahl} in {versuche} Versuchen erraten!")
                    geraten = True
                elif tipp < geheime_zahl:
                    print("Deine Zahl ist zu klein.")
                    comp_min = max(comp_min, tipp + 1)
                else:
                    print("Deine Zahl ist zu groß.")
                    comp_max = min(comp_max, tipp - 1)

            except ValueError:
                print("Bitte gib eine gültige Zahl ein.")
                continue

            if geraten:
                break

            # Computergegner ist an der Reihe
            if schwierigkeit == '1':
                comp_tipp = random.randint(1, 100)
            elif schwierigkeit == '2':
                comp_tipp = random.randint(comp_min, comp_max)
            elif schwierigkeit == '3' and versuche >= 10:
                comp_tipp = geheime_zahl
            else: # Fallback für Schwierigkeit 3 vor dem 10. Versuch
                comp_tipp = random.randint(comp_min, comp_max)

            print(f"Der Computer rät: {comp_tipp}")
            if comp_tipp == geheime_zahl:
                print(f"Der Computer hat die Zahl {geheime_zahl} erraten und gewinnt!")
                geraten = True
            else:
                print("Der Computer hat falsch geraten.")

        if not geraten:
            print(f"Schade, du hast die Zahl {geheime_zahl} nach 30 Versuchen nicht erraten.")

        # Frage nach einem neuen Spiel
        nochmal = input("Willst du noch eine Runde spielen? (ja/nein): ").lower()
        if nochmal != 'ja':
            spielen = False
            print("Danke fürs Spielen!")

# Spiel starten
zahlenraten_spiel()
