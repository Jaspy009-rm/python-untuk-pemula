# Membuat dictionary untuk menyimpan informasi tentang seseorang
firstPerson = {
    "first_name": "Muna",
    "last_name": "Maulida",
    "age": 18
}

# Mengakses item pada dictionary dengan nama key
print(firstPerson["first_name"])  # Muna

# Mengakses item dengan method get()
print(firstPerson.get("age"))  # 18

# Mengambil semua key dengan keys()
print(firstPerson.keys())

# Mengambil semua value dengan values()
print(firstPerson.values())