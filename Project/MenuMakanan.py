import os

ulang = 'Y'
while ulang.upper() == 'Y':
    os.system('cls')

    print()
    print()
    print()
    print('       SELAMAT DATANG DI SAMBAL BAKAR')
    print('============================================')
    print()
    print()
    print('              MENU PILIHAN')
    print()
    print(' --------------------------------------')
    print('|       Menu         |       Harga     |')
    print(' --------------------------------------')
    print('|  1.Sambak Ayam     |        50.000   |')
    print('|  2.Sambak Iga      |        100.000  |')
    print('|  3.Sambak Telor    |        70.000   |')
    print('|  4.Sambak Kulit    |        40.000   |')
    print('|  5.Sambak Kikil    |        55.000   |')
    print('|  6.Sambak Lele     |        70.000   |')
    print('|  7.Sambak Udang    |        40.000   |')
    print('|  8.Sambak Cumi     |        90.000   |')
    print('|  9.Sambak Paru     |        30.000   |')
    print('| 10.Sambak Belut    |        90.000   |')
    print(' --------------------------------------')

    pilihan = int(input('Masukkan menu pilihan anda: '))

    menu = {
        1: ("Sambak Ayam", 50000),
        2: ("Sambak Iga", 100000),
        3: ("Sambak Telor", 70000),
        4: ("Sambak Kulit", 40000),
        5: ("Sambak Kikil", 55000),
        6: ("Sambak Lele", 70000),
        7: ("Sambak Udang", 40000),
        8: ("Sambak Cumi", 90000),
        9: ("Sambak Paru", 30000),
        10: ("Sambak Belut", 90000),
    }

    if pilihan in menu:
        nama_menu, harga = menu[pilihan]
        print(f'{pilihan}. {nama_menu}')
        
        while True:
            try:
                jumlah = int(input('Masukkan jumlah pesanan anda: '))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0.")
                else:
                    break
            except ValueError:
                print("Masukkan angka yang valid.")

        total = jumlah * harga
        print(f'Total Harga: {total}')
        bayar = int(input('Uang yang Dibayar: '))
        kembalian = bayar - total
        print(f'Kembalian: {kembalian}')
    else:
        print('Pilihan tidak ada di menu')
    
    ulang = input('Apakah Masih ada yang Ingin Anda Pesan? (Y/T): ')

print('Terima Kasih Telah Mengunjungi Sambal Bakar')
print(' Semoga Harimu Menyenangkan Terima Kasih😊')
