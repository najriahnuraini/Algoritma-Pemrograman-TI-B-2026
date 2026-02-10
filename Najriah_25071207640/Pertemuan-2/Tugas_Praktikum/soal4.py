def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    return a * pangkat_rekursif(a, b - 1)

# Contoh pemanggilan
hasil = pangkat_rekursif(3, 3)
print(hasil)