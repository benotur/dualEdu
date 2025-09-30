while True:
    num1 = float(input("Zadaj prvé číslo: "))
    num2 = float(input("Zadaj druhé číslo: "))
    op = input("Vyber si operáciu (+, -, *, /): ")

    if op == "+":
        result = num1 + num2
        break
    elif op == "-":
        result = num1 - num2
        break
    elif op == "*":
        result = num1 * num2
        break
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
            break
        else:
            print("Chyba: Delenie nulou. Skús to znova.")
    else:
        print("Neplatná operácia. Skús to znova.")

print("Výsledok:", num1, op, num2, "=", result)
