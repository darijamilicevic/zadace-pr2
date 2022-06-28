def str_rek(string):
    if len(string) == 0:
        return string
    else:
        prvo = string[0]
        ostala = string[1:]
        obrnuto = ostala[::-1]
        return(obrnuto + prvo)
#unos = str_rek("Darija")
#print(unos)


