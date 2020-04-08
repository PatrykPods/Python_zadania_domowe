counter = int(input("podaj liczbe:"))

x = 0

while x < counter :
    if x == 0 or x == counter - 1 :
        print("*" * counter)
    elif x > 0 and x < counter :
        print("*" + " " * (counter - 2) + "*")
    x += 1

