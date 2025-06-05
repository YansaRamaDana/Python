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
    print('|  10.Sambak Belut   |        90.000   |')
    print(' --------------------------------------')

    pilihan = int(input('Masukkan pilihan anda: '))

    if pilihan == 1:
        print('1.Sambak Ayam')
        harga = 50000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 2:
        print('1.Sambak Iga')
        harga = 100000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 3:
        print('1.Sambak Telor')
        harga = 70000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 4:
        print('1.Sambak kulit')
        harga = 40000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 5:
        print('1.Sambak Kikil')
        harga = 55000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 6:
        print('1.Sambak lele')
        harga = 70000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 7:
        print('1.Sambak Udang')
        harga = 40000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 8:
        print('1.Sambak Cumi')
        harga = 90000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 9:
        print('1.Sambak Paru')
        harga = 30000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    elif pilihan == 10:
        print('1.Sambak Belut')
        harga = 90000
        jumlah_pesanan = int(input('Masukkan jumlah pesanan anda: '))
        Total_harga = int(harga) * int(jumlah_pesanan)
        print('Total Harga: ' + str(Total_harga))
        uang_yang_dibayar = int(input('Uang yang Dibayar: '))
        kembalian = int(uang_yang_dibayar) - int(Total_harga)
        print('Kembalian: ' + str(kembalian))
    else :
        print('Pilihan tidak ada di menu')
    ulang = input('Apakah Masih ada yang Ingin Anda Pesan Y/T: ')
print('Terima Kasih Telah Mengunjungi Sambal Bakar')
print(' Semoga Harimu Menyenangkan Terima Kasih😊')
