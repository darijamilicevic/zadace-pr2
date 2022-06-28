def parnii(a):
    broj = 2

    while broj < a:
        yield broj
        broj += 2
for i in parnii(25):
    print("Parni: ",i)

 
def neparnii(b):
    broj1 = 1

    while broj1 < b:
        yield broj1
        broj1 += 2
for j in neparnii(38):
    print ("Neparni: ",j)
