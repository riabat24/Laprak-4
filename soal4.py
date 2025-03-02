try: 
    sisi_1 = int(input("Masukan panjang sisi 1:")) 
    sisi_2 = int(input("Masukan panjang sisi 2:")) 
    sisi_3 = int(input("Masukan panjang sisi 3:")) 
    if sisi_1 == sisi_2 == sisi_3: 
        print("3 sisi sama") 
    elif sisi_1 == sisi_2 != sisi_3 or sisi_1 != sisi_2 == sisi_3 or sisi_1 == sisi_3 != sisi_2: 
        print("2 sisi sama") 
    else: 
        print("Tidak ada yang sama") 
except: 
    print("mohon di periksa kembali")