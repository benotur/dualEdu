vstup = input("Zadaj ľubovoľný počet čísel oddelených medzerou: ")
cisla = [float(x) for x in vstup.split()]

sucet = sum(cisla)
minimum = min(cisla)
maximum = max(cisla)

subor = open("./vypis.txt", "a")

print("\nČo chceš spraviť s výsledkami?")
print("1 - Len vypísať na obrazovku")
print("2 - Len uložiť do súboru")
print("3 - Vypísať aj uložiť")
volba = input("Zadaj číslo (1/2/2): ")

vypis = (
    "=== Výpis zo vstupov ===\n"
    f"Počet čísel: {len(cisla)}\n"
    f"Súčet: {sucet:.2f}\n"
    f"Minimum: {minimum:.2f}\n"
    f"Maximum: {maximum:.2f}\n"
) # treba napisat to cez funkciu, daj funkciu co returnuje string, neni to zly sposob co robis ale pythonu sa stym nechce pracovat

if volba == "1":
    print("\n" + vypis)
elif volba == "2":

    print("\nVýpis bol uložený do súboru 'vypis.txt'.")
elif volba == "3":
    subor.write(vypis)
    print("\n" + vypis)
    print("\nVýpis bol zároveň uložený do súboru 'vypis.txt'")
