def indeks():
    boy=int(input("Boyunuzu giriniz"))
    kilo=int(input("Kilonuzu giriniz"))
    indeks= kilo / (boy/100)**2
    print("indeksiniz",indeks)
    if indeks<18:
        print("Zayif")
        if indeks>=18< indeks< 25:
            print("Normal")
            if indeks>= 26 < indeks < 30:
                print(" kilolu")
                if indeks>30<indeks<35:
                    print("obez")
indeks()