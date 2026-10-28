# Program: data_mahasiswa.py
# Deskripsi: Sistem pengelolaan data mahasiswa berbasis dictionary.

def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# Inisialisasi data minimal 5 mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Pencarian data mahasiswa
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil is not None:
    print(f"Pencarian {nim_cari}: {hasil}")
else:
    print(f"Pencarian {nim_cari}: Data tidak ditemukan")

# Pencarian NIM tidak ada
nim_salah = "A999"
hasil_salah = cari_mahasiswa(data_mahasiswa, nim_salah)
if hasil_salah is not None:
    print(f"Pencarian {nim_salah}: {hasil_salah}")
else:
    print(f"Pencarian {nim_salah}: Data tidak ditemukan")

# 2. Tambah mahasiswa baru
data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "B", "nilai": 80}

# 3. Ubah nilai salah satu mahasiswa
data_mahasiswa["A002"]["nilai"] = 82

# 4. Tampilkan seluruh rekap data
print("\n--- Rekap Data Mahasiswa ---")
for nim, info in data_mahasiswa.items():
    print(nim, info)

# 5. Hitung rata-rata nilai
print(f"\nRata-rata Nilai Kelas = {rata_rata_nilai(data_mahasiswa):.2f}")