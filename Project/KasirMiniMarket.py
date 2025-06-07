import os

def input_barang():
    while True:
        try:
            nama = input('Nama Barang: ')
            jumlah = int(input('Jumlah     : '))
            harga = int(input('Harga      : '))
            subtotal = jumlah * harga
            print(f'Subtotal: {subtotal}\n')
            return subtotal
        except ValueError:
            print('Input tidak valid! Masukkan angka yang benar untuk jumlah dan harga.\n')

os.system('cls')

print('        ======================================')
print('                    TOKO ANOMALI')
print('               Jl. Agal Laen no. 444')
print('          07-06-2025  14:23:15')
print('               No. Struk: 9213196308')
print('        ======================================')
print()
print('Item:')

# Gunakan list untuk menampung subtotal semua barang
daftar_subtotal = []

# Perulangan input barang
while True:
    subtotal = input_barang()
    daftar_subtotal.append(subtotal)
    
    lanjut = input('Tambah barang lagi? (y/n): ').lower()
    if lanjut != 'y':
        break
    print()

# Proses perhitungan
print('--------------------------------')
keseluruhan = sum(daftar_subtotal)
print(f'Subtotal : {keseluruhan}')
diskon = 2500
print(f'Diskon   : -{diskon}')
ppn = 2000
print(f'PPN (10%): +{ppn}')
print('--------------------------------')
Total_bayar = keseluruhan - diskon + ppn
print(f'Total Bayar               :  {Total_bayar}')
print()

# Input pembayaran
while True:
    try:
        bayar = int(input('Bayar   :   '))
        if bayar < Total_bayar:
            print('Uang tidak cukup. Masukkan jumlah yang cukup.\n')
            continue
        break
    except ValueError:
        print('Masukkan angka yang benar untuk pembayaran!\n')

total_semuanya = bayar - Total_bayar
print(f'Kembalian           :   {total_semuanya}')
print('===============================')
print('Terima kasih atas kunjunganya!')
print(f'Promo: Diskon 10% setiap Sabtu')
print('===============================')
