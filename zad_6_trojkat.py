counter = int(input("podaj liczbe"))

x = 0

while x < counter :
    if x == 0 :
        print("*" * counter)
    elif x > 0 and x < counter - 1:
        print("*" + " " *(counter - x - 2)  + "*")
    elif x == counter - 1:
        print("*")

    x += 1