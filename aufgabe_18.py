# Aufgabe 18
import random

# Versuche, matplotlib zu importieren. Wenn es nicht da ist, gib eine
# Fehlermeldung aus, da das Programm sonst abstürzt.
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Fehler: Das Paket 'matplotlib' ist nicht installiert.")
    print("Bitte installiere es mit dem Befehl: pip install matplotlib")
    # Beende das Skript, wenn das Paket fehlt
    exit()

# Erzeuge die Daten
# x-Werte sind die Zahlen von 1 bis 8
x_werte = list(range(1, 9))
# y-Werte sind 8 Zufallszahlen zwischen 1 und 10
y_werte = [random.randint(1, 10) for _ in range(8)]

print(f"Verwende x-Werte: {x_werte}")
print(f"Verwende zufällige y-Werte: {y_werte}")

# --- Diagramm 1: Blaue Linie ---
plt.figure(1) # Erstellt eine neue "Zeichenfläche" für das erste Diagramm
plt.plot(x_werte, y_werte, color='blue', linestyle='-')
plt.xlabel("X-Achse (Werte 1-8)")
plt.ylabel("Y-Achse (Zufallszahlen)")
plt.title("Diagramm 1: Blaue durchgezogene Linie")
plt.grid(True) # Fügt ein Gitter hinzu zur besseren Lesbarkeit
plt.savefig('aufgabe_18_diagramm_1.png')
print("Diagramm 1 als 'aufgabe_18_diagramm_1.png' gespeichert.")

# --- Diagramm 2: Rote gestrichelte Linie mit Punkten ---
plt.figure(2)
plt.plot(x_werte, y_werte, color='red', linestyle='--', marker='o')
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.title("Diagramm 2: Rote gestrichelte Linie mit Kreisen")
plt.grid(True)
plt.savefig('aufgabe_18_diagramm_2.png')
print("Diagramm 2 als 'aufgabe_18_diagramm_2.png' gespeichert.")

# --- Diagramm 3: Grüne Punkte (Scatter Plot) ---
plt.figure(3)
plt.scatter(x_werte, y_werte, color='green', marker='x')
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.title("Diagramm 3: Grüne 'x'-Punkte")
plt.grid(True)
plt.savefig('aufgabe_18_diagramm_3.png')
print("Diagramm 3 als 'aufgabe_18_diagramm_3.png' gespeichert.")

# --- Diagramm 4: Schwarze nur-Punkte-Linie ---
plt.figure(4)
plt.plot(x_werte, y_werte, color='black', linestyle='None', marker='*')
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.title("Diagramm 4: Nur Sterne, keine Linie")
plt.grid(True)
plt.savefig('aufgabe_18_diagramm_4.png')
print("Diagramm 4 als 'aufgabe_18_diagramm_4.png' gespeichert.")

# plt.show() # Würde die Diagramme in einem Fenster anzeigen, wenn man es interaktiv nutzt.
# Für dieses Skript speichern wir sie nur als Dateien.
