def jumlah_digit(n):
    if n == 0:
        return 0
    return (n % 10) + jumlah_digit(n // 10)

# Contoh pemanggilan
hasil = jumlah_digit(1234567)
print(hasil)