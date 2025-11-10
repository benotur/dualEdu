from utils import is_even, avg

nums = []
while True:
    try:
        vstup = input("Zadajte číslo (prázdny riadok pre ukončenie): ")
        if not vstup:
            break
        nums.append(float(vstup))
    except ValueError:
        print("Neplatný vstup. Prosím zadajte platné číslo.")

if nums:
    pocet = len(nums)
    priemer = avg(nums)
    pocet_parnych = sum(1 for n in nums if is_even(int(n)))
    print(f"Počet čísel: {pocet}")
    print(f"Priemer: {priemer:.2f}")
    print(f"Počet párnych čísel: {pocet_parnych}")
else:
    print("Neboli zadané žiadne čísla.")
