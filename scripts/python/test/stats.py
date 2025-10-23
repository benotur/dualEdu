while True:
    try:
        n = int(input("How many values do you wanna use? (positive integer): "))
        if n > 0:
            break
    except:
        pass

values = []
for i in range(n):
    values.append(int(input(f"Enter number {i+1}: ")))

print("\nOutput:")
print(f"sum: {sum(values)}")
print(f"min: {min(values)}")
print(f"max: {max(values)}")
