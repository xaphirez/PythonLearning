# Tuple: ordered, immutable, allows duplicate elements
myTuple = ("Max", 27 , "Boston")
print(myTuple)
print(type(myTuple))

#Membuat tuple dengan function tuple
myTuple1 = tuple(["Max", 22 , "California"])
print(myTuple1)
print(type(myTuple1))

#Mengambil item dari dalam tuple menggunakan index.
item = myTuple[0]
print(item)

#Tuple yg sudah dibuat tidak dapat dimodifikasi lagi

#Print item in tuple using for
for i in myTuple:
    print(i)

#Melakukan pengecekan item di dalam tuple
if "Max" in myTuple:
    print("Yes")
else:
    print("Nox")

print("------------------------------------------------------------------------------")

#Len = memeriksa banyak item di dalam tuple
myTuple2 = tuple(['a','p','p','l','e'])
print(myTuple2)
print("Jumlah item di dalam tuple = ", len(myTuple2))

#Count = memerika banyak item di dalam tuple secara spesifik
print("Banyak huruf 'p' di dalam tuple = " , myTuple2.count('p'))

#memeriksa index item di dalam tuple secara spesifik
print("index huruf 'l' di dalam tuple adalah : " , myTuple2.index('l'))

#Convert tuple menjadi list dan sebaliknya
myTuple3 = tuple(['a','p','p','l','e'])

my_list = list(myTuple3)
print(my_list)
print(type(my_list))

#Convert list menjadi tuple
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

print("------------------------------------------------------------------------------")

# Cara memanggil tuple menggunakan start dan last index
a = tuple([1,2,3,4,5,6,7,8,9,10])
b = a[2:5]
print(b)

print("------------------------------------------------------------------------------")

#Cara melakukan unpack tuple

myTuple4 = tuple(["Max", 22 , "California"])

name, age, city = myTuple4
print(name)
print(age)
print(city)

myTuple5 = tuple([1,2,3,4,5,6,7,8,9,10])

i1, *i2, i3 = myTuple5
print(i1)
print(i2) #wajib menggunakan simbol "*" untuk memastikan tuple dapat di unpacking semuanya
print(i3)


print("------------------------------------------------------------------------------")

#Membandingkan size tuple dan list menggunakan library sys

import sys
List = [0,1,2, "hello" , True]
tuple = (0,1,2, "hello" , True)
print(sys.getsizeof(List), "bytes")
print(sys.getsizeof(tuple), "bytes")