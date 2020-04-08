spk = float(input("podaj stan poczatkowy konta"))
n = int(input("ile pelnych lat mineło?"))
p = float(input("podaj oprocentowanie:"))

p = p / 100

result = spk * ( 1 + p)**n

print(f"Stan konta po {n} latach to {result:.2f} zl.")