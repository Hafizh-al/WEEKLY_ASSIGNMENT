# TUGAS PEKANAN PEKAN 1

# Proyek Kasir Cerdas Sederhana

print("="*43)
print("SELAMAT DATANG DI PROGRAM KASIR CERDAS!")
print("="*43)

# Input Barang 1
print("--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan: Rp "))
jumlah_1 = int(input("Jumlah: "))

# Input Barang 2
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan: Rp "))
jumlah_2 = int(input("Jumlah: "))

# Kalkulasi
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2
subtotal = total_1 + total_2

# Logika Diskon
diskon_persen = 0
if subtotal > 200000:
    diskon_persen = 10
elif subtotal > 100000:
    diskon_persen = 5

jumlah_diskon = subtotal * (diskon_persen / 100)
total_setelah_diskon = subtotal - jumlah_diskon

# Bonus: Tambahkan PPN 11%
ppn = total_setelah_diskon * 0.11
total_final = total_setelah_diskon + ppn

# Bonus: Uang kembalian
uang_bayar = float(input("\nMasukkan jumlah uang yang dibayarkan: Rp "))
kembalian = uang_bayar - total_final

# Cetak Struk
print("\n" + "="*43)
print("STRUK PEMBELIAN ANDA")
print("="*43)
print("Detail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("-"*43)
print(f"Subtotal            : Rp {subtotal}")
print(f"Diskon ({diskon_persen}%)      : - Rp {jumlah_diskon}")
print(f"PPN (11%)           : + Rp {ppn}")
print("-"*43)
print(f"Total yang dibayar  : Rp {total_final}")
print(f"Uang dibayarkan     : Rp {uang_bayar}")
print(f"Kembalian           : Rp {kembalian}")
print("="*43)
print("TERIMA KASIH TELAH BERBELANJA!")
print("="*43)