for i in range(5):
    a=int(input("sayı giriniz:"))
    for j in range(2,a):
        if a%j==0:
            print(a,"asal değil")
            break
    else:
        print(a,"asal")
