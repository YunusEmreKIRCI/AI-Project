def TemizVeri(s1, s2, s3):
    Birlesmis_deger = ""
    for a in s1:
        if not a.isdigit():
            
            Birlesmis_deger += a
            
    Birlesmis_deger += "-"

    for a in s2:
        if not a.isdigit():
            
            Birlesmis_deger += a
            
    Birlesmis_deger += "-"

    for a in s3:
        if not a.isdigit():
             
            Birlesmis_deger += a

    return Birlesmis_deger

print(TemizVeri("Ah5me4t", "M9eHm4eT", "Ha3K5a1n"))
