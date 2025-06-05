import os

ulang = 'Y'
while ulang.upper() == 'Y':
    os.system('cls')


    print()
    print()
    print()
    operator = input('Pilih yang ingin anda jumlahkan (+,-,*,/) :')

    num1 = (input('Masukkan Angka: '))
    num2 = (input('Masukkan Angka: '))

    if operator == '+':
      hasil = int(num1) + int(num2)
      print(f'Hasil:  {str(hasil)}' )

    elif operator == '-':
      hasil = int(num1) - int(num2)
      print(f'Hasil: {str(hasil)}')

    elif operator == '*':
      hasil = int(num1) * int(num2)
      print(f'Hasil: {str(hasil)}' )

    elif operator == '/':
       hasil = int(num1) / int(num2)
       print(f'Hasil:{str(hasil)}')
    else:
       print(f'{operator} Yang andaa Masukkan tidak Valid')
    ulang = input ('Apakah Masih Ada yang ingin anda jumlahkan Y/T: ')
print('Terima Kasih Telah Memakai Kalkulator Anomali Ini')
