mport os
os.system('cls')

def login():
    username = 'codingansempak@gmail.com'
    password = 'Yansa12399'
    
    # -------------------
    # Pengecekan Username
    # -------------------
    percobaan_username = 0
    while percobaan_username < 6:
        masuk_user = input('Masukkan Username/Gmail: ')
        if masuk_user == username:
            print('Username Benar')
            break
        else:
            print('Username Salah')
            percobaan_username += 1

        if percobaan_username == 6:
            print('Terlalu banyak percobaan. Akun ditangguhkan.')
            return  # keluar dari fungsi login

    # -------------------
    # Pengecekan Password
    # -------------------
    percobaan_password = 0
    while percobaan_password < 3:
        masuk_pass = input('Masukkan Password: ')
        if masuk_pass == password:
            print('Login Berhasil')
            return
        else:
            print('Password Salah')
            percobaan_password += 1

        if percobaan_password == 3:
            print('Terlalu banyak percobaan. Akun ditangguhkan.')

login()
