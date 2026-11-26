# PROGRAM KALKULATOR SEDERHANA

print("===========================")
print("    KALKULATOR SEDERHANA")
print("===========================")

print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

pilihan = input("Pilih operasi (1-4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Funngsi Pemjumlahan
if pilihan == "1":
    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

# Fungsi pengurangan 
elif pilihan == "2":
    hasil = angka1 - angka2
    print("Hasil pengurangan:", hasil)

# Funngsi perkalian
elif pilihan == "3":
    hasil = angka1 * angka2
    print("Hasil perkalian:", hasil)

# Fungsi Pembagian
elif pilihan == "4":
    hasil = angka1 / angka2
    print("Hasil pembagian:", hasil)


else:
    print("Pilihan tidak tersedia.")
