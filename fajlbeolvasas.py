
def beolvas(fajnev):
    """Beolvassuk az adatokat a fő fájlból"""
    my_file = open(fajnev,"r",encoding='utf8')
    fejlec=my_file.readline().strip()
    sorok= my_file.readlines()
    feldolgoz(sorok)
    my_file.close()
nevek=[]
nemek=[]
korok=[]

def feldolgoz(sorok):
    i=0
    while i<len(sorok):
        #print(sorok[i].strip())
        sor=sorok[i].strip().split(", ")
        #print(sorok)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        i+=1
    print(nevek)
    print(nemek)
    print(korok)
    print('Összesen ennyi adatsor van', len(nevek))

def atlagkor():
    i=0
    osszeletkor=0
    while i<len(korok):
        osszeletkor+=korok[i]
        i+=1
    atlag = osszeletkor/len(korok)
    print('Az átlag életkor: ',atlag)

def nok(nem):
    i=0
    index=-1
    valasztott_nemek_szama=0
    while i<len(nemek):
        if nemek[i]==nem:
            valasztott_nemek_szama+=1
            index=nemek[i]
        i+=1
        return index
    print('Összesen',valasztott_nemek_szama,' nő van a listában')

def lefitalabbno():
    i=0
    legfiatalabb=0

