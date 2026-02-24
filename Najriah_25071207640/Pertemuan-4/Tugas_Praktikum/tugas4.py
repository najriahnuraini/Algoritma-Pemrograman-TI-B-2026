class InputError(Exception):
    pass

try:
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))

    if b == 0:
        raise InputError("Tidak boleh membagi dengan nol!")

    hasil = a / b
    print("Hasil pembagian:", hasil)

except ValueError:
    print("Input harus berupa angka!")

except InputError as e:
    print(e)

finally:
    print("Program selesai dijalankan.")