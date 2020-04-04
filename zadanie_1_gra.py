while True:
    x = int(input("podaj pozycje gracza X:"))
    y = int(input("podaj pozycje gracza Y:"))

    if x > 10 and x < 90 and y > 10 and y < 90 :
        print("Gracz znajduje sie w centrum")
    elif x >= 1 and x <= 10 and y > 10 and y < 90 :
        print("Gracz znajduje sie na lewej krawedzi")
    elif x >= 90 and x <= 100 and y > 10 and y < 90 :
        print("Gracz znajduje sie na prawej krawedzi")
    elif x > 10 and x < 90 and y >= 1 and y <= 10 :
        print("gracz znajduje sie na dolnej krawedzi")
    elif x > 10 and x < 90 and y >= 90 and y <= 100 :
        print("gracz znajduje sie na gornej krawedzi")
    elif x >= 1 and x <= 10 and y >= 1 and y <= 10 :
        print("Gracz znajduje sie w lewym dolnym rogu")
    elif x >= 1 and x <= 10 and y >= 90 and y <= 100 :
        print("gracz znajduje sie w lewym gornym rogu")
    elif x >= 90 and x <= 100 and y >= 1 and y <= 10 :
        print("gracz znajduje sie w prawym dolnym rogu")
    elif x >= 90 and x <= 100 and y >= 90 and y <= 100 :
        print("Gracz znajduje sie w prawym gornym rogu")
    else :
        print("gracz znajduje sie poza plansza")

    q = input("czy chcesz kontynowac? tak/nie")

    if q == "nie"  :
        break
