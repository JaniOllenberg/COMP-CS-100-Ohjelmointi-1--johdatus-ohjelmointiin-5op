flights = {"AY437": "Oulu", "BA6033": "London", "JL048": "Tokyo", "SK707": "Stockholm", "BT302": "Riga"}
def main():
    hakemisto = {}
    print("Syötä sana ja sivunumero (lopeta tyhjällä rivillä):")
    while True:
        rivi = input()
        if rivi == "":
            break

        tiedot = rivi.split()
        hakusana = tiedot[0]
        sivunumero = int(tiedot[1])

        if hakusana not in hakemisto:
            hakemisto[hakusana] = []
        hakemisto[hakusana].append(sivunumero)
    print(hakemisto)
    for sana in sorted(hakemisto):
        print(sana, "", end="")
        for numero in sorted(hakemisto[sana]):
            print(numero, "", end="")
        print()


if __name__ == "__main__":
    main()