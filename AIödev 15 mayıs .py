metin = open('odev.txt')
yeni_metin = ""
for x in metin:
    y = list(x)
    for a in y:
        if a.isalpha():
            yeni_metin += a

print(yeni_metin)

