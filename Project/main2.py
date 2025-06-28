import random
import time
import os
ulang = 'y'
while ulang.lower() == 'y':
    os.system('cls')

    print('+------------------------------------------------------------+')
    print('|                  CEK DOSA DAN PAHALA TEMAN                 |')
    print('+------------------------------------------------------------+')

    while True:
        def cek_pahala(nama):
            pahala_level = random.randint(1000, 1000000)
            

            print(f"{nama}...")
            print("Menghitung Pahala...")
            time.sleep(2)
            print(f"Pahala : {pahala_level}")
            return pahala_level
        nama_input = input('Masukakn Nama : ')
        pahala = cek_pahala(nama_input)
        lanjut = input('ingin cek dosa (y/n): ').lower()
        if lanjut != 'y':
            break

        def cek_dosa(nama):
            dosa_level = random.randint(1000, 1000000)

            print('Mengitung Dosa...')
            time.sleep(2)
            print(f'Dosa : {dosa_level}')
            return dosa_level
        dosa = cek_dosa(nama_input)
    
        break
    while True:
        lanjut = input('ingin melihat peluang masuk surga (y/n): ').lower()
        if lanjut != 'y':
            break
        hasil = pahala / dosa * 100
        print(f'Persentase masuk surga : {hasil:.2f}%')
        break
        
        
    ulang = input('Apa masih ada yang ingin di hitung y/n : ')