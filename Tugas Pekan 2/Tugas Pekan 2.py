# kasir_cerdas_v2.py
# Kasir Cerdas 2.0 - Functions & Loops
# Siap jalan: python kasir_cerdas_v2.py

def tampilkan_header():
    print("=" * 44)
    print("      SELAMAT DATANG DI TOKO SERBAGUNA")
    print("=" * 44)
    print("\n--- Masukkan Detail Barang ---")
    print("(Ketik 'selesai' di nama barang untuk selesai)\n")

def get_numeric_input(prompt, tipe=float):
    """
    Meminta input sampai user memasukkan angka valid.
    tipe: float atau int
    """
    while True:
        nilai = input(prompt)
        try:
            if tipe is int:
                return int(nilai)
            else:
                return float(nilai)
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

def format_rupiah(angka):
    """
    Mengembalikan string format Rupiah, misal:
    1250000.0 -> "Rp 1.250.000,00"
    """
    # pastikan angka adalah float
    nilai = float(angka)
    # ambil bagian integer dan dua desimal
    bagian_int = int(abs(nilai))
    bagian_desimal = int(round((abs(nilai) - bagian_int) * 100))
    # format ribuan menggunakan koma lalu ganti ke titik
    bagian_int_str = f"{bagian_int:,}".replace(",", ".")
    tanda = "-" if nilai < 0 else ""
    return f"{tanda}Rp {bagian_int_str},{bagian_desimal:02d}"

def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0.0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total

def hitung_diskon(subtotal):
    """
    Aturan diskon:
    - subtotal >= 500_000 => 10%
    - subtotal >= 250_000 => 5%
    - else 0%
    Mengembalikan: (jumlah_diskon, persen)
    """
    if subtotal >= 500_000:
        persen = 10
    elif subtotal >= 250_000:
        persen = 5
    else:
        persen = 0
    diskon = subtotal * (persen / 100)
    return diskon, persen

def tampilkan_struk(semua_nama, semua_harga, semua_jumlah, subtotal, total_diskon, persen_diskon):
    print("\nMenghitung total belanja Anda...\n")
    print("=" * 44)
    print("         STRUK PEMBELIAN ANDA")
    print("=" * 44)
    print("Detail Belanja:\n")
    for i in range(len(semua_nama)):
        nama = semua_nama[i]
        harga = semua_harga[i]
        jumlah = semua_jumlah[i]
        total_item = harga * jumlah
        # rapikan kolom dengan f-string (bisa disesuaikan)
        print(f"{i+1}. {nama} ({jumlah} x {format_rupiah(harga)}) = {format_rupiah(total_item)}")
    print("-" * 44)
    print(f"Subtotal            : {format_rupiah(subtotal)}")
    print(f"Diskon ({persen_diskon}%)        : - {format_rupiah(total_diskon)}")
    print("-" * 44)
    total_bayar = subtotal - total_diskon
    print(f"Total yang harus dibayar: {format_rupiah(total_bayar)}")
    print("=" * 44)
    print("      TERIMA KASIH TELAH BERBELANJA!")
    print("=" * 44)

def main():
    daftar_nama_barang = []
    daftar_harga_barang = []
    daftar_jumlah_barang = []

    tampilkan_header()

    while True:
        nama_barang = input("Nama Barang: ").strip()
        if nama_barang.lower() == "selesai":
            break
        if nama_barang == "":
            print("Nama barang tidak boleh kosong. Ulangi.")
            continue

        harga = get_numeric_input("Harga Satuan: Rp ", tipe=float)
        jumlah = get_numeric_input("Jumlah: ", tipe=int)

        daftar_nama_barang.append(nama_barang)
        daftar_harga_barang.append(harga)
        daftar_jumlah_barang.append(jumlah)

        print("--- Barang berhasil ditambahkan! ---\n")

    if len(daftar_nama_barang) == 0:
        print("\nTidak ada barang yang dimasukkan. Program selesai.")
        return

    subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)
    diskon, persen = hitung_diskon(subtotal)
    tampilkan_struk(daftar_nama_barang, daftar_harga_barang, daftar_jumlah_barang, subtotal, diskon, persen)

