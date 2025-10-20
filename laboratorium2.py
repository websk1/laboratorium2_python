data = input("Podaj liczby całkowite oddzielone spacją: ")

if not data:
    print("Nie wprowadzono żadnych danych.")
else:
    liczbyCalkowite = [int(x) for x in data.split()]

    iloscLiczb = len(liczbyCalkowite)
    suma = sum(liczbyCalkowite)
    srednia = suma / iloscLiczb

    dodatnie = len([liczba for liczba in liczbyCalkowite if liczba > 0])
    ujemne = len([liczba for liczba in liczbyCalkowite if liczba < 0])
    zera = len([liczba for liczba in liczbyCalkowite if liczba == 0])


    maks = max(liczbyCalkowite)
    min_ = min(liczbyCalkowite)

    print(f"Liczba wszystkich wartości: {iloscLiczb}")
    print(f"Suma: {suma}")
    print(f"Średnia: {srednia:.2f}")
    print(f"Liczba dodatnich: {dodatnie}")
    print(f"Liczba ujemnych: {ujemne}")
    print(f"Liczba zer: {zera}")
    print(f"Największa wartość: {maks}")
    print(f"Najmniejsza wartość: {min_}")
