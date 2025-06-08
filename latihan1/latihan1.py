# =============================================
# 📌 BELAJAR PYTHON DASAR UNTUK PEMULA
# =============================================
# CATATAN : Agar tidak TerRun/Di jalankan semua tambah kan komentar setiap 1 materi. Atas """ ,  Bawah """ 
# 1. Variabel dan Tipe Data
# 2. Output dan String Manipulation
# 3. List dan Tuple
# 4. Operator Aritmatika
# 5. Kondisional (if-elif-else)
# 6. Perulangan: For dan While
# 7. Input dari User
# 8. Function (Fungsi)
# 9. Menggunakan Module
# 10. Mini Project : Konversi Berat
# 11. Mini Project : Kalkulator Majemuk
# 12. Mini Project : Countdown Tahun Baru
# 13. Perulangan dan Break
# 14. Mini Project : Time Mundur Detik


# ----------------------------
# 1. VARIABEL DAN TIPE DATA
# ----------------------------
nama = 'Selamet Kopling'   # String
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
print(nama.find('Optimus'))
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
import os
os.system('cls')

def sapa(nama): # nama opsional yahhh 
    print(f'Halo {nama}')
    print('Semangat yah')
    print('Kamu Pasti bisa')

sapa('Bagas Titik Kumpull')
sapa('Daffa Martabak')
sapa('Agung Buzcut')

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

# ----------------------------
# 11. MINI PROJECT: KALKULATOR MAJEMUK
# ----------------------------

# Kalkulator majemuk python

prinsip = 0
tingkat = 0
waktu = 0

while True:
    prinsip = float(input('Masukkan Jumlah Pokok:  '))
    if prinsip < 0:
        print('Prinsip tidak bisa kurang dari nol ')
    else:
        break
while True:
    tingkat = float(input('Masukkan tingkat bunga:  '))
    if tingkat < 0:
        print('Tingkat bunga tidak bisa kurang dari nol ')
    else:
        break
while True:
    waktu = int(input('Masukkan waktu tahun:  '))
    if waktu < 0:
        print('Waktu tidak bisa kurang dari nol ')
    else:
        break

total = prinsip * pow((1 + tingkat / 100), waktu)
print(f'Keseimbangan setelahnya {waktu} tahun/s: ${total:.2f}')


# ----------------------------
# 12. MINI PROJECT: COUNTDOWN TAHUN BARU
# ----------------------------

for x in reversed(range(1, 10)): # Reversed dari bawah ke atas # Range dari atas ke bawah
    print(x)
print('HAPPY NEW YEAR!!')


# ----------------------------
# 13. PERULANGAN DAN BREAK
# ----------------------------

import os
os.system('cls')

# kartu_kredit = '12434-5678-9012-3456'
# for x in kartu_kredit:
    #print(x)

for x in range(1, 21):
    if x == 13: # Untuk skip
        break
    else:
        print(x)


# ----------------------------
# 14. MINI PROJECT: TIMER MUNDUR DETIK
# ----------------------------

import time

# Detik Waktu
time_saya = int(input('Masukkan waktu dalam detik: '))

for  x in range(time_saya, 0, -1):
    detik = x % 60
    print(f'00:00:0{detik}')
    time.sleep(1)

print('TITID BANGAU')


