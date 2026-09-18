
print("=== PROGRAM KASIR SEDERHANA ===")

nama_barang = input("Nama barang: ")
harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

total = harga * jumlah

print("\nData barang berhasil dicatat.")
print("Nama barang:", nama_barang)
print("Harga:", harga)
print("Jumlah:", jumlah)

print("\n=== TOTAL BELANJA ===")
print("Total belanja:", total)

print("\n=== PEMBAYARAN ===")

bayar = int(input("Uang pembayaran: "))

kembalian = bayar - total

print("Total belanja:", total)
print("Uang pembayaran:", bayar)
print("Kembalian:", kembalian)