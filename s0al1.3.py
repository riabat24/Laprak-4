tulis_a= input("Masukkan bilangan pertama: ")  
tulis_b = input("Masukkan bilangan kedua: ") 
tulis_c = input("Masukkan bilangan ketiga: ")  
try: 
 
    a = int(tulis_a) 
    b = int(tulis_b) 
    c = int(tulis_c)  
    if a > b and a > c:  
        print("Terbesar: ", a) 
    elif b > a and b > c: 
        print("Terbesar: ", b)  
    elif c > a and c > b:  
        print("Terbesar: ", c) 
except: 
    print("Input yang anda masukan salah: ", c)
