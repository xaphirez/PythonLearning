# List: ordered, mutable, allows duplicate elements

myList = ["banana", "cherry", "apple"]
print(myList)

# Check isi dalam list menggunakan if
if "lemon" in myList:
    print("Yes")
else:
    print("No")

# Append = memasukkan item ke dalam list
myList.append("Lemon")
print(myList)

#Insert = memasukkan item ke dalam list sesuai index yg diharapkan
myList.insert(2, "Blueberry")
print(myList)

# Pop = mengambil item paling terakhir di dalam list dan membuangnya
item1 = myList.pop()
print(item1)
print(myList)

#Remove = Menghapus spesifik item dari dalam list
item2 = myList.remove("banana")
print(myList)

#Clear untuk menghapus semua item dari dalam list
item3 = myList.clear()
print(myList)

# Reverse = membalikan urutan list
item4 = myList.reverse()
print(myList)

# Sort = mengurutkan item dari list secara ascending
myList2 = [3,2,6,7,8,3,-2,13,-5]

new_List = sorted(myList2)
print(myList2)
print(new_List)
