import os.path

while True:
    if os.path.exists('dokument.txt') == True:
        dokument = open('dokument.txt', 'r')
        break
    else:
        dokument = open('dokument.txt', 'w')
        dokument.close()

emner = []
karakter = {}
karakterVerdi = {"A": 6,"B":5,"C":4,"D":3,"E":2,"F":1}
fagområde = {"informasjonsvitenskap": "INFO", "økonomi": "ECON", "geografi":"GEOV"}

for i in dokument:
    x = i.strip().split(" ")
    if len(x) == 2:
        karakter[x[0]] = x[1]
        emner.append(x[0])
    else:
        emner.append(x[0])

def leggTilEmne():
    nyttEmne = input("Nytt emne: ").upper()
    if nyttEmne in emner:
        print("Emnet finnes allerede.")
    else:
        emner.append(nyttEmne)

def finnEmner():
    lst = []
    print("Velg fag og/eller enmenivå(<Enter> for alle)")
    velgFag = input("- Fag: ").lower()
    velgNivå = input("- Nivå: ")

    if velgNivå != "" and velgFag == "":
        for i in sorted(emner):
            if velgNivå[0] == i[-3]:
                lst.append(i)

    elif velgNivå == "" and velgFag != "":
        for i in sorted(emner):
            if fagområde[velgFag] in i:
                lst.append(i)

    elif velgNivå != "" and velgFag != "":
        for i in sorted(emner):
            if velgNivå[0] == i[-3]:
                if fagområde[velgFag] in i:
                    lst.append(i)
    else:
        for i in sorted(emner):
            lst.append(i)

    return lst

def karakterSnitt():
    karakterliste = []
    emneListe = finnEmner()

    for i in emneListe:
        if i in karakter:
            karakterliste.append(karakter[i])

    def snittkalkulator():
        poeng = []
        for i in karakterliste:
            poeng.append(karakterVerdi[i])
        nummer = round(sum(poeng)/len(poeng))
        for i,j in karakterVerdi.items():
            if nummer == j:
                return i

    return snittkalkulator()

def leggTilKarakter():
    while True:
        gyldigeKarakterer = ["A","B","C","D","E","F"]
        velgEmne = input("Emne(0 for å gå tilbake til meny): ").upper()
        if velgEmne in emner:
            settKarakter = input("Karakter: ").upper()
            if settKarakter in gyldigeKarakterer:
                karakter[velgEmne] = settKarakter
            else:
                print("Ugyldig input! Bruk enkel bokstav mellom A og F")
                continue
        elif velgEmne == "0":
            break
        else:
            print("Emne finnes ikke. Prøv på nytt, eller trykk 0 for å gå tilbake til menyen: ")

while True:
    try:
        valg = int(input("Velg handling(0 for meny): "))
    except:
        print("Bruk tall som input!")
        valg = 0

    if valg == 0:
        print('--------------------')
        print('1 - Emneliste')
        print('2 - Legg til emne')
        print('3 - Sett karakter')
        print('4 - Karaktersnitt')
        print('5 - Avslutt')
        print('6 - Lagre')
        print('--------------------')
    elif valg == 1:
        for i in finnEmner():
            if i in karakter:
                print(i + " " + karakter[i])
            else:
                print(i)
    elif valg == 2:
        leggTilEmne()
    elif valg == 3:
        leggTilKarakter()
    elif valg == 4:
        print("Snitt: "+ karakterSnitt())
    elif valg == 5:
        break
    elif valg == 6:
        avslutt = input("Vil du lagre endringene? (j/n)").lower()
        if avslutt == "j":
            nyfil = open('nyfil.txt','w')
            for i in sorted(emner):
                if i in karakter:
                    nyfil.write(i + " " + karakter[i]+'\n')
                else:
                    nyfil.write(i+'\n')
            nyfil.close()
            dokument.close()
            os.remove('dokument.txt')
            os.rename('nyfil.txt', 'dokument.txt')
            break

        elif avslutt == "n":
            continue
        else:
            print('Ugyldig input! Skriv "j" for ja, eller "n" for nei')

    else:
        print("Ugyldig input! Velg et tall mellom 1-5 for handling, eller velg 0 for meny.")
