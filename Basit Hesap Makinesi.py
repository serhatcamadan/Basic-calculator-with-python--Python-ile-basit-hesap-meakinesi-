print("""***********************
-----BASİT HESAP MAKİNESİ-----
1. Toplamı işlemi

2. Çıkarma İşlemi

3. Çarpma işlemi

4. ölme işlemi

***********************
""")
a=float(input("Birinci sayıyı giriniz:"))
b=float(input("İkinci sayıyı giriniz:"))
islem=input("İşlemi giriniz:")

if islem == "1":
    print ("{} ile {} nin toplamı {} dır".format(a,b,a+b))

elif islem == "2":
    print ("{} ile {} nin farkı {} dır".format(a,b,a-b))

elif islem == "3":
    print ("{} ile {} nin çarpımı {} dır".format(a,b,a*b))

elif islem == "4":
    print ("{} ile {} nin bölümü {} dır".format(a,b,a/b))
else:
    print("Geçersiz işlem......")