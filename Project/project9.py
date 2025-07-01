import os

menu = {
    'A1' : 'Soal Untuk A1',
    'A2' : 'Soal Untuk A2',
    'A3' : 'Soal Untuk A3',
    'A4' : 'Soal Untuk A4',
    'B1' : 'Soal Untuk B1',
    'B2' : 'Soal Untuk B2',
    'B3' : 'Soal Untuk B3',
    'B4' : 'Soal Untuk B4',
    'C1' : 'Soal Untuk C1',
    'C2' : 'Soal Untuk C2',
    'C3' : 'Soal Untuk C3',
    'C4' : 'Soal Untuk C4',
    'D1' : 'Soal Untuk D1',
    'D2' : 'Soal Untuk D2',
    'D3' : 'Soal Untuk D3',
    'D4' : 'Soal Untuk D4',
    'E1' : 'Soal Untuk E1',
    'E2' : 'Soal Untuk E2',
    'E3' : 'Soal Untuk E3',
    'E4' : 'Soal Untuk E4',
}





ulang = 'y'
while ulang.lower() == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('+----------------------------------------------+')
    print('|             PROGRAM CRYPTARITHM              |')
    print('+----------------------------------------------+')
    print('+------+  +------+  +------+  +------+  +------+')
    print('|  A4  |  |  B4  |  |  C4  |  |  D4  |  |  E4  |')
    print('+------+  +------+  +------+  +------+  +------+')
    print('|  A3  |  |  B3  |  |  C3  |  |  D3  |  |  E3  |')
    print('+------+  +------+  +------+  +------+  +------+')
    print('|  A2  |  |  B2  |  |  C2  |  |  D2  |  |  E2  |')
    print('+------+  +------+  +------+  +------+  +------+')
    print('|  A1  |  |  B1  |  |  C1  |  |  D1  |  |  E1  |')
    print('+------+  +------+  +------+  +------+  +------+')
    
    
    pilihan = input('Pilih kotak untuk melihat soal: ').upper()
    def tentukan_hasil(hasil):
        if hasil == 198:
            return 'Jawaban Benar'
        if hasil == 10652:
            return 'Jawaban Benar'
        if hasil == 1651757:
            return 'Jawaban Benar'
        if hasil == 166410:
            return 'Jawaban Benar'
        if hasil == 25952921:
            return 'Jawaban Benar'
        if hasil == 909416:
            return 'Jawaban Benar'
        if hasil == 476757:
            return 'Jawaban Benar'
        if hasil == 469134:
            return 'Jawaban Benar'
        if hasil == 273259:
            return 'Jawaban Benar'
        if hasil == 419963:
            return 'jawaban Benar'
        if hasil == 282768:
            return 'Jawaban Benar'
        if hasil == 68367:
            return 'Jawaban Benar'
        if hasil == 746969:
            return 'Jawaban Benar'
        if hasil == 36992:
            return 'Jawaban Benar'
        if hasil == 648608:
            return 'Jawaban Benar'
        if hasil == 7300184:
            return 'Jawaban Banar'
        if hasil == 107056:
            return 'Jawaban Benar'
        if hasil == 754620:
            return 'Jawaban Benar'
        if hasil == 930674:
            return 'Jawaban Benar'
        if hasil == 244468:
            return 'Jawaban Benar'
        else:
            return 'Jawaban Salah'
    if pilihan not in menu:
        print('Pilihan tidak ada di menu!')
        input('Tekan Enter untuk kembali ke menu...')
        continue


    if pilihan == 'A1':
        print(f'\nSoal {pilihan}')
        print('Percobaan Hanya 5 kali')
        print('+----------+')
        print('|   I I    |')
        print('|   I I    |')
        print('|   ----+  |')
        print('| H I U    |')
        print('+----------+')
        percobaan = 0
        while percobaan <5 :
            nilai_list = []
            jumlah = 2
            for i in range(jumlah):
                while True:
                    try:
                        nilai = int(input('  I I = '))
                        break
                    except ValueError:
                        print('Angka tidak valid')
            hasil_akhir = nilai + nilai
            akhir = tentukan_hasil(hasil_akhir)
            print(f'H I U = {hasil_akhir}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk mulai ulang...')
                break
        if akhir != 'Jawaban Benar':
            continue
    
        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah nya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------+')
                        print(f'|   {nilai}    |')
                        print(f'|   {nilai}    |')
                        print('|  ----+  |')
                        print(f'|  {hasil_akhir}    |')
                        print('+---------+')
                        langkah_langkah ='n'
            except ValueError:
                print('Hanya huruf')
                continue
            break
    
    if pilihan == 'A2':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|   SEND    |')
        print('|   + MORE  |')
        print('|   -----   |')
        print('|     MONEY |')
        print('+-----------+')
        percobaan = 0
        while percobaan <5 :
            while True:
                try:
                    send = int(input(' SEND = '))
                    more = int(input(' MORE = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_nyata = send + more
            akhir = tentukan_hasil(hasil_nyata)
            print(f'MONEY = {hasil_nyata}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan +=1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang...')
                break
        if akhir != 'Jawaban Benar':
            continue 

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah-langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+-----------+     +-----------------+')
                        print(f'| {send}      |     | S = 9     M = 1 |')
                        print(f'|+ {more}     |     | E = 5     O = 0 |')
                        print(f'| --------  |     | N = 6     R = 8 |')
                        print(f'|  {hasil_nyata}    |     | D = 7     Y = 2 |')
                        print('+-----------+     +-----------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya huruf')
                continue
            break  
    if pilihan == 'A3':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|   SYSTEM  |')
        print('|    ERROR  |')
        print('|   ----- + |')
        print('|   FAILURE |')
        print('+-----------+')
        percobaan = 0
        while percobaan <5 :
            while True:
                try:
                    system = int(input('SYSTEM = '))
                    error = int(input('ERROR  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_se = system + error
            akhir = tentukan_hasil(hasil_se)
            print(f'FAILURE = {hasil_se}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan +=1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah ='y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +-----------------------------+')
                        print(f'|   {system}      |        | S = 9     M = 5       A = 0 |')
                        print(f'|  {error}       |        | Y = 3     R = 1       I = 8 |')
                        print('|  -------- +   |        | T = 4     O = 0       L = 1 |')
                        print(f'| {hasil_se}       |        | E = 7     F = 6       U = 9 |')
                        print('+---------------+        +-----------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'A4':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|   POWER   |')
        print('|    SPEED  |')
        print('|   ----- + |')
        print('|  ENGINE   |')
        print('+-----------+')
        percobaan = 0
        while percobaan <5 :
            while True:
                try:
                    power = int(input('POWER = '))
                    speed = int(input('SPEED  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_ps = power + speed
            akhir = tentukan_hasil(hasil_ps)
            print(f'ENGINE = {hasil_ps}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan +=1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah ='y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +-----------------------------+')
                        print(f'|   {power}       |        | P = 8     R = 7       G = 2 |')
                        print(f'|  {speed}        |        | O = 1     S = 5       I = 9 |')
                        print('|  -------- +   |        | W = 4     D = 3             |')
                        print(f'| {hasil_ps}        |        | E = 0     N = 6             |')
                        print('+---------------+        +-----------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'B1':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|   GALAXY  |')
        print('|  UNIVERSE |')
        print('|   ----- + |')
        print('|   EXPLORE |')
        print('+-----------+')
        percobaan = 0
        while percobaan <5 :
            while True:
                try:
                    galaxy = int(input('GALAXY = '))
                    universe = int(input('UNIVERSE  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_gu = galaxy + universe
            akhir = tentukan_hasil(hasil_gu)
            print(f'FAILURE = {hasil_gu}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan +=1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah ='y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +-----------------------------------------+')
                        print(f'|   {galaxy}      |        | G = 1     Y = 7       V = 9        O = 0|')
                        print(f'|  {universe}     |        | A = 0     U = 2       E = 4       R = 6 |')
                        print('|  -------- +   |        | L = 3     N = 5       S = 1             |')
                        print(f'| {hasil_gu}      |        | X = 6     I = 8       P = 3             |')
                        print('+---------------+        +-----------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'B2':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  NUMBER   |')
        print('|   THEORY  |')
        print('|   ----- + |')
        print('|  ANSWER   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    number = int(input('NUMBER = '))
                    theory = int(input('THEORY = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_nt = number + theory
            akhir = tentukan_hasil(hasil_nt)
            print(f'ANSWER = {hasil_nt}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +---------------------------------------+')
                        print(f'|   {number}      |        | N = 1     T = 4     A = 0     W = 3 |')
                        print(f'|  {theory}       |        | U = 6     H = 9     S = 2     R = 5   |')
                        print('|  -------- +    |        | E = 8     O = 7     Y = 1             |')
                        print(f'| {hasil_nt}       |        |                                     |')
                        print('+---------------+        +---------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'B3':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  PLANET   |')
        print('|  + SYSTEM |')
        print('|  -------- |')
        print('|  ORBITAL  |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    planet = int(input('PLANET = '))
                    system = int(input('SYSTEM = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_ps = planet + system
            akhir = tentukan_hasil(hasil_ps)
            print(f'ORBITAL = {hasil_ps}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {planet}      |        | P = 3     S = 1     O = 4     A = 7 |')
                        print(f'|+  {system}      |        | L = 5     Y = 2     R = 6     T = 8 |')
                        print('|  -----------  |        | N = 6     M = 9     B = 3     I = 0 |')
                        print(f'|  {hasil_ps}      |        | E = 7                             |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break

    if pilihan == 'B4':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  CREATE   |')
        print('|  + DESIGN |')
        print('|  -------- |')
        print('|  PRODUCT  |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    create = int(input('CREATE = '))
                    design = int(input('DESIGN = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_cd = create + design
            akhir = tentukan_hasil(hasil_cd)
            print(f'PRODUCT = {hasil_cd}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +----------------------------------------+')
                        print(f'|   {create}      |        | C = 3     D = 1     P = 4     O = 6 |')
                        print(f'|+  {design}      |        | R = 7     E = 8     U = 9     T = 0 |')
                        print('|  -----------  |        | A = 5     S = 2     I = 6     G = 3 |')
                        print(f'|  {hasil_cd}       |        | N = 4                             |')
                        print('+---------------+        +----------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'C1':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  BINARY   |')
        print('|  + LOGIC  |')
        print('|  -------- |')
        print('|  RESULT   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    binary = int(input('BINARY = '))
                    logic = int(input('LOGIC  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_bl = binary + logic
            akhir = tentukan_hasil(hasil_bl)
            print(f'RESULT = {hasil_bl}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +---------------------------------------+')
                        print(f'|   {binary}       |        | B = 2     I = 5     R = 0     S = 6 |')
                        print(f'|+  {logic}         |        | N = 3     A = 4     Y = 7     L = 1 |')
                        print('|  -----------   |        | O = 9     G = 8     C = 2     T = 3 |')
                        print(f'|  {hasil_bl}         |        | E = 5     U = 6                   |')
                        print('+---------------+        +---------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'C2':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  DEVICE   |')
        print('|  + SMART  |')
        print('|  -------- |')
        print('|  SCREEN   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    device = int(input('DEVICE = '))
                    smart = int(input('SMART  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_ds = device + smart
            akhir = tentukan_hasil(hasil_ds)
            print(f'SCREEN = {hasil_ds}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {device}       |        | D = 3     E = 5     S = 6     M = 2 |')
                        print(f'|+  {smart}         |        | V = 7     I = 9     A = 0     R = 4 |')
                        print('|  -----------   |        | C = 1     T = 8     N = 6            |')
                        print(f'|  {hasil_ds}         |        |                                   |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'C3':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  SIGNAL   |')
        print('|  + WAVE   |')
        print('|  -------- |')
        print('|  SOUND    |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    signal = int(input('SIGNAL = '))
                    wave = int(input('WAVE   = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_sw = signal + wave
            akhir = tentukan_hasil(hasil_sw)
            print(f'SOUND = {hasil_sw}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {signal}       |        | S = 2     I = 7     G = 9     N = 6 |')
                        print(f'|+  {wave}          |        | A = 1     L = 0     W = 3     V = 5 |')
                        print('|  -----------   |        | E = 8     O = 4     U = 9     D = 6 |')
                        print(f'|  {hasil_sw}        |        |                                   |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'C4':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  ROBOT    |')
        print('|  + CODE   |')
        print('|  -------- |')
        print('|  FUTURE   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    robot = int(input('ROBOT = '))
                    code = int(input('CODE  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_rc = robot + code
            akhir = tentukan_hasil(hasil_rc)
            print(f'FUTURE = {hasil_rc}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {robot}       |        | R = 6     O = 1     B = 2     T = 3 |')
                        print(f'|+  {code}         |        | C = 7     D = 5     E = 4           |')
                        print('|  -----------   |        | F = 9     U = 8                      |')
                        print(f'|  {hasil_rc}         |        |                                   |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'D1':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  ENERGY   |')
        print('|  + LIGHT  |')
        print('|  -------- |')
        print('|  MOTION   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    energy = int(input('ENERGY = '))
                    light = int(input('LIGHT  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_el = energy + light
            akhir = tentukan_hasil(hasil_el)
            print(f'MOTION = {hasil_el}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {energy}       |        | E = 7     N = 2     R = 3     G = 6 |')
                        print(f'|+  {light}         |        | Y = 4     L = 1     I = 9     H = 0 |')
                        print('|  -----------   |        | T = 5     M = 8     O = 1           |')
                        print(f'|  {hasil_el}         |        |                                   |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    
    if pilihan == 'D2':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  BRAIN    |')
        print('|  + LOGIC  |')
        print('|  -------- |')
        print('|  THINK    |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    brain = int(input('BRAIN = '))
                    logic = int(input('LOGIC = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_bl = brain + logic
            akhir = tentukan_hasil(hasil_bl)
            print(f'THINK = {hasil_bl}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {brain}       |        | B = 1     R = 6     A = 3     I = 9 |')
                        print(f'|+  {logic}        |        | N = 4     L = 2     O = 0     G = 5 |')
                        print('|  -----------   |        | C = 8     T = 7     H = 2     K = 1 |')
                        print(f'|  {hasil_bl}         |        |                                   |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'D3':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  SIGNAL   |')
        print('|  + RADAR  |')
        print('|  -------- |')
        print('|  RANGE    |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    signal = int(input('SIGNAL = '))
                    radar = int(input('RADAR  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_sr = signal + radar
            akhir = tentukan_hasil(hasil_sr)
            print(f'RANGE = {hasil_sr}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {signal}       |        | S = 6     I = 1     G = 8     N = 2 |')
                        print(f'|+  {radar}         |        | A = 0     L = 5     R = 3     D = 4 |')
                        print('|  -----------   |        | E = 7                             |')
                        print(f'|  {hasil_sr}         |        |                                   |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'D4':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  CIRCUIT  |')
        print('|  + BOARD  |')
        print('|  -------- |')
        print('|  SYSTEM   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    circuit = int(input('CIRCUIT = '))
                    board = int(input('BOARD   = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_cb = circuit + board
            akhir = tentukan_hasil(hasil_cb)
            print(f'SYSTEM = {hasil_cb}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+----------------+        +----------------------------------------+')
                        print(f'|   {circuit}     |        | C = 7   I = 2   R = 5   U = 1   T = 6 |')
                        print(f'|+  {board}       |        | B = 4   O = 3   A = 0   D = 8         |')
                        print('|  ------------  |        | S = 9   Y = 1   E = 2   M = 7         |')
                        print(f'|  {hasil_cb}     |        |                                        |')
                        print('+----------------+        +----------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'E1':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  SPEED    |')
        print('|  + LIMIT  |')
        print('|  -------- |')
        print('|  SAFETY   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    speed = int(input('SPEED = '))
                    limit = int(input('LIMIT = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_sl = speed + limit
            akhir = tentukan_hasil(hasil_sl)
            print(f'SAFETY = {hasil_sl}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +--------------------------------------+')
                        print(f'|   {speed}      |        | S = 9     P = 4     E = 3     D = 6 |')
                        print(f'|+  {limit}      |        | L = 1     I = 2     M = 7     T = 0 |')
                        print('|  -----------  |        | A = 5     F = -     Y = 8           |')
                        print(f'|  {hasil_sl}      |        |                                   |')
                        print('+---------------+        +--------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break

    if pilihan == 'E2':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  SIGNAL   |')
        print('|  + POWER  |')
        print('|  -------- |')
        print('|  OUTPUT   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    signal = int(input('SIGNAL = '))
                    power = int(input('POWER  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_sp = signal + power
            akhir = tentukan_hasil(hasil_sp)
            print(f'OUTPUT = {hasil_sp}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +----------------------------------------+')
                        print(f'|   {signal}     |        | S = 7   I = 1   G = 6   N = 0   A = 9 |')
                        print(f'|+  {power}      |        | L = 4   P = 3   O = 8   W = 5   E = 2 |')
                        print('|  -----------  |        | R = 6   U = 0   T = 7                  |')
                        print(f'|  {hasil_sp}     |        |                                        |')
                        print('+---------------+        +----------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break

    if pilihan == 'E3':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  SENSOR   |')
        print('|  + ERROR  |')
        print('|  -------- |')
        print('|  STATUS   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    sensor = int(input('SENSOR = '))
                    error = int(input('ERROR  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_se = sensor + error
            akhir = tentukan_hasil(hasil_se)
            print(f'STATUS = {hasil_se}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +----------------------------------------+')
                        print(f'|   {sensor}     |        | S = 9   E = 1   N = 2   O = 3   R = 7 |')
                        print(f'|+  {error}      |        | T = 0   A = 6   U = 4                 |')
                        print('|  -----------  |        |                                        |')
                        print(f'|  {hasil_se}     |        |                                        |')
                        print('+---------------+        +----------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break
    if pilihan == 'E4':
        print(f'\n Soal {pilihan}')
        print('Percobaan hanya 5 kali')
        print('+-----------+')
        print('|  ENERGY   |')
        print('|  + LIGHT  |')
        print('|  -------- |')
        print('|  SOURCE   |')
        print('+-----------+')
        percobaan = 0
        while percobaan < 5:
            while True:
                try:
                    energy = int(input('ENERGY = '))
                    light = int(input('LIGHT  = '))
                    break
                except ValueError:
                    print('Angka Tidak Valid')
            hasil_el = energy + light
            akhir = tentukan_hasil(hasil_el)
            print(f'SOURCE = {hasil_el}')
            if akhir == 'Jawaban Benar':
                print(akhir)
                break
            else:
                print('Jawaban Salah, Coba lagi...')
                percobaan += 1
            if percobaan == 5 and akhir != 'Jawaban Benar':
                print('Terlalu banyak percobaan')
                input('Tekan enter untuk memulai ulang')
                break
        if akhir != 'Jawaban Benar':
            continue

        while True:
            try:
                langkah_langkah = 'y'
                while langkah_langkah == 'y':
                    langkah_langkah = input('Ingin melihat langkah langkahnya y/n: ').lower()
                    if langkah_langkah == 'y':
                        print('+---------------+        +----------------------------------------+')
                        print(f'|   {energy}     |        | E = 2   N = 0   R = 6   G = 7   Y = 3 |')
                        print(f'|+  {light}      |        | L = 4   I = 1   H = 9   T = 5         |')
                        print('|  -----------  |        | S = 8   O = 1   U = 0   C = 6         |')
                        print(f'|  {hasil_el}     |        |                                        |')
                        print('+---------------+        +----------------------------------------+')
                        langkah_langkah = 'n'
            except ValueError:
                print('Hanya Huruf')
                continue
            break




        ulang = input('Ingin mencoba lagi y/n : ').lower()
        if ulang == 'y':
            continue
        else:
            print('Terima kasih')
            break

    

    