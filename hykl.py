#visualisasi sorting nama saja
Kue = ['Sponge Cake', 'Apple Pie', 'Ovaltine', 'Avocado Bread', 'Blueberry Pancake', 'Caramel Pancake', 'Strawberry Cupcakes', 'Almond Chocolate', 'Red Velvet Pancake', 'Matcha Latte', 'Nutella Muffin']

def merge_sort_nama(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_nama(left_arr)
        merge_sort_nama(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].lower() < right_arr[j].lower():
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

merge_sort_nama(Kue)
print(Kue)

#visualisasi sorting nama dan deskripsi
kue_list = [    {"nama": "Sponge Cake", "harga": 34000, "kategori": "Tart Cake", "rasa": "Fluffy Jelly", "stok": 20},   
             {"nama": "Apple Pie", "harga": 40000, "kategori": "Pie", "rasa": "Apple", "stok": 20},   
            {"nama": "Ovaltine", "harga": 43000, "kategori": "Brownies", "rasa": "Ovaltine", "stok": 17},   
            {"nama": "Avocado Bread", "harga": 45000, "kategori": "Bread", "rasa": "Avocado", "stok": 20},    
            {"nama": "Blueberry Pancake", "harga": 45000, "kategori": "Pancake", "rasa": "Blueberry", "stok": 20},    
            {"nama": "Caramel Pancake", "harga": 45000, "kategori": "Pancake", "rasa": "Caramel", "stok": 20},    
            {"nama": "Strawberry Cupcakes", "harga": 45000, "kategori": "Cupcake", "rasa": "Strawberry", "stok": 23},    
            {"nama": "Almond Chocolate", "harga": 50000, "kategori": "Pie", "rasa": "Chocolate", "stok": 20},    
            {"nama": "Red Velvet Pancake", "harga": 55000, "kategori": "Pancake", "rasa": "Red Velvet", "stok": 20},    
            {"nama": "Matcha Latte", "harga": 56000, "kategori": "Muffin", "rasa": "Matcha", "stok": 20},    
            {"nama": "Nutella Muffin", "harga": 69000, "kategori": "Muffin", "rasa": "Chocolate", "stok": 20}]

def merge_sort_nama(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_nama(left_arr)
        merge_sort_nama(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]["nama"].lower() < right_arr[j]["nama"].lower():
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

merge_sort_nama(kue_list)

print(kue_list)

#visualisasi sorting harga saja
harga = [50000, 40000, 45000, 45000, 45000, 56000, 69000, 43000, 55000, 34000, 45000]

def merge_sort_harga(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_harga(left_arr)
        merge_sort_harga(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

merge_sort_harga(harga)
print(harga)

#visualisasi sorting harga dan deskripsi
def merge_sort_harga(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_harga(left_arr)
        merge_sort_harga(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]["price"] < right_arr[j]["price"]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

harga = [    {"name": "Almond Chocolate", "price": 50000, "category": "Pie", "flavor": "Chocolate", "stock": 20},    
         {"name": "Apple Pie", "price": 40000, "category": "Pie", "flavor": "Apple", "stock": 20},    
         {"name": "Avocado Bread", "price": 45000, "category": "Bread", "flavor": "Avocado", "stock": 20},    
         {"name": "Blueberry Pancake", "price": 45000, "category": "Pancake", "flavor": "Blueberry", "stock": 20},    
         {"name": "Caramel Pancake", "price": 45000, "category": "Pancake", "flavor": "Caramel", "stock": 20},    
         {"name": "Matcha Latte", "price": 56000, "category": "Muffin", "flavor": "Matcha", "stock": 20},    
         {"name": "Nutella Muffin", "price": 69000, "category": "Muffin", "flavor": "Chocolate", "stock": 20},    
         {"name": "Ovaltine", "price": 43000, "category": "Brownies", "flavor": "Ovaltine", "stock": 17},    
         {"name": "Red Velvet Pancake", "price": 55000, "category": "Pancake", "flavor": "Red Velvet", "stock": 20},    
         {"name": "Sponge Cake", "price": 34000, "category": "Tart Cake", "flavor": "Fluffy Jelly", "stock": 20},    
         {"name": "Strawberry Cupcakes", "price": 45000, "category": "Cupcake", "flavor": "Strawberry", "stock": 23}]

merge_sort_harga(harga)

print(harga)

#visualisasi mencari nama saja

def jump_search(key, data):
    if not data:
        print("Data Tidak Ditemukan!")
        return None

    n = len(data)
    step = int(n ** 0.5)
    prev = 0

    while prev < n and data[prev] < key:
        prev += step
    prev -= step
    while prev < n:
        if data[prev] == key:
            return data[prev]
        prev += 1
    print("Data Tidak Ditemukan!")
    return None

# contoh pemanggilan fungsi
list_barang = ['Almond Chocolate', 'Apple Pie', 'Avocado Bread', 'Blueberry Pancake', 'Caramel Pancake', 'Matcha Latte', 'Nutella Muffin', 'Ovaltine', 'Red Velvet Pancake', 'Sponge Cake', 'Strawberry Cupcakes']
key = "Matcha Latte"
result = jump_search(key, list_barang)

if result:
    print("Data ditemukan:", result)
else:
    print("Data tidak ditemukan!")

#visualisasi mencari nama dan deskripsi produk

kue = [    {"name": "Almond Chocolate", "price": 50000, "category": "Pie", "flavor": "Chocolate", "stock": 20},    
         {"name": "Apple Pie", "price": 40000, "category": "Pie", "flavor": "Apple", "stock": 20},    
         {"name": "Avocado Bread", "price": 45000, "category": "Bread", "flavor": "Avocado", "stock": 20},    
         {"name": "Blueberry Pancake", "price": 45000, "category": "Pancake", "flavor": "Blueberry", "stock": 20},    
         {"name": "Caramel Pancake", "price": 45000, "category": "Pancake", "flavor": "Caramel", "stock": 20},    
         {"name": "Matcha Latte", "price": 56000, "category": "Muffin", "flavor": "Matcha", "stock": 20},    
         {"name": "Nutella Muffin", "price": 69000, "category": "Muffin", "flavor": "Chocolate", "stock": 20},    
         {"name": "Ovaltine", "price": 43000, "category": "Brownies", "flavor": "Ovaltine", "stock": 17},    
         {"name": "Red Velvet Pancake", "price": 55000, "category": "Pancake", "flavor": "Red Velvet", "stock": 20},    
         {"name": "Sponge Cake", "price": 34000, "category": "Tart Cake", "flavor": "Fluffy Jelly", "stock": 20},    
         {"name": "Strawberry Cupcakes", "price": 45000, "category": "Cupcake", "flavor": "Strawberry", "stock": 23}]

def jump_search(key):
    data = kue
    
    if not data:
        print("Data Tidak Ditemukan!")
        return None

    n = len(data)
    step = int(n ** 0.5)
    prev = 0

    while prev < n and data[prev]['name'] < key:
        prev += step
    prev -= step
    while prev < n:
        if data[prev]['name'] == key:
            print(f"Nama: {data[prev]['name']}")
            print(f"Harga: {data[prev]['price']}")
            print(f"Kategori: {data[prev]['category']}")
            print(f"Rasa: {data[prev]['flavor']}")
            print(f"Stok: {data[prev]['stock']}")
            return data[prev]
        prev += 1
    print("Data Tidak Ditemukan!")
    return None

jump_search("Matcha Latte")