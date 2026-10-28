# Program: 04_iterasi_dictionary.py
# Deskripsi: Menelusuri key dan value menggunakan method items().

data = {"nama": "Ayu", "nilai": 85, "kelas": "A"}

for key, value in data.items():
    print(f"{key}: {value}")