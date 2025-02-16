yas = 25  

print(yas > 18 and yas < 65)  


print(yas < 18 or yas > 65) 


print(not (yas == 25))  

sayi = int(input("Bir sayı girin: ")) 

if sayi % 2 == 0 and sayi > 0:
    print(True)  
else:
    print(False)  

yas = int(input("Yaşınızı girin: "))  
ehliyet = input("Ehliyetiniz var mı? (Evet/Hayır): ").lower() 

if yas > 18 and ehliyet == "evet":
    print("Araba kullanabilirsiniz")
else:
    print("Araba kullanamazsınız")
