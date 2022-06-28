def ocjena(bodovi):
    if bodovi < 50:
        return("Nedovoljan")
    elif bodovi < 65:
        return("Dovoljan")
    elif bodovi < 80:
        return("Dobar")
    elif bodovi < 90:
        return("Vrlodobar")
    else:
        return("Izvrstan")

from csv import reader
datoteka = open("rezultati.csv","r")

csv_reader =reader(datoteka)

rezultati = list(map(tuple,csv_reader))

novi_rezultati1 = []
for ime,prezime,bodovi in rezultati:
    novi_rezultati1.append((prezime, ime, bodovi))

novi_rezultati1.sort()
rezultati_ocjena = []

for osoba in novi_rezultati1:
    rijecnik = {}
    rijecnik["prezime"] = osoba[0]
    rijecnik["ime"] = osoba[1]
    rijecnik["ocjena"] = ocjena(int(osoba[2]))
    rezultati_ocjena.append(rijecnik)

rezultati_ocjena2 = []

for osoba in rezultati_ocjena:
    rezultati_ocjena2.append((osoba["prezime"], osoba["ime"], osoba["ocjena"]))

print(rezultati_ocjena2)
            
