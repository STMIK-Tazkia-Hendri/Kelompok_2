# Soal nomor 2. Buatlah fungsi untuk mengambil irisan dan beda setangkup dari dua himpunan ini
# Definisi himpunan A dan B
A = {33, 47, 50, 18, 22, 3, 23, 14, 3, 19}
B = {23, 12, 56, 21, 21, 33, 51,15, 6, 4, 21}

# Fungsi untuk irisan
def irisan(set_A, set_B): 
    return set_A.intersection(set_B)

# Fungsi untuk beda setangkup
def beda_setangkup(set_A, set_B):
    return set_A.symmetric_difference(set_B)

# Fungsi peluang
def peluang(himpunan, semesta):
    return len(himpunan) / len(semesta)
# Menghitung irisan dan beda setangkup
irisan_himpunan = irisan(A, B)
beda_setangkup_himpunan = beda_setangkup(A, B)

# Menghitung peluang P(A) dan P(B)
semesta = A.union(B)  # Gabungan himpunan sebagai semesta
peluang_A = peluang(A, semesta)
peluang_B = peluang(B, semesta)

# Output hasil
print("Irisan (A ∩ B):", irisan_himpunan)
print("Beda setangkup (A Δ B):", beda_setangkup_himpunan)
print("Peluang P(A):", peluang_A)
print("Peluang P(B):", peluang_B)
