metin = open('odev.txt')
yeni_metin = ""
for x in metin:
    satir=""
    y = list(x)
    for a in y:
        if a.isalpha():
            satir += a
            yeni_metin += a
    print(satir)
print(yeni_metin)

