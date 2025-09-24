# Aufgabe 11 - Listenmanipulation

# a) Liste von 0 bis 100 erstellen
meine_liste = []
for i in range(101):
    meine_liste.append(i)
# print("a)", meine_liste)

# b) 50. Eintrag (Index 49) ersetzen
meine_liste[49] = "Quatsch"
# print("b)", meine_liste)

# c) "Quatsch" entfernen
meine_liste.remove("Quatsch")
# print("c)", meine_liste)

# d) Werte an Index 3 und 5 vertauschen
hilfs_variable = meine_liste[3]
meine_liste[3] = meine_liste[5]
meine_liste[5] = hilfs_variable
# print("d)", meine_liste)

# e) Zweite Liste von 100 bis 0 erstellen
zweite_liste = []
for i in range(100, -1, -1):
    zweite_liste.append(i)
# print("e)", zweite_liste)

# f) Zweite Liste an die erste anhängen
meine_liste.extend(zweite_liste)
# print("f)", meine_liste)

# g) Liste sortieren und die erste 50 entfernen
meine_liste.sort()
meine_liste.remove(50)
# print("g)", meine_liste)

# h) Index der ersten 48 ausgeben
index_48 = meine_liste.index(48)
print(f"Der Index, an dem zum ersten Mal die Zahl 48 vorkommt, ist: {index_48}")

print("\nEndgültige Liste (zur Kontrolle):")
# print(meine_liste)
