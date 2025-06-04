import os

ulang = 'Y'
while ulang.upper() == 'Y':
    os.system('cls')


    print()
    print()
    print()
    print('SELAMAT DATANG DI KALKULATOR BMI SEDERHANA')
    print()
    berat = float(input('Masukkan Berat Anda (kg): '))
    tinggi = float(input('Masukkan Tinggi Anda (cm): '))

    tinggi = tinggi / 100
    bmi = (berat) / (tinggi**2)

    if bmi <= 16.9:
        print('Keterangan: Sangat Kurang Bobot')
        print(f'IMT: {round(bmi, 2)}')
    elif bmi <= 18.4:
        print('Keterangan: Kurang Bobot')
        print(f'IMT: {round(bmi, 2)}')
    elif bmi <= 24.9:
        print('Keterangan: Normal ')
        print(f'IMT: {round(bmi, 2)}')
    elif bmi <= 29.9:
        print('Keterangan: Kelebihan Bobot')
        print(f'IMT: {round(bmi, 2)}')
    elif bmi <= 34.9:
        print('Keterangan: Obesitas Kelas I ')
        print(f'IMT: {round(bmi, 2)}')
    elif bmi <= 39.9:
        print('Keterangan: Obesitas Kelas II ')
        print(f'IMT: {round(bmi, 2)}')
    else:
        print('Keterangan: Obesitas Kelas III')
    ulang = input('Apakah anda Masih Penasaran Y/T: ' )
print('Terima Kasih Telah Memakai Kalkulator Bmi Sederhana')