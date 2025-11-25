            
def cek_tebakan(tebak, angka_rahasia):
    if tebak == angka_rahasia:
        return "Selamat!! Anda Benar"
    elif tebak < angka_rahasia:
        return "Terlalu Kecil"
    else:
        return "Terlalu Besar"
