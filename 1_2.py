#Part two: What is the product of the three entries multiplyed that sum to 2020?

def lue_lista(tiedosto: str):
    from string import punctuation
    luvut = []

    with open (tiedosto) as lista:
        sisalto = lista.read()
        sisalto = sisalto.split("\n")
        mappaus = map(int, sisalto)
        luvut = list(mappaus)

    return luvut

def etsi_luvut(luvut:list):
    tripla = []

    for luku1 in luvut:
        for luku2 in luvut:
            for luku3 in luvut:
                if luku1+luku2+luku3 == 2020:
                    tripla.append(luku1)
                    tripla.append(luku2)
                    tripla.append(luku3)

    return tripla

def kerro(luvut:list):
    return luvut[0]*luvut[1]*luvut[2]

luvut = lue_lista("list.txt")
print("3 lukua, joiden summasta saadaan 2020:")
tripla = etsi_luvut(luvut)
print(tripla[0], tripla[1], "ja", tripla[2])
print("Lukujen tulo:")
print(kerro(tripla))