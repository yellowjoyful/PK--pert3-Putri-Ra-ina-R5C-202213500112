bulan_hari = {
    1: 31,
    2: 29,
    3: 31, 
    4: 30, 
    5: 31, 
    6: 30, 
    7: 31, 
    8: 31,  
    9: 30, 
    10: 31, 
    11: 30, 
    12: 31 
}

def tampilkan_jumlah_hari():
    while True:
        try:
            bulan = int(input("Masukkan bulan (1-12): "))
            if bulan < 1 or bulan > 12:
                print("Bulan yang diinputkan tidak valid. Silakan coba lagi.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

   
    jumlah_hari = bulan_hari[bulan]
    print(f"Jumlah hari: {jumlah_hari}")

tampilkan_jumlah_hari()