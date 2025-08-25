# ===========================================
#   APLIKASI POLLING SEDERHANA
# ===========================================

# Struktur data survei
SURVEI = [
    {
        "pertanyaan": "Apa bahasa pemrograman favoritmu?",
        "opsi": ["Python", "JavaScript", "Java", "C++"]
    },
    {
        "pertanyaan": "Apa sistem operasi yang paling sering kamu gunakan?",
        "opsi": ["Windows", "macOS", "Linux"]
    },
    {
        "pertanyaan": "Tim mana yang akan menang di final piala dunia?",
        "opsi": ["Argentina", "Prancis", "Brasil", "Jerman"]
    }
]

# Inisialisasi hasil polling
hasil_polling = {}
for item in SURVEI:
    for opsi in item["opsi"]:
        hasil_polling[opsi] = 0

print("=" * 44)
print("   SELAMAT DATANG DI APLIKASI POLLING")
print("=" * 44)

# Loop pertanyaan
for idx, item in enumerate(SURVEI, start=1):
    print(f"\nPertanyaan {idx}: {item['pertanyaan']}")
    for opsi in item["opsi"]:
        print(f" - {opsi}")

    # Loop validasi input
    while True:
        jawaban = input("Jawaban Anda: ").strip()
        if jawaban in item["opsi"]:
            print("--- Jazakallah Khoiron! ---")
            hasil_polling[jawaban] += 1
            break
        else:
            print("Jawaban tidak valid. Silakan pilih dari opsi yang tersedia.")

# Menampilkan hasil polling
print("\n" + "=" * 44)
print("               HASIL POLLING")
print("=" * 44)
total_suara = sum(hasil_polling.values())
for opsi, jumlah in hasil_polling.items():
    persentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
    print(f"{opsi} : {jumlah} suara ({persentase:.2f}%)")
print("=" * 44)
