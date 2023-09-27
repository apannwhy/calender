#program untuk melihat kalender
#import packages calendar
import calendar
import os
import time


year = int(input("Masukkan tahun : "))
month = int(input("Masukkan bulan (dalam angka) : "))
# print kalender
print(calendar.month(year, month))


keluar = input("Ingin keluar (y/n) : ")

	
# pilihan
while(keluar == "y"):
	time.sleep(1)
	os.system("exit")
else:
	print("system out")
	time.sleep(3)
