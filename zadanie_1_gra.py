while True:
    x = int(input("podaj pozycje gracza X:"))
    y = int(input("podaj pozycje gracza Y:"))

    if x > 100 or y > 100 :
        print("gracz jest poza plansza")

    elif x <= 10 and y <= 10 :
         print("gracz znajduje sie w lewym dolnym rogu")
    elif x >= 90 and y <= 10 :
        print("gracz znajduje sie w prawym dolnym rogu")
    elif x <= 10 and y >= 90 :
        print("gracz znajduje sie w lewym gornym rogu")
    elif x >= 90 and y >= 90 :
        print("gracz znajduje sie w prawym gornym rogu")
    elif x > 10 and y <= 10 :
        print("gracz znajduje sie na dolnej krawedzi")
    elif x > 10 and y >= 90 :
        print("gracz znajduje sie na gornej krawedzi")
    elif x <= 10 and y > 10 :
        print("gracz znajduje sie na lewej krawedzi")
    elif x >= 90 and y > 10 :
        print("gracz znajduje sie na prawej krawedzi")
    else :
        print("gracz znajduje sie w centrum")


    q = input("czy chcesz kontynowac? tak/nie")

    if q == "nie"  :
        break


