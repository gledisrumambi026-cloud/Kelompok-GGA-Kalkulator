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

if pilihan == "1":
    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

elif pilihan == "2":
    hasil = angka1 - angka2
    print("Hasil pengurangan:", hasil)

# --- BAGIAN ANGGOTA 1 (Branch: fitur-perkalian) ---


# --- BAGIAN ANGGOTA 2 (Branch: fitur-pembagian) ---


else:
    print("Pilihan tidak tersedia.")
