#In this list, find the two entries that sum to 2020; what do you get if you multiply them together?
#Part two: What is the product of the three entries that sum to 2020?

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
    a_luvut = []
    b_luvut = []
    pari = []

    for luku in luvut:
        if luku < 1010:
            a_luvut.append(luku)
        else:
            b_luvut.append(luku)
    
    for luku1 in a_luvut:
        for luku2 in b_luvut:
                if luku1 + luku2 == 2020:
                    pari.append(luku1)
                    pari.append(luku2)
    return pari

def kerro(luvut:list):
    return luvut[0]*luvut[1]

luvut = lue_lista("list.txt")
print("luvut joiden summasta saadaan 2020:")
pari = etsi_luvut(luvut)
print(pari[0], "ja", pari[1])
print("Lukujen tulo:")
print(kerro(pari))