print("SELAMAT DATANG DI KALKULATOR SEDERHANA Powered by Python")
print("")

def Menu_List() :
    print("")
    print("=== MENU UTAMA ===")
    print("")
    Menu = ["1. Kalkulator" , "2. Temperatur" , "3. Waktu","4. Jarak (BETA)","0. Versi Aplikasi","00. Keluar"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print(Menu[3])
    print(Menu[4])
    print(Menu[5])
    print("")
    Menu_Utama()

def Calculate_List():
    print("")
    print("=== MENU KALKULATOR ===")
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
    print("=== KALKULATOR SUHU ===")
    print("")
    Menu = ["1. Celcius / C","2. Reamur / R","3. Kelvin / K","4. Fahrenheit / F","0. Kembali ke Menu Utama"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print(Menu[3])
    print(Menu[4])
    print("")
    Temperatur()

def Waktu_List():
    print("")
    print("=== KALKULATOR WAKTU ===")
    print("")
    Menu = ["1. Detik","2. Menit","3. Jam","0. Kembali ke Menu Utama"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print(Menu[3])
    print("")
    Waktu()

def Jarak_List():
    print("")
    print("=== KALKULATOR JARAK BETA ===")
    print("")
    Menu = ["1. Kilometer / KM","2. Meter / M","3. Centimeter / CM","0. Kembali ke Menu Utama"]
    print(Menu[0])
    print(Menu[1])
    print(Menu[2])
    print('')
    Jarak()

def Menu_Utama():
    mainmenu = input("Silahkan tulis angka sesuai keterangan di atas! : ")
    if mainmenu == "1" :
        Calculate_List()
    else :
        if mainmenu == "2" :
            Temperatur_List()
        else :
            if mainmenu == "3" :
                Waktu_List()
            else :
                if mainmenu == "4" :
                    Jarak_List()
                else :
                    if mainmenu == "0" :
                        versi()
                    else :
                        if mainmenu == "00" :
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
        print (a, " Celcius = ", (float(a)*(4/5)) , " Reamur = " , (float(a)+273) , " Kelvin = " , ((float(a)*(9/5))+32) , " Fahrenheit" )
        print("")
        akhir()
    else :
        if suhu == "2" : 
            a = input("Masukkan Angka Suhunya! : ")
            print (a, " Reamur = ",(float(a)*(5/4))," Celcius = ",((float(a)*(5/4))+273)," Kelvin = ",((float(a)*(9/4))+32)," Fahrenheit")
            print("")
            akhir()
        else :
            if suhu == "3" :
                a = input("Masukkan Angka Suhunya! : ")
                print(a, " Kelvin = ",(273-(float(a)))," Celcius = ",((float(a)-273)*(4/5))," Reamur = ",((9/5)*((float(a)-273)+32))," Fahrenheit" )
                print("")
                akhir()
            else :
                if suhu == "4" :
                    a = input("Masukkan Angka Suhunya! : ")
                    print(a," Fahrenheit = ",((5/9)*(float(a)-32))," Celcius = ",((4/9)*(float(a)-43)), " Reamur = ",((5/9)*(float(a)-32)+273), " Kelvin" )
                    print("")
                    akhir()
                else :
                    if suhu == "0" :
                        Menu_List()
                    else :
                        print("Angka tidak terdefinisi. Mohon menulis angka yang sudah disediakan!")
                        print("")
                        Temperatur_List()

def Waktu() :
    print("")
    waktu = input("Silahkan tulis nomer sesuai dengan satuan waktu yang diketahui : ")
    print("")
    if waktu == "1" :
        a = input("Masukkan Waktu nya! : ")
        print(a, " Detik = ", (int(a)/60) , " Menit = ", (int(a)/3600), " Jam")
        print("")
        akhir()
    else :
        if waktu == "2" :
            a = input("Masukkan Waktu nya! : ")
            print(a, " Menit = ", (int(a)*60), " Detik = ", (int(a)/60), " Jam")
            print("")
            akhir()
        else :
            if waktu == "3" :
                a = input("Masukkan Waktu nya! : ")
                print(a, " Jam = ", (int(a)*3600), " Jam = ", (int(a)*60), " Menit")
                print("")
                akhir()
            else :
                if waktu == "0" :
                        Menu_List()
                else :
                    print("Angka tidak terdefinisi. Mohon menulis angka yang sudah disediakan!")
                    print("")
                    Waktu_List()

def Jarak() :
    a = ("Masukkan Jarak nya! : ")
    print("")
    MenuJarak = input("Silahkan tulis nomer sesuai dengan satuan jarak yang diketahui! : ")
    print("")
    if MenuJarak == "1" :
        jarak = float(input(a))
        print(("{:,}".format(jarak)) , " Kilometer ") 
        print(("{:,}".format(jarak*1000)), " Meter ")
        print(("{:,}".format(jarak*100000)), " Centimeter   ")
        print("")
        akhir()
    else :
        if MenuJarak == "2" :
            jarak = float(input(a))
            print(("{:,}".format(jarak/1000)), " Kilometer ")
            print(("{:,}".format(jarak)), " Meter ")
            print(("{:,}".format(jarak*100)), " Centimeter ")
            print("")
            akhir()
        else :
            if MenuJarak == "3" :
                jarak = float(input(a))
                print(("{:,}".format(jarak/100000)), " Kilometer  ")
                print(("{:,}".format(jarak/100)), " Meter  ")
                print(("{:,}".format(jarak)) , " Centimeter")
                print("")
                akhir()
            else :
                if MenuJarak == "0" :
                        Menu_List()
                else :
                    print("Angka tidak terdefinisi. Mohon menulis angka yang sudah disediakan!")
                    print("")
                    Jarak_List()

def penjumlahan() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (float(a) + float(b)))
    print("")
    akhir()

def pengurangan() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (float(a) - float(b)))
    print("")
    akhir()

def perkalian() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (float(a) * float(b)))
    print("")
    akhir()

def pembagian() :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    print("Hasil : ", (float(a) / float(b)))
    print("")
    akhir()

def akhir() :
    x = input("Kembali ke Menu Awal? Y/N : ")
    if x == "Y" or x == "y" or x == "Yes":
        print("")
        Menu_List()
    else:
        if x == "N" or x == "n" or x == "No" :
            exit
        else:
            print("Huruf tak terdefinisi! Mohon tulis Y atau N!")
            print("")
            akhir()

def Coming_Soon():
    print("")
    print("Fitur ini masih dalam tahap pengembangan! Nantikan di update Selanjutnya!")
    print("")
    input("Pencet Enter Untuk Kembali ke Menu Awal")
    print("")
    Menu_List()

def versi() :
    print("")
    print("KALKULATOR SEDERHANA")
    print("")
    print("Versi Aplikasi : v.1.2")
    print("Last Updated : 2021-09-30")
    print("Created by FakhriF")
    print("")
    print("Silahkan cek versi terbaru aplikasi ini di Github.com/Fakhri1/Random-Calculator-Python !")
    print("")
    print('Mengalami Kendala atau Masukan? Silahkan buat "Issue" di Github!')
    print("")
    akhir()
        
Menu_List()

exit = print("Program Terminated")
input("Tekan Enter!")