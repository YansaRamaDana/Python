#Input
#nama = 'Yansa Rama Dana '   #tipe data - string
#usia = 18 #tipe-integer
#tinggi_badan = 179.5 #tipe float
#menyapa = 'Hello World!!'
#kata = ' tahun '
#kata_1 = 'dan tinggi badan saya: '
#punya_pacar = True

#Output
#print(menyapa)
#print(punya_pacar)
#print('usia saya adalah: ' + str(usia) + kata + kata_1 + str(tinggi_badan))

"""
# String 
first_name = 'Yansa Rama Dana'
food = 'Pizza'
email = 'yansa123@fake.com'

#print (f'Hello {first_name}')


# Integers
age = 25
quantity = 3
num_of_student = 30

#print (f'Umur saya  {age}')


# Float
price = 99.99
gpa = 7.90
distance = 5.5

#print (f'Menang undian $ {price}')
"""


# Boolean
#is_student = False

#print (f'Apakah kamu mahasiswa? {is_student}')
#if is_student:
    #print('Maka kamu mahasiswa')
#else :
   # print('Kamu bukan mahasiswa')




#input_nama = input('Halo nama kamu siapa? ')

#print(input_nama)


"""
#Menghapus atau menambah data
x = [1, 2, 3, 4, 5]
#del x [0]#Menghapus data
x.append(9)#Menambah data
print(x)
"""


#a = 90
#b = 10
#c = a + b

#print(c)

"""
a = input('Masukkan angka: ')
b = input('Masukkan angka: ')
hasil = int(a)+ int(b)

print('Hasil: ' + str(hasil))
"""

#a = input('Masukkan angka pertama: ')
#b = input('Masukkan angka kedua: ')
#c = int(a) + int(b)

#print(c)
#print ('Hasil nya adalah: ' + str(c))



#saldo_awal = input('Berapa saldo awal mu: ')
#deposit = input('Berapa mau deposit nya? ')

#hasilnya = int(saldo_awal) + int(deposit)

#print('Jumlah saldo awal ' + str(saldo_awal) + ' yang mau saya depositkan ' + str(deposit) + ' jumlahnya adalah: ' + str(hasilnya))



""""
nama_saya = 'Yansa Rama Dana'

print(nama_saya.find('R'))
print(nama_saya.find('Yansa'))
print(len(nama_saya))
print('r' in nama_saya)
print(nama_saya.upper())
print(nama_saya.capitalize())
print(nama_saya.count('n'))
print(nama_saya.replace('Yansa','4'))
#dan masih banyak lagi tipe data nya
"""


# == sama dengan
# > lebih dari
# < kurang dari
# != tidak sama dengan
# >= lebih dari sama dengan
# <= kurang dari sama dengan

#usia = 52

#if usia >= 5 and usia <= 10: 
  # print('balita')
#elif usia > 10 and usia <= 16:
    #print('anak anak')
#elif usia > 16 and usia <= 25:
    #print('remaja')
#elif usia > 25 and usia <= 35:
   # print('Dewasa')
#elif usia > 35 and usia <= 50:
  # print('Orang tua')
#elif usia > 50 and usia <= 80:
    #print('Kakek/Nenek')

#else: 
   # print('......pengecualian.......')


"""
pacar_saya = ['nelsa', 'angelica', 'nisa']

for pacar in pacar_saya:
    print(pacar)
"""

"""
names = ['John', 'Bob', 'Mosh', 'Sam', 'Marry']
names [0] = 'Jon'
print(names[0:3])
print(names)
"""


"""
awal = 1
while awal <= 10:
    print(awal)
    awal = awal + 1
"""

# == sama dengan
# > lebih dari
# < kurang dari
# != tidak sama dengan
# >= lebih dari sama dengan
# <= kurang dari sama dengan





"""
saldo_awal = 10000
deposit = input('Jumlah deposit: ')

saldo_total = int (saldo_awal) + int (deposit)
hutang = 50000

if saldo_total <= hutang:
    print('Tidak bisa bayar hutang')
elif saldo_total >= hutang:
    print('Bisa bayar hutang')
"""


