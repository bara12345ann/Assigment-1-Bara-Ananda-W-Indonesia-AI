print("Program penghitung luas lingkaran ")
pi = 22/7
r = float(input("Masukkan nilai jari-jari : "))
luas = pi * (r ** 2)
format_luas = "{:.2f}".format(luas)
print("Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2".format(r, format_luas) )