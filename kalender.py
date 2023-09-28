# program untuk melihat kalender
# import packages
import calendar
import sys
import time

# perulangan pilihan
x = "curut"

while x == "curut":
    year = int(input("Masukkan tahun : "))
    month = int(input("Masukkan bulan (dalam angka) : "))
    # print kalender
    print(calendar.month(year, month))

    # input untuk pilihan
    keluar = input("apakah anda ingin keluar (y/n) => ")
    if keluar == "y":
        time.sleep(2)
        sys.exit()
