animals = ["Ayam", "Bebek", "Cicak"]

# Menghapus item tertentu dengan remove()
animals.remove("Bebek")
print(animals)  # ['Ayam', 'Cicak']

# Menghapus item terakhir dengan pop()
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals)  # ['Ayam', 'Bebek']

# Menghapus item berdasarkan indeks dengan pop(indeks)
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals)  # ['Bebek', 'Cicak']

# Mengosongkan seluruh isi list dengan clear()
animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals)  # []