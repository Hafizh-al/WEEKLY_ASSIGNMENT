nama_file = "database_siswa.txt"

def mulai_data(nama_file):  
    data = {} 
    try:     
        with open(nama_file, "r", encoding="utf-8") as f:   
            for line in f:        
                
                line = line.strip()
                if not line:     
                    continue  
                
                
                parts = line.split(",", 2)  
                nis = parts[0].strip()      
                nama = parts[1].strip()    
                
                
                nilai_list = []   
                if len(parts) == 3 and parts[2].strip() != "":
                    nilai_strs = parts[2].split(";")
                    for ns in nilai_strs:
                        nilai_list.append(int(ns))
                
                
                data[nis] = {"nama": nama, "nilai": nilai_list}
    except FileNotFoundError:
        print("File database ga ditemukan, mulai dengan data kosong.")
    return data



siswa_data = mulai_data(nama_file)
print("Data siswa berhasil dibaca:")
for nis, info in siswa_data.items():
    print(f"NIS: {nis}, Nama: {info['nama']}, Nilai: {info['nilai']}")

def simpan_data(nama_file, data_siswa):
    baris = []
    for nis, info in data_siswa.items():
        nama = info.get("nama", "")
        nilai_list = info.get("nilai", [])
        nilai_str = ";".join(str(n) for n in nilai_list)
        baris.append(f"{nis},{nama},{nilai_str}")
    
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("\n".join(baris) + "\n")
    print("Data berhasil disimpan.")

def hitung_data(nilai_list):
    if not nilai_list:
        return 0.0, 0, 0
    total = sum(nilai_list)
    rata = total / len(nilai_list)
    maksimum = max(nilai_list)
    minimum = min(nilai_list)
    return rata, maksimum, minimum

def kasi_nile(ratarata):
    if ratarata >= 85:
        return "A"
    elif ratarata >= 75:
        return "B"
    elif ratarata >= 65:
        return "C"
    elif ratarata >= 50:
        return "D"
    else:
        return "E"
    
def lihat_daftar_siswa(data_siswa):
    if not data_siswa:
        print("Ga ada data siswa.")
        return
    print("\nDaftar Siswa:")
    print("-" * 30)
    print(f"{'NIS':<10} {'Nama':<20}")
    print("-" * 30)
    for nis, info in data_siswa.items():
        nama = info.get("nama", "")
        print(f"{nis:<10} {nama:<20}")
    print("-" * 30)
    
def info_siswa(data_siswa):
    nis = input("Masukkan NIS siswa: ").strip()
    if nis not in data_siswa:
        print("NIS ga ditemukan.")
        return
    info = data_siswa[nis]
    nama = info.get("nama", "")
    nilai_list = info.get("nilai", [])
    rata, maksimum, minimum = hitung_data(nilai_list)
    grade = kasi_nile(rata) if nilai_list else "N/A"
    
    print(f"\nDetail Siswa NIS {nis}:")
    print(f"Nama       : {nama}")
    print(f"Nilai      : {', '.join(map(str, nilai_list)) if nilai_list else 'Belum ada nilai'}")
    if nilai_list:
        print(f"Rata-rata  : {rata:.2f}")
        print(f"Nilai Maks : {maksimum}")
        print(f"Nilai Min  : {minimum}")
        print(f"Grade      : {grade}")
    else:
        print("Rata-rata  : N/A")
        print("Nilai Maks : N/A")
        print("Nilai Min  : N/A")
        print("Grade      : N/A")

def tambah_siswa_baru(data_siswa):
    nis = input("Masukkan NIS baru: ").strip()
    if nis in data_siswa:
        print("Error: NIS sudah ada. Pembatalan.")
        return
    nama = input("Masukkan nama siswa: ").strip()
    if not nama:
        print("Error: Nama ga boleh kosong. Pembatalan.")
        return
    data_siswa[nis] = {"nama": nama, "nilai": []}
    print(f"Siswa baru dengan NIS {nis} dan nama {nama} berhasil ditambahkan.")

def tambah_nilai_siswa(data_siswa):
    nis = input("Masukkan NIS siswa: ").strip()
    if nis not in data_siswa:
        print("NIS ga ditemukan. Pembatalan.")
        return
    while True:
        nilai_input = input("Masukkan nilai baru (0-100) atau 'selesai' untuk berhenti: ").strip()
        if nilai_input.lower() == "selesai":
            break
        if not nilai_input.isdigit():
            print("Error: Nilai harus angka 0-100. Coba lagi.")
            continue
        nilai = int(nilai_input)
        if nilai < 0 or nilai > 100:
            print("Error: Nilai harus di antara 0-100. Coba lagi.")
            continue
        data_siswa[nis]["nilai"].append(nilai)
        print(f"Nilai {nilai} berhasil ditambahkan ke siswa dengan NIS {nis}.")

 

def main():
    data_siswa = mulai_data(nama_file)
    while True:
        print("\nSistem Informasi Siswa (SIS)")
        print("1. Lihat Daftar Siswa")
        print("2. Info Detail Siswa")
        print("3. Tambah Siswa Baru")
        print("4. Tambah Nilai Siswa")
        print("5. Simpan & Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            lihat_daftar_siswa(data_siswa)
        elif pilihan == "2":
            info_siswa(data_siswa)
        elif pilihan == "3":
            tambah_siswa_baru(data_siswa)
        elif pilihan == "4":
            tambah_nilai_siswa(data_siswa)
        elif pilihan == "5":
            simpan_data(nama_file, data_siswa)
            print("Data disimpan. Keluar dari program.")
            break
        else:
            print("Pilihan ga valid. Coba lagi.")

if __name__ == "__main__":
    main()

