def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

while True:
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")  # Opsi untuk keluar

    pilihan = input("Masukkan pilihan pengoperasian: ")

    if pilihan == '5':
        print("Terima kasih telah menggunakan kalkulator!")
        break

    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(angka1, "+", angka2, "=", tambah(angka1, angka2))

        elif pilihan == '2':
            print(angka1, "-", angka2, "=", kurang(angka1, angka2))

        elif pilihan == '3':
            print(angka1, "*", angka2, "=", kali(angka1, angka2))

        elif pilihan == '4':
            print(angka1, "/", angka2, "=", bagi(angka1, angka2))
    else:
        print("Input tidak valid")