
import sqlite3
import subprocess
import os
import tkinter as tk
from tkinter import filedialog

DATABASE_NAME = "file_database.db"

def setup_database():
    """Erstellt die Datenbank und die Tabelle, falls sie nicht existieren."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        path TEXT NOT NULL UNIQUE
    )
    """)
    conn.commit()
    conn.close()

def add_file():
    """Öffnet einen Datei-Explorer, um eine Datei auszuwählen und sie zur DB hinzuzufügen."""
    print("Öffne Dateiauswahl-Dialog...")
    try:
        root = tk.Tk()
        root.withdraw()  # Versteckt das Hauptfenster
        file_path = filedialog.askopenfilename(title="Wähle eine Datei zum Hinzufügen aus")
        root.destroy()

        if not file_path:
            print("Keine Datei ausgewählt.")
            return

        file_name = os.path.basename(file_path)
        
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO files (name, path) VALUES (?, ?)", (file_name, file_path))
            conn.commit()
            print(f"Datei '{file_name}' erfolgreich hinzugefügt.")
        except sqlite3.IntegrityError:
            print(f"Fehler: Die Datei '{file_name}' ist bereits in der Datenbank vorhanden.")
        finally:
            conn.close()

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        print("Stellen Sie sicher, dass eine grafische Benutzeroberfläche verfügbar ist (z.B. X11, Wayland).")


def execute_file(path):
    """Führt die ausgewählte Datei als Python-Skript aus."""
    print(f"\n--- Führe Skript aus: {os.path.basename(path)} ---\n")
    try:
        # Wir nehmen an, dass es sich um Python-Skripte handelt
        result = subprocess.run(["python3", path], capture_output=True, text=True, check=True)
        print("--- Ausgabe ---")
        print(result.stdout)
        if result.stderr:
            print("--- Fehler ---")
            print(result.stderr)
    except FileNotFoundError:
        print(f"Fehler: 'python3' wurde nicht gefunden. Stellen Sie sicher, dass Python installiert ist.")
    except subprocess.CalledProcessError as e:
        print("--- Fehler bei der Ausführung ---")
        print(e.stdout)
        print(e.stderr)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    print("\n--- Ausführung beendet ---\n")


def delete_file(file_id):
    """Löscht eine Datei aus der Datenbank."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM files WHERE id = ?", (file_id,))
    conn.commit()
    conn.close()
    print("Datei erfolgreich aus der Datenbank gelöscht.")

def show_and_select_files():
    """Zeigt alle Dateien an und lässt den Benutzer eine für Aktionen auswählen."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, path FROM files ORDER BY name")
    files = cursor.fetchall()
    conn.close()

    if not files:
        print("Keine Dateien in der Datenbank gespeichert.")
        return

    print("\n--- Gespeicherte Dateien ---")
    for file in files:
        print(f"{file['id']}: {file['name']}")
    print("--------------------------")

    try:
        choice_str = input("Gib die Nummer der Datei ein, die du verwalten möchtest (oder 'q' zum Abbrechen): ")
        if choice_str.lower() == 'q':
            return
        
        choice_id = int(choice_str)
        selected_file = next((f for f in files if f['id'] == choice_id), None)

        if not selected_file:
            print("Ungültige Auswahl.")
            return

        while True:
            print(f"\n--- Aktionen für: {selected_file['name']} ---")
            print("1. Ausführen")
            print("2. Löschen")
            print("3. Zurück zur Übersicht")
            action_choice = input("Deine Wahl: ")

            if action_choice == '1':
                execute_file(selected_file['path'])
            elif action_choice == '2':
                delete_file(selected_file['id'])
                break 
            elif action_choice == '3':
                break
            else:
                print("Ungültige Aktion.")

    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


def main():
    """Hauptschleife des Programms."""
    setup_database()
    while True:
        print("\n===== Datei-Manager =====")
        print("1. Neues File hinzufügen")
        print("2. Alle gespeicherten Files zeigen")
        print("3. Beenden")
        choice = input("Was möchtest du tun? ")

        if choice == '1':
            add_file()
        elif choice == '2':
            show_and_select_files()
        elif choice == '3':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte versuche es erneut.")

if __name__ == "__main__":
    main()