"""""
name = input ('Nama kamu siapa? ')

print('Hello ' + name)
"""
""""
name = input ('Nama kamu siapa? ')
print('Nama kamu ' + name)

birth_year = input ('Tahun berapa kamu lahir?')
age = int (2025) - int (birth_year)

print ('Usia mu sekarang adalah ' + str(age))
"""


#Aritmatic Logic
"""
print(10 / 3)
x = 10
x = x + 3
x -= 3
"""


#x = (10 + 3) * 2
#print(x)
"""
number = 25
print(number > 10 or number < 30 )
"""

"""
number = 35

if number > 30: 
    print('panas banget')
    print('Butuh minum air dingin')
elif number > 20: # (20, 30)
    print('Hari yang menyenangkan')
elif number > 10: # (10, 20)
    print('Cuaca nya agak dingin')
else:
   print('Cuaca dingin')
print('Done')
"""
"""
weight =int (input ('Weight: '))
unit = input ('(K) or (L)bs: ')
if unit.upper() =='K':
    converted = weight / 0.45
    print('Weight in Lbs: ' + str (converted))
else:
    converted = weight * 0.45
    print('Weight in Kgs: ' + str(converted))
    """

"""
i = 1
while i <= 10:
    print(i * 'I Love U')
    i = i  + 1
"""


#numbers = [1, 2, 3, 4, 5] #bagian utama


#for item in numbers:
   # print(item)
#i = 0
#while i < len(numbers):
    #print(numbers[i])
    #i = i + 1
#numbers.insert(0, -1)
#numbers.remove(2)
#numbers.clear()
#print(numbers)
#print(1 in numbers) #true or false
#print(len(numbers))


"""
numbers =  range(5, 10, 2)
for number in range(5):
    print (number)
"""
"""
numbers = (1, 2, 3)
numbers.
"""
"""
def sapa(nama):
    print("Halo, " + nama)

sapa("Budi")
"""


"""
nama = input ('Siapa nama kamu? ')
usia = input ('Usia kamu berapa?')

usia = int(usia)
usia = usia + 1

print(f'Hello {nama}')
print(f'Usia kamu {str(usia)}')
"""

"""
x = 3.14
y = 4
z = 5

# result = round(x)
#result = abs(y)
#result = pow (4, 3)
result = min(x, y, z)

print(result)
"""

"""
import math

x = 9.9

#print (math.pi)
#print(math.e)
#result = math.sqrt(x)
#ressult = math.ceil(x)
result = math.floor(x)



print(result)

"""

"""
import math

radius = float(input('Enter the radius of circle'))

circumference = 2 * math.pi * radius

print(f'The circumference is: {circumference}')
"""

"""
import math

radius =  float(input('Enter the radius of circle'))

area = math.pi * pow(radius, 2)

print(f'The area of the circle is: {round(area, 2)}cm2')
"""
"""
usia = int (input('Masukkan usia anda: '))

if usia <= 18:
    print('Masih Remaja')
    """

"""
response = input('Apakah kamu suka makanan? (Y/T) ')

if response == 'Y':
  print ('Kamu sehat!')
elif response == 'T':
  print ('Kamu cacingan')
else :
  print('Kamu Anomali')
  """

#Boolean
"""
online = False

if online :
    print('Anda Online')
else :
    print('Anda offline')
    """
"""
# Python weight converted

weight = float(input('Masukkan Beratmu: '))
unit = input('Kilograms or Pounds? (K or L): ')

if unit =='K':
    wight = weight* 2.205
    unit = 'Lbs.'
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kgs.'
else:
    print(f'{unit} tidak valid')

print(f'Berat Kamu Adalah: {weight} {unit}')
"""

"""
unit = input('Is thhis temperaturs in Celsius  or Fahrenheit (C/F): ')
temp = float (input('Enter The Temperatur: '))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'The Temperatur in Fahrenheit is: {temp}F')
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9)
    print(f'The Temperatur in Celcius is: {temp}C')
else:
    print(f'{unit} is an invalid unit of measurement')
    """

