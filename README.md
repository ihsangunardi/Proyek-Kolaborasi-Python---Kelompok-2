# Proyek-Kolaborasi-Python---Kelompok-2




## Fitur utama
- **Random Number Generator** yaitu komputer memilih angka secara acak
- **Input Validasi Pengguna** memastikan input berupa angka dan berada dalam rentang yang sudah ditentukan
- **Sistem Batas Percobaan** membuat maksimal percobaan 7 kali
- **Feedback Langsung** memberikan petunjuk jika tebakan "Terlalu Kecil", "Terlalu Besar", atau "Benar"
- **Akhir Permainan** Menamilkan hasil menang atau kalah

---





## Dokumentasi Teknis
### **Flowchart Program**

````mermaid
flowchart TD
    A([Start]) --> B[Inisialisasi:<br>paling_kecil=1<br>paling_besar=50<br>batas_percobaan=7<br>angka_rahasia=random]
    B --> C[percobaan = 0<br>menang = False]

    C --> D{percobaan < batas_percobaan?}
    D -->|Tidak| O[Print: Percobaan habis<br>Tampilkan angka_rahasia<br>End]

    D -->|Ya| E[percobaan += 1<br>Tampilkan nomor percobaan]
    E --> F[Minta input tebakan<br>Validasi input]

    F --> G{tebak == angka_rahasia?}
    G -->|Ya| H[Print: Selamat!<br>Tampilkan angka_rahasia<br>menang=True]
    H --> I([End])

    G -->|Tidak| J{tebak < angka_rahasia?}
    J -->|Ya| K[Print: Terlalu Kecil]
    J -->|Tidak| L[Print: Terlalu Besar]

    K --> C
    L --> C

````
---

### Penjelasan Alur Program

1. Program menginisialisasi rentang angka dan batas percobaan.

2. Komputer memilih angka rahasia secara acak.

3. Pengguna diminta memasukkan tebakan.

4. Input divalidasi (harus angka dan dalam rentang yang sudah ditentukan).

5. Sistem mengevaluasi:
   Jika tebakan benar, permainan selesai.
   Jika terlalu besar atau terlalu kecil, pengguna diminta mencoba lagi.

7. Jika pengguna gagal dalam 7 percobaan, angka rahasia ditampilkan.

---
## Anggota Kelompok :  

| Nama | NIM | Github |
|------|-----|--------|
| Muhammad Ihsan Gunardi | 250211060044 | https://github.com/ihsangunardi |
| Hanna Siahaan | 250211060033 | https://github.com/anaashnn |
| Anastasia Tinungki | 250211060029 | https://github.com/anastasia04tinungki-coder |
| Paris Kevin | 250211060045 | https://github.com/Pariskevin |
