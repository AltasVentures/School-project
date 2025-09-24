# Aufgabe 12 - Würfel-Statistik
import random

# a) Liste mit 100 Zufallszahlen (Würfelergebnisse)
wuerfe = []
for _ in range(100):
    wuerfe.append(random.randint(1, 6))

print("Die 100 Würfelergebnisse:")
print(wuerfe)

# b) Häufigkeit der einzelnen Zahlen zählen

# 1) Liste 'anzahl' mit sieben Nullen erstellen
anzahl = [0] * 7 # Index 0 wird nicht benötigt

# 2) Würfe durchgehen und zählen
for wurf in wuerfe:
    anzahl[wurf] += 1

# Ergebnisse ausgeben
print("\nHäufigkeitsverteilung:")
for i in range(1, 7):
    print(f"Die {i} wurde {anzahl[i]}-mal gewürfelt.")
