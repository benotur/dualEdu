from datetime import datetime
import os

def zapis_chybu(chyba):
    with open("errors.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}: {chyba}\n")

while True:
    print("\nKonzolové menu:")
    print("1) Sčítanie")
    print("2) Odčítanie")
    print("3) Násobenie")
    print("4) Delenie")
    print("5) Štatistika")
    print("q) Koniec")

    volba = input("Vyberte možnosť (1/2/3/4/5/q): ")

    if volba == "q":
        print("Koniec programu")
        break

    if volba not in ["1", "2", "3", "4", "5"]:
        chyba = "Neplatná voľba!"
        print(chyba)
        zapis_chybu(chyba)
        continue

    if volba == "5":
        try:
            n = int(input("Koľko čísel chcete zadať? "))
            if n <= 0:
                raise ValueError("Počet čísel musí byť kladný")
            
            cisla = []
            for i in range(n):
                cislo = float(input(f"Zadajte {i+1}. číslo: "))
                cisla.append(cislo)
            
            suma = sum(cisla)
            minimum = min(cisla)
            maximum = max(cisla)
            
            print(f"Súčet: {suma}")
            print(f"Minimum: {minimum}")
            print(f"Maximum: {maximum}")
            continue
        except ValueError:
            chyba = f"Chyba pri štatistike!"
            print(chyba)
            zapis_chybu(chyba)
            continue

    try:
        cislo1 = float(input("Zadajte prvé číslo: "))
        cislo2 = float(input("Zadajte druhé číslo: "))
    except ValueError:
        chyba = "Neplatné číslo!"
        print(chyba)
        zapis_chybu(chyba)
        continue

    if volba == "1":
        vysledok = cislo1 + cislo2
        print(f"{cislo1} + {cislo2} = {vysledok}")
    elif volba == "2":
        vysledok = cislo1 - cislo2
        print(f"{cislo1} - {cislo2} = {vysledok}")
    elif volba == "3":
        vysledok = cislo1 * cislo2
        print(f"{cislo1} * {cislo2} = {vysledok}")
    elif volba == "4":
        if cislo2 == 0:
            chyba = "Nemožno deliť nulou!"
            print(chyba)
            zapis_chybu(chyba)
        else:
            vysledok = cislo1 / cislo2
            print(f"{cislo1} / {cislo2} = {vysledok}")

