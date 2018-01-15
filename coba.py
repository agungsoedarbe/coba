list=[]
try:
	jumlah_nama = int(input("beberapa jumlah nama yang akan dimasukan: "))
	for i in range(jumlah_nama):
		nama = str (input("Nama ke %i: "%(i)))
		list.append(nama)
	pilihan = int(input("Panggil nama deng index ke: "))
	print(list[pilihan])
except ValueError:
	print("Masukan nilai angka bilangan bulat, bukan string")
except:
	print("Index data tersebut tidak tersedia")