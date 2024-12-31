print('Yoga Pratama 1232050163 Kelas 3E')
import math

#memeriksa_inputan_user
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            #jika_input_angka_negatif
            if value < 0:
                print("Maaf, sebuah ukuran tidak mungkin negatif,  silakan ulangi lagi.")
            #jika_input_angka_Nol
            elif value ==0:
                print('Ukuran tidak berinilai 0, silahkan ulangi')
            else:
                return value
        #jika_inputan_bukan_angka
        except ValueError:
            print("Maaf, yang Anda masukkan bukan angka bilangan bulat/desimal. Silakan ulangi lagi.")
            
def segitiga():
    alas = get_float('Masukkan ukuran alas segitiga: ')
    tinggi = get_float('Masukkan ukuran tinggi segitiga: ')
    luas = 0.5 * alas * tinggi
    return f'Luas segitiga dengan alas {alas:,} cm dan tinggi {tinggi:,} cm adalah {luas:,} cm²'

def persegip():
    panjang = get_float('Masukkan ukuran panjang persegi panjang: ')
    lebar = get_float('Masukkan ukuran lebar persegi panjang: ')
    luas = panjang * lebar
    return f'Luas persegi panjang dengan panjang {panjang:,} cm dan lebar {lebar:,} cm adalah {luas:,} cm²'
def persegi():
    sisi = get_float('Masukkan ukuran sisi persegi: ')
    luas = pow(sisi,2)
    return f'Luas persegi dengan sisi {sisi:,} cm adalah {luas:,} cm²'

def jajar():
    alas = get_float('Masukkan ukuran alas jajar genjang: ')
    tinggi = get_float('Masukkan ukuran tinggi jajar genjang: ')
    luas = alas * tinggi
    return f'Luas jajar genjang dengan alas {alas:,} cm dan tinggi {tinggi:,} cm adalah {luas:,} cm²'

def trapesium():
    atas = get_float('Masukkan ukuran sisi atas: ')
    bawah = get_float('Masukkan ukuran sisi bawah: ')
    tinggi = get_float('Masukkan ukuran tinggi: ')
    luas = 0.5 * (atas + bawah) * tinggi
    return f'Luas trapesium dengan sisi atas {atas:,} cm, sisi bawah {bawah:,} cm, dan tinggi {tinggi:,} cm adalah {luas:,} cm²'

def lingkaran():
    r = get_float('Masukan Nilai R (Jari-jari): ')
    luas = math.pi*pow(r,2)
    return f'Luas lingkaran dengan jari-jari {r:,} cm adalah {luas:,} cm²'

def layang():
    d1 = get_float('Masukkan ukuran diagonal 1: ')
    d2 = get_float('Masukkan ukuran diagonal 2: ')
    luas = 0.5 * d1 * d2
    return f'Luas layang-layang dengan diagonal 1 {d1:,} cm dan diagonal 2 {d2:,} cm adalah {luas:,} cm²'

def kupat():
    d1 = get_float('Masukkan ukuran diagonal 1: ')
    d2 = get_float('Masukkan ukuran diagonal 2: ')
    luas = 0.5 * d1 * d2
    return f'Luas belah ketupat dengan diagonal 1 {d1:,} cm dan diagonal 2 {d2:,} cm adalah {luas:,} cm²'
    
