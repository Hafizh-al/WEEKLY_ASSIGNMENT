try:
    # Buka file input dan output
    with open("transaksi_kotor.txt", "r") as file_input, open("laporan_bersih.txt", "w") as file_output:

        # Header laporan
        file_output.write("LAPORAN TRANSAKSI BERSIH\n")
        file_output.write("=========================\n\n")

        # Proses tiap baris
        for baris in file_input:
            baris = baris.strip()

            # Lewati baris kosong
            if not baris:
                continue

            data_potongan = baris.split(",")

            # Pastikan format punya 4 kolom
            if len(data_potongan) != 4:
                print(f"Format salah: {baris}")
                continue

            try:
                id_bersih = data_potongan[0].strip().upper()
                nama_bersih = data_potongan[1].strip().title()
                jumlah_bersih = int(data_potongan[2].strip())
                harga_bersih = float(data_potongan[3].strip())

                total_harga = jumlah_bersih * harga_bersih

                string_output = (
                    f"{id_bersih} | {nama_bersih} | "
                    f"{jumlah_bersih} x {harga_bersih} = {total_harga}\n"
                )
                file_output.write(string_output)

            except ValueError:
                print(f"Data tidak valid: {baris}")
                continue

        # Footer laporan
        file_output.write("\n--- ANALISIS SELESAI ---\n")

    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("File transaksi_kotor.txt tidak ditemukan.")
