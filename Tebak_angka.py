import random

paling_kecil = 1
paling_besar = 50
angka_rahasia = random.randint(paling_kecil, paling_besar)
batas_percobaan = 7

def cek_tebakan(tebak, angka_rahasia):
    if tebak == angka_rahasia:
        return "Selamat!! Anda Benar"
    elif tebak < angka_rahasia:
        return "Terlalu Kecil"
    else:
        return "Terlalu Besar"

def mainkan_permainan():
    percobaan = 0
    menang = False

    while percobaan < batas_percobaan:
        percobaan += 1
        tebakan = minta_tebakan()
        hasil = cek_tebakan(tebakan, angka_rahasia)

        if hasil == "Benar":
            print(f"Selamat! Anda berhasil menebak angka rahasia {angka_rahasia} dalam {percobaan} percobaan.")
            menang = True
            break
        else:
            print(f"{hasil}. Coba lagi!")

    if not menang:
        print(f"Maaf, percobaan Anda habis! Angka rahasianya adalah {angka_rahasia}.")