"""

temp = True
is_raining = 20

if temp > 35 or temp < 0 or is_raining:
    print('The outdor event is cancelled')
else:
    print('The Outdoor event is still sheduled')

"""

"""
temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print('It is HOT outside ')
    print(' it is SUNNY')
elif temp <= 0 and is_sunny:
    print('it is COLD outside')
    print('it is SUNNY')
elif 28 > temp > 0 and is_sunny:
    print('it is WARM outside')
    print('It is SUNNY')
if temp >= 28 and not is_sunny:
    print('It is HOT outside ')
    print(' it is CLOUDY')
elif temp <= 0 and not is_sunny:
    print('it is COLD outside')
    print('it is CLOUDY')
elif 28 > temp > 0 and not is_sunny:
    print('it is WARM outside')
    print('It is CLOUDY')
    """

"""
num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = 'admin'

#print('Positive' if num < 6 else 'Negative')
#result = 'EVEN' if  num % 2 == 0 else 'ODD'
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = 'Adult' if age >= 18 else 'Child'
#weather = 'Hot' if temperature > 20 else 'COLD'
acces_level = 'Full Access' if user_role  == 'admin' else 'Limitid Access'
print (acces_level)
"""

"""
import os

os.system('cls')

#nama = input ('Masukkan full nama anda: ')
phone_number = input ('Masukkan nomor telepon: ')

#result = len(nama) # Untuk mengitung ada berapa alfabet di dalam nama
#result = nama.find('a') # untuk mendeteksi huruf di dalam nama
#result = nama.rfind('z')
#result = nama.capitalize()
#result = nama.upper() # Huruf besar semua
#result = nama.lower() # Huruf kecil semua
#result = nama.isdigit() # hanya untuk angka
#result = nama.isalpha() # hanya untuk huruf
#phone_number.count('-') # membaca string
#result = phone_number.replace('-', ' ')

print(result)
"""

"""
import os
os.system('cls')

username = input('Masukkan nama: ')


if len(username) > 12:
    print('Nama terdiri dari 12 karakter')
elif not username.find (' ') == -1:
    print('Nama pengguna anda tidak dapat menggunakan spasi')
elif not username.isalpha ():
    print('Nama pengguna anda tidak dapat berisi angka')
else: 
    print(f'Welcome {username}')
    """

"""
import os
os.system('cls')

credit_number = '1234-5678-9012-3456'

#print(credit_number[0])
#print(credit_number[:4])
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-1])
#print(credit_number[::2])
#angka_terakhir = credit_number[-4:]
angka_terakhir = credit_number[::-1]
print(f'XXXX-XXXX-XXXX-{angka_terakhir}')
print(credit_number)
"""

"""
import os
os.system('cls')

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f'Price 1 is {price1:,.3f}')
print(f'Price 2 is {price2:,.3f}')
print(f'Price 3 is {price3:,.3f}')
"""

"""
import os
os.system('cls')

nama = input ('Masukkan nama anda: ')

while nama == '':
    print('Anda tidak memasukkan nama anda')
    nama = input('Masukkan nama anda: ')
print(f'Hello {nama}')
"""

"""
import os
os.system('cls')

usia = int(input('Masukkan usia anda: '))

while usia < 0:
    print('Usia tidak bisa negative')
    usia = int(input('Masukkan usia anda: '))

print(f'Umur anda sudah {usia} tahun')
"""

"""
import os
os.system('cls')

makanan = input('Masukkan makanan yang anda sukai (q to quit): ')

while not makanan == 'quit':
   print(f'Anda menyukai {makanan}')
   makanan = input('Masukkan makanan lain yang anda sukai (q to quit): ')

print('selesai')

"""

"""
import os
os.system('cls')

num =  int(input('Masukkan a # diantara 1 - 10: '))

while num < 1 or num > 100:
    print(f'{num} ini tidak sah')
    num = int(input('Masukkan a # diantara 1 - 10: '))

print(f'Nomor kamu adalah {num}')
"""