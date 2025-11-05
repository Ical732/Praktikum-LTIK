"""
Muhammad Faisal Anwar
NIM: 2512458
Kelas: 1A
"""

#Ganjil dan genap, positif dan negatif
x = int(input("Masukan sebuah angka: "))
if (x % 2 == 0):
    print(f"{x} merupakan angka genap")
    if (x > 0):
        print(f"{x} juga merupakan angka positif")
    elif (x < 0):
        print(f"{x} juga merupakan angka negatif")
    else:
        print(f"{x} tidak termasuk angka positif maupun negatif")
else:
    print(f"{x} merupakan angka ganjil")
    if (x > 0):
        print(f"{x} juga merupakan angka positif")
    else:
        print(f"{x} juga merupakan angka negatif")