import re

regex = "^A|d([a-z]+)?[0-5]([a-z]+)?\s([a-z]+)?m$"

while 1:
    unos = input("Unesite string:")
    rezultat = re.match(regex,unos)
    print(rezultat)
    if rezultat:
        break;
    else:
        print("Nema podudaranja!")
print("Postoji podudaranje!")
