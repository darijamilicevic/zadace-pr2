import re

regex = "^[a-z]+\.[a-z]+@fpmoz.sum.ba$"
regex1 = "^[a-z]{1}[a-z]+([0-9]*)?@sum.ba$"

while 1:
    unos = input("Unesite mail: ")
    unos1 = input("Unesite eduId: ")
    rezultat = re.match(regex,unos)
    rezultat1 = re.match(regex1,unos1)
    if rezultat and rezultat1:
        break;
    else:
        print("Nepravilan unos!")
print("Uspješno ste unijeli mail i eduId!")

              
