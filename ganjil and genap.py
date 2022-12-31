'''Buatlah program yang dapat menerima 2 input angka dengan 
ketentuan sebagai 
- Jika penjumlahan kedua nilai adalah genap, maka 
tambahkan angka 1
- Jika penjumlahan kedua adalah ganjil, maka jumlah di tambah 2 '''

a = int(input("angka pertama :"))
b = int(input("angka kedua :"))

if a and b %2 ==0:
	genap = a+b +1
	print(genap)
	
	
elif a and b %2 != 0:
	ganjil = a + b +2
	print(ganjil)
	

