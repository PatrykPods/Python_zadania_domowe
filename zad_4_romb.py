counter = int(input("podaj liczbe:"))

x = 0
y = 0

while x < counter :
    print(" " * (counter - x) + "/" + " " * x  * 2   +  "\\" )

    x += 1
while y < counter :
    print(" " * (y + 1) + "\\" + " " *  (((counter - y)) - 1) * 2 + "/")

    y += 1