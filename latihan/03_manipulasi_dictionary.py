# Program: 03_manipulasi_dictionary.py
# Deskripsi: Menambah, mengubah, dan menghapus elemen dictionary.

data = {"nama": "Ayu", "nilai": 85}

# Menambah dan mengubah data
data["kelas"] = "A"
data["nilai"] = 90
print(data)

# Menghapus key 'kelas'
data.pop("kelas")
print(data)