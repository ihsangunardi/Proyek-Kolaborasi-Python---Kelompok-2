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