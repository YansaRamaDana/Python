import os

ulang = 'y'
while ulang.lower() == 'y':
    os.system('cls')

    print('+------------------------------------------------------+')
    print('|    SELAMAT DATANG DI PENJUMLAHAN NILAI PELAJARAN     |')
    print("+------------------------------------------------------+")

    def tentukan_grade (Grade):
        if Grade >= 90:
            return 'A'
        elif Grade >= 80:
            return 'B'
        elif Grade >= 70:
            return 'C'
        elif Grade >= 60:
            return 'D'
        else:
            return 'E'
    def main():
        try:
            banyak_pelajaran = int(input('Berapa Banyak Pelajaran yang Kamu Ikuti: '))
            if banyak_pelajaran <= 0:
                print('Pelajaran Harus Lebih Dari 0')
                return

            total_nilai = 0
            for i in range(1, banyak_pelajaran + 1):
                while True:
                    try: 
                        nilai = float(input(f'Masukan Nilai pelajaran Ke {i}: '))
                        break
                    except ValueError:
                        print('Angka Tidak Valid')
                total_nilai += nilai
            rata = total_nilai / banyak_pelajaran
            hasil = tentukan_grade(rata)
            print('+--------------HASIL-----------------+')
            print(f'Rata-Rata Nilai : {rata:.3f}')
            print(f'Nilai Grade: {hasil}')
            print('+------------------------------------+')
        except ValueError:
            print('Masukan Angka yang Valid')
    main()
    ulang = input('Apa Masih ada yang Ingin di Jumlahkan y/n: ')
    
