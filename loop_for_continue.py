# Melewati nilai tertentu saat perulangan berjalan
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)