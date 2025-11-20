"""
SIS_praktik_lanjutan.py
Ujian Akhir Praktik Lanjutan: Sistem Informasi Siswa (SIS) Sederhana

Cara pakai:
- Letakkan file ini di folder yang sama dengan 'database_siswa.txt' (atau buat file
  itu manual jika belum ada) lalu jalankan: python SIS_praktik_lanjutan.py

Fitur sesuai spesifikasi ujian: load/save file, nested dict data structure,
modular functions, helper functions returning tuples, error handling, CLI menu.
"""

import os
from typing import Dict, List, Tuple, Any

DATA_FILE = 'database_siswa.txt'

# -------------------- Helper functions --------------------

def parse_line_to_record(line: str) -> Tuple[str, dict]:
    """Parse satu baris dari file ke (nis, { 'nama': ..., 'nilai': [...] })"""
    # Format: NIS,NAMA LENGKAP,NILAI_1;NILAI_2;...
    parts = [p.strip() for p in line.strip().split(',')]
    if not parts or parts == ['']:
        raise ValueError('Baris kosong')
    if len(parts) < 2:
        raise ValueError('Baris tidak sesuai format (kurang kolom)')
    nis = parts[0]
    nama = parts[1]
    nilai_list: List[int] = []
    if len(parts) >= 3 and parts[2] != '':
        # nilai dipisah dengan ;
        nilai_strs = [s.strip() for s in parts[2].split(';') if s.strip() != '']
        for ns in nilai_strs:
            try:
                nilai_list.append(int(ns))
            except ValueError:
                # jika tidak bisa konversi, skip atau bisa raise; kita skip dan lanjut
                continue
    return nis, {'nama': nama, 'nilai': nilai_list}


def format_record_to_line(nis: str, record: dict) -> str:
    """Ubah record ke satu baris file sesuai format."""
    nama = record.get('nama', '').strip()
    nilai_list = record.get('nilai', [])
    nilai_part = ';'.join(str(int(n)) for n in nilai_list) if nilai_list else ''
    return f"{nis},{nama},{nilai_part}\n"


def calc_stats(nilai_list: List[int]) -> Tuple[float, int, int]:
    """Menghitung rata-rata, nilai_max, nilai_min.
    Jika tidak ada nilai, rata-rata = 0 dan max/min = 0.
    Mengembalikan tuple (avg, max, min).
    """
    if not nilai_list:
        return 0.0, 0, 0
    total = sum(nilai_list)
    count = len(nilai_list)
    avg = total / count
    return avg, max(nilai_list), min(nilai_list)


def determine_grade(avg: float) -> Tuple[str, bool]:
    """Menentukan grade berdasarkan aturan dan kembalikan (grade, is_pass).
    is_pass di-return hanya sebagai contoh penggunaan tuple; tidak dipakai di UI.
    """
    if avg >= 85:
        return 'A', True
    if avg >= 75:
        return 'B', True
    if avg >= 65:
        return 'C', True
    if avg >= 50:
        return 'D', False
    return 'E', False


# -------------------- File I/O --------------------

def load_data_from_file(filename: str) -> Dict[str, dict]:
    """Mencari file dan memuat data ke nested dictionary.
    Jika file tidak ada, kembalikan dict kosong.
    """
    data: Dict[str, dict] = {}
    if not os.path.exists(filename):
        # File tidak ditemukan -> mulai dengan kosong
        return data
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    nis, rec = parse_line_to_record(line)
                    # Pastikan nis adalah string dan unik
                    data[str(nis)] = rec
                except ValueError:
                    # Lewatkan baris yang tidak sesuai
                    continue
    except Exception as e:
        print(f"Gagal membaca file '{filename}': {e}")
    return data


