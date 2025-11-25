def get_guess():
    while True:
        try:
            tebak = int(f"tebak angka dari {paling_kecil} sampai {paling_besar}:")
            if paling_kecil <= tebak <= paling_besar:
                return tebak
            else:
                print("input tidak valid. harap masukkan angka dalam rentang yang ditentukan.")
        except ValueError:
            print("input tidak valid.harap masukkan angka yang valid.")