if __name__ == "__main__":
    main()
# kasir_cerdas_v2.py
# Kasir Cerdas 2.0 - Functions & Loops
# Siap jalan: python kasir_cerdas_v2.py

def tampilkan_header():
    print("=" * 44)
    print("      SELAMAT DATANG DI TOKO SERBAGUNA")
    print("=" * 44)
    print("\n--- Masukkan Detail Barang ---")
    print("(Ketik 'selesai' di nama barang untuk selesai)\n")

def get_numeric_input(prompt, tipe=float):
    """
    Meminta input sampai user memasukkan angka valid.
    tipe: float atau int
    """
    while True:
        nilai = input(prompt)
        try:
            if tipe is int:
                return int(nilai)
            else:
                return float(nilai)
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

def format_rupiah(angka):
    """
    Mengembalikan string format Rupiah, misal:
    1250000.0 -> "Rp 1.250.000,00"
    """
    # pastikan angka adalah float
    nilai = float(angka)
    # ambil bagian integer dan dua desimal
    bagian_int = int(abs(nilai))
    bagian_desimal = int(round((abs(nilai) - bagian_int) * 100))
    # format ribuan menggunakan koma lalu ganti ke titik
    bagian_int_str = f"{bagian_int:,}".replace(",", ".")
    tanda = "-" if nilai < 0 else ""
    return f"{tanda}Rp {bagian_int_str},{bagian_desimal:02d}"

def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0.0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total

def hitung_diskon(subtotal):
    """
    Aturan diskon:
    - subtotal >= 500_000 => 10%
    - subtotal >= 250_000 => 5%
    - else 0%
    Mengembalikan: (jumlah_diskon, persen)
    """
    if subtotal >= 500_000:
        persen = 10
    elif subtotal >= 250_000:
        persen = 5
    else:
        persen = 0
    diskon = subtotal * (persen / 100)
    return diskon, persen

def tampilkan_struk(semua_nama, semua_harga, semua_jumlah, subtotal, total_diskon, persen_diskon):
    print("\nMenghitung total belanja Anda...\n")
    print("=" * 44)
    print("         STRUK PEMBELIAN ANDA")
    print("=" * 44)
    print("Detail Belanja:\n")
    for i in range(len(semua_nama)):
        nama = semua_nama[i]
        harga = semua_harga[i]
        jumlah = semua_jumlah[i]
        total_item = harga * jumlah
        # rapikan kolom dengan f-string (bisa disesuaikan)
        print(f"{i+1}. {nama} ({jumlah} x {format_rupiah(harga)}) = {format_rupiah(total_item)}")
    print("-" * 44)
    print(f"Subtotal            : {format_rupiah(subtotal)}")
    print(f"Diskon ({persen_diskon}%)        : - {format_rupiah(total_diskon)}")
    print("-" * 44)
    total_bayar = subtotal - total_diskon
    print(f"Total yang harus dibayar: {format_rupiah(total_bayar)}")
    print("=" * 44)
    print("      TERIMA KASIH TELAH BERBELANJA!")
    print("=" * 44)

def main():
    daftar_nama_barang = []
    daftar_harga_barang = []
    daftar_jumlah_barang = []

    tampilkan_header()

    while True:
        nama_barang = input("Nama Barang: ").strip()
        if nama_barang.lower() == "selesai":
            break
        if nama_barang == "":
            print("Nama barang tidak boleh kosong. Ulangi.")
            continue

        harga = get_numeric_input("Harga Satuan: Rp ", tipe=float)
        jumlah = get_numeric_input("Jumlah: ", tipe=int)

        daftar_nama_barang.append(nama_barang)
        daftar_harga_barang.append(harga)
        daftar_jumlah_barang.append(jumlah)

        print("--- Barang berhasil ditambahkan! ---\n")

    if len(daftar_nama_barang) == 0:
        print("\nTidak ada barang yang dimasukkan. Program selesai.")
        return

    subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)
    diskon, persen = hitung_diskon(subtotal)
    tampilkan_struk(daftar_nama_barang, daftar_harga_barang, daftar_jumlah_barang, subtotal, diskon, persen)

if __name__ == "__main__":
    main()