def save_data_to_file(filename: str, data: Dict[str, dict]) -> bool:
    """Menulis seluruh data ke file (overwrite). Mengembalikan True jika sukses."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for nis in sorted(data.keys(), key=lambda x: int(x) if x.isdigit() else x):
                line = format_record_to_line(nis, data[nis])
                f.write(line)
        return True
    except Exception as e:
        print(f"Gagal menyimpan ke '{filename}': {e}")
        return False


# -------------------- Fitur menu (fungsi terpisah) --------------------

def lihat_daftar_siswa(data_siswa: Dict[str, dict]) -> None:
    """Menampilkan daftar semua siswa: NIS: Nama Lengkap."""
    if not data_siswa:
        print("Belum ada data siswa.")
        return
    print("Daftar Siswa:")
    for nis in sorted(data_siswa.keys(), key=lambda x: int(x) if x.isdigit() else x):
        nama = data_siswa[nis].get('nama', '')
        print(f"{nis}: {nama}")


def lihat_detail_siswa(data_siswa: Dict[str, dict]) -> None:
    nis = input('Masukkan NIS siswa: ').strip()
    if nis == '':
        print('NIS tidak boleh kosong.')
        return
    rec = data_siswa.get(nis)
    if not rec:
        print('Error: NIS tidak ditemukan.')
        return
    nama = rec.get('nama', '')
    nilai_list = rec.get('nilai', [])
    avg, nmax, nmin = calc_stats(nilai_list)
    grade, is_pass = determine_grade(avg)
    print('--- Detail Siswa ---')
    print(f'NIS  : {nis}')
    print(f'Nama : {nama}')
    if nilai_list:
        print('Daftar Nilai : ' + ', '.join(str(n) for n in nilai_list))
    else:
        print('Daftar Nilai : (belum ada nilai)')
    print(f'Rata-rata    : {avg:.2f}')
    print(f'Nilai Tertinggi: {nmax}')
    print(f'Nilai Terendah : {nmin}')
    print(f'Grade Akhir  : {grade}')


def tambah_siswa_baru(data_siswa: Dict[str, dict]) -> None:
    nis = input('Masukkan NIS baru: ').strip()
    if nis == '':
        print('NIS tidak boleh kosong. Batal.')
        return
    if nis in data_siswa:
        print('Error: NIS sudah ada. Batal.')
        return
    nama = input('Masukkan Nama Lengkap: ').strip()
    if nama == '':
        print('Nama tidak boleh kosong. Batal.')
        return
    # Tambah record baru dengan list nilai kosong
    data_siswa[nis] = {'nama': nama, 'nilai': []}
    print(f'Sukses: Siswa {nama} (NIS {nis}) ditambahkan.')


def tambah_nilai_siswa(data_siswa: Dict[str, dict]) -> None:
    nis = input('Masukkan NIS siswa: ').strip()
    if nis == '':
        print('NIS tidak boleh kosong. Batal.')
        return
    rec = data_siswa.get(nis)
    if not rec:
        print('Error: NIS tidak ditemukan. Batal.')
        return
    nilai_input = input('Masukkan nilai baru (angka 0-100): ').strip()
    try:
        nilai = int(nilai_input)
    except ValueError:
        print('Input nilai tidak valid. Harus berupa angka integer. Batal.')
        return
    if nilai < 0 or nilai > 100:
        print('Nilai di luar rentang 0-100. Batal.')
        return
    rec.setdefault('nilai', []).append(nilai)
    print(f'Sukses: Nilai {nilai} ditambahkan untuk NIS {nis} ({rec.get("nama")} ).')


def simpan_dan_keluar(data_siswa: Dict[str, dict]) -> None:
    sukses = save_data_to_file(DATA_FILE, data_siswa)
    if sukses:
        print('Data berhasil disimpan. Program berakhir.')
    else:
        print('Terjadi kesalahan saat menyimpan data. Program berakhir (tetap keluar).')


# -------------------- Program Utama --------------------

def main():
    print('Memulai Sistem Informasi Siswa (SIS) Sederhana...')
    data_semua_siswa = load_data_from_file(DATA_FILE)
    if data_semua_siswa:
        print(f"Memuat data dari '{DATA_FILE}'... Sukses. Jumlah siswa: {len(data_semua_siswa)}")
    else:
        print(f"File '{DATA_FILE}' tidak ditemukan atau kosong. Memulai dengan data kosong.")

    while True:
        print('\n--- Sistem Informasi Siswa ---')
        print('1. Lihat Daftar Siswa')
        print('2. Lihat Detail Siswa')
        print('3. Tambah Siswa Baru')
        print('4. Tambah Nilai Siswa')
        print('5. Simpan & Keluar')
        print('------------------------------')
        pilihan = input('Pilih menu: ').strip()
        if pilihan == '1':
            lihat_daftar_siswa(data_semua_siswa)
        elif pilihan == '2':
            lihat_detail_siswa(data_semua_siswa)
        elif pilihan == '3':
            tambah_siswa_baru(data_semua_siswa)
        elif pilihan == '4':
            tambah_nilai_siswa(data_semua_siswa)
        elif pilihan == '5':
            simpan_dan_keluar(data_semua_siswa)
            break
        else:
            print('Pilihan tidak dikenali. Silakan pilih angka 1-5.')


if __name__ == '__main__':
    main()
