print("SELAMAT DATANG DI KALKULATOR SEDERHANA Powered by Python")
print("")

def Menu_List() :
    print("")
    print("MENU UTAMA")
    print("")
    Menu = ["1. Kalkulator" , "2. Temperatur" , "3. Versi Aplikasi","4. Keluar"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print(Menu[3])
    print("")
    Menu_Utama()

def Calculate_List():
    print("")
    print("MENU KALKULATOR")
    print("")
    Menu = ["1. Penjumlahan","2. Pengurangan","3. Perkalian","4. Pembagian","0. Kembali Ke Menu Utama"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print(Menu[3])
    print(Menu[4])
    print("")
    Menu_Kalkulator()

def Temperatur_List():
    print("")
    print("KALKULATOR SUHU")
    print("")
    Menu = ["1. Celcius / C","2. Reamur / R","3. Kelvin / K","4. Fahrenheit / F","0. Kembali ke Menu Utama"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print(Menu[3])
    print(Menu[4])
    print("")
    Temperatur()

def Menu_Utama():
    mainmenu = input("Silahkan tulis angka sesuai keterangan di atas! : ")
    if mainmenu == "1" :
        Calculate_List()
    else :
        if mainmenu == "2" :
            Temperatur_List()
        else :
            if mainmenu == "3" :
                versi()
            else :
                if mainmenu == "4" :
                    exit
                else : 
                    print("Angka tidak terdefinisi. Mohon menulis angka yang sudah disediakan!")
                    Menu_List()

def Menu_Kalkulator() :
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
                    if operasi == "0":
                        Menu_List
                    else:
                        print("Angka tidak terdefinisi. Mohon menulis angka yang sudah disediakan!")
                        print("")
                        Calculate_List()

def Temperatur() :
    print("")
    suhu = input("Silahkan tulis nomer sesuai dengan jenis suhu yang diketahui : ")
    print("")
    if suhu == "1" :
        a = input("Masukkan Angka Suhunya! : ")
        print (a, " Celcius = ", (int(a)*(4/5)) , " Reamur = " , (int(a)+273) , " Kelvin = " , ((int(a)*(9/5))+32) , " Fahrenheit" )
        print("")
        akhir()
    else :
        if suhu == "2" :
            a = input("Masukkan Angka Suhunya! : ")
            print (a, " Reamur = ",(int(a)*(5/4))," Celcius = ",((int(a)*(5/4))+273)," Kelvin = ",((int(a)*(9/4))+32)," Fahrenheit")
            print("")
            akhir()
        else :
            if suhu == "3" :
                a = input("Masukkan Angka Suhunya! : ")
                print(a, " Kelvin = ",(273-(int(a)))," Celcius = ",((int(a)-273)*(4/5))," Reamur = ",((9/5)*((int(a)-273)+32))," Fahrenheit" )
                print("")
                akhir()
            else :
                if suhu == "4" :
                    a = input("Masukkan Angka Suhunya! : ")
                    print(a," Fahrenheit = ",((5/9)*(int(a)-32))," Celcius = ",((4/9)*(int(a)-43)), " Reamur = ",((5/9)*(int(a)-32)+273), " Kelvin" )
                    print("")
                    akhir()
                else :
                    if suhu == "0" :
                        Menu_List()
                    else :
                        print("Angka tidak terdefinisi. Mohon menulis angka yang sudah disediakan!")
                        print("")
                        Temperatur_List()


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
        Menu_List()
    else:
        if x == "N" :
            exit
        else:
            print("Huruf tak terdefinisi! Mohon tulis Y atau N!")
            print("")
            akhir()

def versi() :
    print("Versi Aplikasi : v.0.6")
    print("Last Updated : 2021-09-05")
    print("Created by FakhriF")
    print("")
    print("Silahkan cek versi terbaru aplikasi ini di Github.com/Fakhri1/Random-Calculator-Python !")
    print("")
    akhir()
        
Menu_List()

exit = print("Program Terminated")