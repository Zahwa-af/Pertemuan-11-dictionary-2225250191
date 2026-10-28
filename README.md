# Pertemuan 11 Dictionary/Map

Nama: Zahwa Ajmala Fitriani
NIM: 22225250191
Kelas: 3B

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
- Key Utama: NIM (string) sebagai identitas unik mahasiswa (contoh: "A001").
- Value: Dictionary bersarang yang memuat `nama` (string), `kelas` (string), dan `nilai` (integer/float).

## Cara Menjalankan
python3 praktik/data_mahasiswa.py

## Test Case
| Kasus | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan | Data Citra ditampilkan | Sesuai |
| Pencarian tidak tersedia | A999 | Pesan 'Data tidak ditemukan' | Pesan 'Data tidak ditemukan' | Sesuai |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 berubah menjadi 82 | Sesuai |
| Penambahan data | A006 | Key A006 tersedia setelah ditambahkan | Key A006 tersedia setelah ditambahkan | Sesuai |
| Rekap | items() | Semua NIM dan data tampil | Semua NIM dan data tampil | Sesuai |

## Refleksi
Kesalahan akses key yang umum terjadi adalah `KeyError` akibat mengakses key yang tidak ada secara langsung menggunakan `[]`. Cara memperbaikinya adalah dengan menggunakan method `.get()` atau memeriksa keberadaan key terlebih dahulu menggunakan operator `in`.