import random

# Menentukan rentang angka dan batas percobaan
paling_kecil = 1
paling_besar = 50
batas_percobaan = 7

angka_rahasia = random.randint(paling_kecil, paling_besar)

# Meminta tebakan pemain
def minta_tebakan():
    while True:
        try:
            tebak = int(input(f"tebak angka dari {paling_kecil} sampai {paling_besar}: "))
            if paling_kecil <= tebak <= paling_besar:
                return tebak
            else:
                print("input tidak valid. harap masukkan angka dalam rentang yang ditentukan.")
        except ValueError:
            print("input tidak valid. harap masukkan angka yang valid.")

# Mengecek/memvalidasi tebakan
def cek_tebakan(tebak, angka_rahasia):
    if tebak == angka_rahasia:
        return "Benar"
    elif tebak < angka_rahasia:
        return "Terlalu Kecil"
    else:
        return "Terlalu Besar"

# Melacak jumlah percobaan, mendeteksi jika permainan sudah berakhir
def mainkan_permainan():
    percobaan = 0
    menang = False

    while percobaan < batas_percobaan:
        percobaan += 1

        print(f"========== Percobaan {percobaan}/{batas_percobaan} ==========")

        tebak = minta_tebakan()
        hasil = cek_tebakan(tebak, angka_rahasia)

        if hasil == "Benar":
            print(f"Selamat! Anda berhasil menebak angka rahasia {angka_rahasia} dalam {percobaan} percobaan.")
            menang = True
            break
        else:
            print(f"{hasil}. Coba lagi!")

    if not menang:
        print(f"Maaf, percobaan Anda habis! Angka rahasianya adalah {angka_rahasia}.")

if __name__ == "__main__":
    print("Selamat datang di game Tebak Angka!")
    mainkan_permainan()