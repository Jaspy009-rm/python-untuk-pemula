firstPerson = {
    "first_name": "Muna",
    "last_name": "Maulida",
    "age": 18
}

# Mengubah nilai dengan menyebut key-nya
firstPerson["age"] = 19

# Mengubah nilai dengan method update()
firstPerson.update({"age": 20})
firstPerson.update({"hair_color": "black"})
print(firstPerson)