#soal nomor 3.buatlah program untuk fungsi menghitung perkalian matrix 
## Perkalian Matriks 4x4
matriksA = -[ 
    [10, 55, 54, 10], 
    [23, 5, 23, 14],
    [21, 7, 13, 11],
    [11, 88, 14, 15], 
]

matriksB = [
    [3, 0, 0, 1],
    [3, 1, 0, 3],
    [3, 0, 1, 3],
    [1, 0, 0, 3]
]
# Perkalian matriks
hasil = [[sum(matriksA[i][k] * matriksB[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

# Menampilkan hasil perkalian
print("Hasil perkalian matriks:")
for baris in hasil:
    print(baris)


