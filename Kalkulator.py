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

# --- AREA BRANCH 1: FITUR PENJUMLAHAN ---
if pilihan == "1":
    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

# --- AREA BRANCH 2: FITUR PENGURANGAN ---
if pilihan == "2":
    hasil = angka1 - angka2
    print("Hasil pengurangan:", hasil)

# --- AREA BRANCH 3: FITUR PERKALIAN ---


# --- AREA BRANCH 4: FITUR PEMBAGIAN ---


if pilihan not in ["1", "2", "3", "4"]:
    print("Pilihan tidak tersedia.")
