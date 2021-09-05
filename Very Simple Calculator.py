print("Kalukulator Sangat Sederhana di Python")
print("")

def LIST() :
    Menu = ["1. Penjumlahan","2. Pengurangan","3. Perkalian","4. Pembagian","5. Versi Aplikasi","6. Keluar"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print(Menu[3])
    print(Menu[4])
    print(Menu[5])
    print("")
    menu()


def menu() :
    print("")
    operasi = input("Silahkan tulis angka sesuai keterangan di atas! : ")
    if operasi == "1":
        penjumlahan()
    else:
        if operasi == "2":
            pengurangan()
        else:
            if operasi == "3":
                perkalian()
            else:
                if operasi == "4":
                    pembagian()
                else:
                    if operasi == "5":
                        versi()
                    else:
                        if operasi == "6":
                            exit
                        else:
                            if operasi == "LIST":
                                LIST()
                            else:
                                print("Angka tidak terdefinisi. Mohon menulis angka yang sudah disediakan!")
                                print("Silahkan ketik - LIST - apabila Anda lupa dengan angkanya!")
                                print("")
                                menu()

def penjumlahan() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (int(a) + int(b)))
    print("")
    akhir()

def pengurangan() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (int(a) - int(b)))
    print("")
    akhir()

def perkalian() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (int(a) * int(b)))
    print("")
    akhir()

def pembagian() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (int(a) / int(b)))
    print("")
    akhir()

def akhir() :
    x = input("Kembali ke Menu Awal? Y/N : ")
    if x == "Y":
        print("")
        menu()
    else:
        if x == "N" :
            exit
        else:
            print("Huruf tak terdefinisi! Mohon tulis Y atau N!")
            print("")
            akhir()

def versi() :
    print("Versi Aplikasi : v.0.4")
    print("Last Updated : 2021-09-05")
    print("Created by FakhriF")
    print("")
    akhir()
        
LIST()

exit = print("Program Terminated")