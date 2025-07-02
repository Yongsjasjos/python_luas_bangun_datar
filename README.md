# 📐 Program Penghitung **Luas** Bangun Datar

Program ini adalah aplikasi berbasis terminal yang dibuat menggunakan bahasa Python untuk menghitung **luas berbagai bangun datar** seperti segitiga, persegi panjang, persegi, jajar genjang, trapesium, lingkaran, layang-layang, dan belah ketupat.

---

## 🛠️ Fitur

* ✅ Validasi input lengkap (tidak menerima angka negatif, nol, atau input non-numerik).
* ✅ Antarmuka pengguna interaktif dan mudah digunakan.
* ✅ Mendukung perhitungan berulang hingga pengguna memilih keluar.
* ✅ Format hasil perhitungan yang rapi dan mudah dibaca.

---

## 🗂️ Struktur File

```
.
├── geometri.py     # Berisi fungsi-fungsi perhitungan luas
├── main.py         # Berisi menu utama dan interaksi dengan pengguna
└── README.md       # Dokumentasi proyek
```

---

## 🔧 Cara Menjalankan

1. Pastikan Anda memiliki Python 3.x terinstal di sistem Anda.
2. Clone repositori ini atau unduh file `geometri.py` dan `main.py`.
3. Jalankan file `main.py` di terminal atau command prompt:

```bash
python main.py
```

---

## 🧮 Bangun Datar yang Didukung

| No | Bangun Datar    | Fungsi yang Digunakan |
| -- | --------------- | --------------------- |
| 1  | Segitiga        | `segitiga()`          |
| 2  | Persegi Panjang | `persegip()`          |
| 3  | Persegi         | `persegi()`           |
| 4  | Jajar Genjang   | `jajar()`             |
| 5  | Trapesium       | `trapesium()`         |
| 6  | Lingkaran       | `lingkaran()`         |
| 7  | Layang-layang   | `layang()`            |
| 8  | Belah Ketupat   | `kupat()`             |

---

## 🧑‍💻 Contoh Output

```text
Masukkan nama Anda: Yoga
Selamat Datang Yoga di Program Penghitung Luas

Pilih jenis perhitungan:
1. Luas Segitiga
...
Pilih jenis perhitungan (1-9): 1
Masukkan ukuran alas segitiga: 6
Masukkan ukuran tinggi segitiga: 4
Luas segitiga dengan alas 6.0 cm dan tinggi 4.0 cm adalah 12.0 cm²

Apakah Anda ingin mencoba lagi? (yes/no): no
Terima kasih kepada Yoga yang sudah mencoba Project Sederhana saya.
```

---

## ✅ Validasi Input

* ❌ Nilai negatif → Tidak diterima.
* ❌ Angka 0 → Tidak valid.
* ❌ Huruf/simbol → Akan diminta input ulang.
* ✅ Hanya menerima angka positif (integer atau desimal).

---

## 📄 Lisensi

Proyek ini bebas digunakan untuk pembelajaran atau pengembangan pribadi. Sertakan atribusi jika ingin membagikan ulang.

---

## 🙌 Kontribusi

Jika Anda memiliki ide perbaikan atau ingin menambahkan fitur lain (misalnya: menghitung keliling, konversi satuan, atau GUI), silakan buat pull request atau fork proyek ini.

---

## 🧑‍💻 Penulis

**Yoga Pratama**

* 📧 Email: yp170090@gmail.com
* 🔗 LinkedIn: https://www.linkedin.com/in/yoga-pratama-923202349
* 🐱 GitHub: https://github.com/Yongsjasjos
