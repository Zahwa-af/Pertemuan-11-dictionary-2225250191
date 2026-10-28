# Program: 02_akses_get.py
# Deskripsi: Akses aman ke value menggunakan method get().

data = {"nama": "Ayu", "nilai": 85}

print(data.get("nama"))
print(data.get("kelas", "Belum ada"))