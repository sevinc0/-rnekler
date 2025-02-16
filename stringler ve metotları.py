metin = input("Bir metin girin: ")
metin = metin.upper()

# Başındaki ve sonundaki boşlukları silme
metin = metin.strip()

# "a" harflerini "e" ile değiştirme
metin = metin.replace("a", "e")

# Boşluklara göre split edip kelimeleri liste halinde yazdırma
kelimeler = metin.split()

# Sonuçları ekrana yazdırma
print("İşlenmiş metin:", metin)
print("Kelime listesi:", kelimeler)
# Görev 2: Metni ters çevirme ve replace() ile değiştirme

metin = "Python programlama dili"

# Metni ters çevirme
terse_cevrilmis = metin[::-1]

# "programlama" yerine "kodlama" yazma
yeni_metin = metin.replace("programlama", "kodlama")

# Sonuçları ekrana yazdırma
print("Metin ters çevrilmiş haliyle:", terse_cevrilmis)
print("Yeni metin:", yeni_metin)
