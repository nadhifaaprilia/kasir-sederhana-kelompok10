
print("=== PROGRAM KASIR SEDERHANA ===")

jumlah_jenis = int(input("Berapa jenis barang yang dibeli: "))

<<<<<<< HEAD
total = harga * jumlah

print("\nData barang berhasil dicatat.")
print("Nama barang:", nama_barang)
print("Harga:", harga)
print("Jumlah:", jumlah)

print("\n=== TOTAL BELANJA ===")
print("Total belanja:", total)
=======
data_barang = []

for i in range(jumlah_jenis):
    print(f"\n--- Barang ke-{i+1} ---")

    nama_barang = input("Nama barang: ")
    harga = int(input("Harga satuan: "))
    jumlah_beli = int(input("Jumlah beli: "))

    data_barang.append({
        "nama": nama_barang,
        "harga": harga,
        "jumlah": jumlah_beli
    })

print("\n=== DATA BARANG ===")

for barang in data_barang:
    print("Nama barang:", barang["nama"])
    print("Harga satuan:", barang["harga"])
    print("Jumlah beli:", barang["jumlah"])
>>>>>>> fitur-input
