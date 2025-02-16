meyveler = ["elma", "armut", "çilek", "kiraz"]  


meyve = input("Bir meyve ismi girin: ")  

if meyve in meyveler:
    print(f"{meyve.capitalize()} listede var.") 
else:
    print(f"{meyve.capitalize()} listede yok.") 

parola = "PyThOn123" 

karakter = input("Bir karakter girin: ")

if karakter not in parola:
    print("Parolada bu karakter yok.")
else:
    print("Parolada bu karakter var.")
