import matplotlib.pyplot as plt

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
    minimum = min(liczbyCalkowite)

    odwrotnaKolejnosc = liczbyCalkowite[::-1]


    print(f"Liczba wszystkich wartości: {iloscLiczb}")
    print(f"Suma: {suma}")
    print(f"Średnia: {srednia:.2f}")
    print(f"Liczba dodatnich: {dodatnie}")
    print(f"Liczba ujemnych: {ujemne}")
    print(f"Liczba zer: {zera}")
    print(f"Największa wartość: {maks}")
    print(f"Najmniejsza wartość: {minimum}")

    print(f"Odwrotna kolejność: {odwrotnaKolejnosc}")

#Wykresy
    plt.figure()
    plt.hist(liczbyCalkowite, bins=100, edgecolor="black")
    plt.title("Histogram wartości")
    plt.xlabel("Wartość")
    plt.ylabel("Częstość")
    plt.grid(axis="y", linestyle="--", alpha=0.6)


    plt.figure()
    kategorie = ["Dodatnie", "Ujemne", "Zera"]
    wartosci = [dodatnie, ujemne, zera]
    plt.title("Liczba dodatnich, ujemnych i zer")
    plt.ylabel("Liczba wystąpień")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.bar(kategorie, wartosci, color=["green", "red", "gray"])
    plt.title("Liczba dodatnich, ujemnych i zer")

    plt.figure()
    plt.plot(range(1, iloscLiczb + 1), liczbyCalkowite, marker="o")
    plt.title("Wykres kolejności liczb")
    plt.xlabel("Indeks")
    plt.ylabel("Wartość")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
