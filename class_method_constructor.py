# Class dengan constructor __init__
class Cat:
    color = "hitam"

    def __init__(self, color):
        self.color = color

# Membuat object dengan mengirim nilai color
cat1 = Cat("orange")
print(cat1.color)  # orange