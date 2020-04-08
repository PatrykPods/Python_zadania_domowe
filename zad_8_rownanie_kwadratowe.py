import math
print("Podaj wartości parametrów a, b orac c dla rownania kwadratowego pod postacia ax2+bx+c=0")

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

if a != 0 :

    delta = b ** 2 - (4 * a * c)
    if delta > 0 :
        x_1 = (-b - math.sqrt(delta)) / (2*a)
        x_2 = (-b + math.sqrt(delta)) / (2*a)

        print(f"delta: {delta:.2f}. Równanie posiada dwa rozwiaznia: x_1 = {x_1:.2f} i x_2 = {x_2:.2f}")
    elif delta == 0 :

        x_0 = -(b / (2*a))

        print(f"Delta: 0. Rownanie posiada jedno rozwiazanie: x_0 = {x_0:.2f} ")
    else :
        print("Delta ujemna. Rownanie nie posiada rozwiazan")
else :
    print("Nie jest to rownanie kwadratowe.")
