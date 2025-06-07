# =============================================
# 📌 BELAJAR PYTHON DASAR UNTUK PEMULA
# =============================================
# 1. Variabel dan Tipe Data
# 2. Output dan String Manipulation
# 3. List dan Tuple
# 4. Operator Aritmatika
# 5. Kondisional (if-elif-else)
# 6. Perulangan: For dan While
# 7. Input dari User
# 8. Function (Fungsi)
# 9. Menggunakan Module
# 10. Mini Project: Konversi Berat


# ----------------------------
# 1. VARIABEL DAN TIPE DATA
# ----------------------------
nama = 'Yansa Rama Dana'   # String
usia = 18                  # Integer
tinggi_badan = 168.5       # Float
punya_pacar = True         # Boolean

# ----------------------------
# 2. OUTPUT DAN STRING MANIPULATION
# ----------------------------
menyapa = 'Hello World!!'
kata = ' tahun '
kata_1 = 'dan tinggi badan saya: '
print(menyapa)
print(punya_pacar)
print('Usia saya adalah: ' + str(usia) + kata + kata_1 + str(tinggi_badan))

# String Methods
print(nama.find('R'))
print(nama.find('Yansa'))
print(len(nama))
print('r' in nama)
print(nama.upper())
print(nama.capitalize())
print(nama.count('n'))
print(nama.replace('Yansa','4'))

# ----------------------------
# 3. TIPE DATA LAINNYA: LIST, TUPLE
# ----------------------------
pacar_saya = ['nelsa', 'angelica', 'bianca']
for pacar in pacar_saya:
    print(pacar)

names = ['John', 'Bob', 'Mosh', 'Sam', 'Marry']
names[0] = 'Jon'
print(names[0:3])
print(names)

# ----------------------------
# 4. OPERATOR ARITMATIKA
# ----------------------------
a = 90
b = 10
c = a + b
print(c)

# ----------------------------
# 5. KONDISIONAL (IF-ELIF-ELSE)
# ----------------------------
usia = 52
if usia >= 5 and usia <= 10: 
    print('Balita')
elif usia > 10 and usia <= 16:
    print('Anak-anak')
elif usia > 16 and usia <= 25:
    print('Remaja')
elif usia > 25 and usia <= 35:
    print('Dewasa')
elif usia > 35 and usia <= 50:
    print('Orang Tua')
elif usia > 50 and usia <= 80:
    print('Kakek/Nenek')
else:
    print('Pengecualian')

# ----------------------------
# 6. PERULANGAN: FOR DAN WHILE
# ----------------------------
awal = 1
while awal <= 10:
    print(awal)
    awal += 1

for number in range(5):
    print(number)

# ----------------------------
# 7. INPUT DARI USER
# ----------------------------
nama = input('Siapa nama kamu? ')
usiamu = int(input('Berapa usiamu sekarang? '))
usiamu += 1
print(f'Halo {nama}, tahun depan kamu akan berusia {usiamu}')

# ----------------------------
# 8. FUNCTION (FUNGSI)
# ----------------------------
def sapa(nama):
    print("Halo, " + nama)

sapa("Budi")

# ----------------------------
# 9. MENGGUNAKAN MODULE
# ----------------------------
import math
x = 9.9
print(math.floor(x))

radius = float(input('Masukkan radius lingkaran: '))
circumference = 2 * math.pi * radius
print(f'Keliling lingkaran: {circumference}')

# ----------------------------
# 10. MINI PROJECT: KONVERSI BERAT
# ----------------------------
weight = float(input('Masukkan beratmu: '))
unit = input('Kilograms atau Pounds? (K/L): ')

if unit.upper() == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
elif unit.upper() == 'L':
    weight = weight / 2.205
    unit = 'Kgs.'
else:
    print(f'{unit} tidak valid')

print(f'Berat kamu adalah: {weight} {unit}')
