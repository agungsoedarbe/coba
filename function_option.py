#fungsi keliling lingkaran
def luas_lingkaran(r):
	luas=phi*(r**2)
	return luas
	
def keliling_lingkaran(r):
	keliling=2*phi*r
	return keliling

#fucation untuk pilihan
def option():
	print("Pilih salah satu dari tiga fungsionallitas berikut :")
	print("1. Mencari Luas Lingkaran")
	print("2. Mencari Keliling lingkran")
	print("3. Keluar dari Program")
	pilihan = int(input("Masukan pilihan anda :"))
	return pilihan
	
#main program
phi = 3.14
r = 8
pilihan = True
while(pilihan<3):
	pilihan = option()
	if(pilihan==1):
		l = luas_lingkaran(r)
		print("Luas Lingkaran : %.2f"%(l))
	elif(pilihan==2):
		k = keliling_lingkaran(r)
		print("Keliling Lingkaran : %.2f"%(k))