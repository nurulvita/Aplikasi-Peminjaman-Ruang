from Model.Database import Database
from Model.Ruang import Ruang
from Controller.ControllerUser import User
from prettytable import PrettyTable

class LinkedList (Database):
    def __init__(self):
        self.head = None
        super().__init__()

    def refresh(self): #mensinkronkan data dari database dan node
        while(self.head != None):
            n = self.head
            self.head = self.head.next
            n = None
        User().updatePeminjamanKelas()
        self.add_data()
         
    def add_data(self): #mencari data di databse
        data = self.data_collection.find({"ket" : "Digunakan"})

        for i in data:
            data = [i["no"],i["kode"],i["nim"],i["nama"],i["prodi"],i["mk"],i["keperluan"],i["tanggalp"],i["tanggals"],i["status"],i["ket"]]
            
            self.add(data) #menambahkan data dari database kedalam node

    def add(self, data): #menambahkan data ke dalam node
        new_node = Ruang(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node 

    def displayData(self, data = ""):
        #menampilkan data dalam node
        self.refresh()
        tabel = PrettyTable(['ID','Kelas','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Tanggal Pinjam', 'Tanggal Selesai', 'Status', 'Keterangan'])
        tabel.title = "PEMINJAMAN RUANG KELAS"

        if(data == ""):

            if self.head is None :
                print("Data tidak ditemukan")

            else :
                n = self.head
                while n is not None:
                    
                    tabel.add_row([n.data["no"], n.data["kode"],n.data["nim"], n.data["nama"], n.data["prodi"], n.data["mk"],n.data["keperluan"],
                                   n.data["tanggalp"], n.data["tanggals"],  n.data["status"], n.data["ket"]])
                  
                    n = n.next
        else:
            for i in range(len(data)):
                temp = []
                temp.extend(data[i])
                tabel.add_row(temp)
                
        print(tabel)

    def hasilSearchKodekelas(self, data):
        #menampilkan hasil search berdasarkan kode kelas
        print("\n")
        tabel = PrettyTable(['ID','Kelas','Tanggal Pinjam', 'Tanggal Selesai'])

        for i in range(len(data)):
            tabel.add_row([data[i][0], data[i][1], data[i][7], data[i][8]])

        print(tabel)

    def fibonacci_search(self, arr, x):
        # Mengurutkan elemen-elemen array secara ascending
        arr = sorted(arr)

        # Inisialisasi nilai awal bilangan fibonacci
        fib2 = 0
        fib1 = 1
        fib = fib1 + fib2

        # Melakukan perulangan selama nilai variabel fib lebih kecil dari panjang list/array 
        while fib < len(arr):
            fib2 = fib1
            fib1 = fib
            fib = fib1 + fib2

        # Inisialisasi variabel pencarian
        i = 0
        mid = 0
        n = len(arr)

        # Melakukan pencarian nilai selama bilangan fibonacci masih lebih besar dari 0 dan indeks i masih kurang dari panjang array
        while fib > 0 and i < n:
            # Menentukan indeks tengah
            mid = min(i + fib2, n - 1)

            # Jika elemen pada indeks tengah adalah sebuah sublist, lakukan pencarian secara linier pada sublist
            # if isinstance(arr[mid], list):
            #     sub_arr = arr[mid]
            #     found = False
            #     for element in sub_arr:
            #         if type(element) == type(x) and element == x:
            #             found = True
            #             break
            #     if found:
            #         return mid, sub_arr.index(x)
                    
            #     # Jika elemen terbesar dari sublist lebih kecil dari elemen yang dicari, cari di bagian kanan array
            #     elif type(sub_arr[0]) == type(x) and sub_arr[0] < x:
            #         fib = fib1
            #         fib1 = fib2
            #         fib2 = fib - fib1
            #         i = mid + 1

            #     # Jika elemen terbesar dari sublist lebih besar atau sama dengan elemen yang dicari, cari di bagian kiri array
            #     else:
            #         fib = fib2
            #         fib1 = fib1 - fib2
            #         fib2 = fib - fib1
            #         n = mid

            # Jika elemen pada indeks tengah bukan sublist, lakukan pencarian langsung pada elemen pada indeks tengah
            # else:
            if arr[mid] == x:
                return mid, 0
            
            # Jika elemen pada indeks tengah lebih kecil dari elemen yang dicari, cari di bagian kanan array
            elif arr[mid] < x:
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                i = mid + 1

            # Jika elemen pada indeks tengah lebih besar dari elemen yang dicari, cari di bagian kiri array
            else:
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
                n = mid

    # Jika elemen tidak ditemukan
        return -1, -1

    def searchKelas(self, search):
        self.refresh()
        list_nodes = []
        temp_list = []

        cursor = self.convertData()
        for data in cursor:
            list_nodes.append(data["kode"])
            temp_list.append(data)
            
        if search not in list_nodes:
            return False
        else :     
            searching = self.fibonacci_search(list_nodes, search)
            if searching == -1:
                return False
            else:
                list_nodes = []
                for x in temp_list:
                    if search == x["kode"]:
                        list_nodes.append(list(x.values())[0:])
                return list_nodes
        
    def searchNIM(self, search):
        self.refresh()
        list_nodes = []
        temp_list = []

        cursor = self.convertData()
        for data in cursor:
            list_nodes.append(data["nim"])
            temp_list.append(data)
            
        if search not in list_nodes:
            return False
        else :     
            searching = self.fibonacci_search(list_nodes, search)
            if searching == -1:
                return False
            else:
                list_nodes = []
                for x in temp_list:
                    if search == x["nim"]:
                        list_nodes.append(list(x.values())[0:])
                return list_nodes
        
    def convertData(self):
        if self.head == None:
            return []
        else:
            current = self.head
            result = []
            while current != None:
                result.append(current.data) #menambahkan data kedalam list
                current = current.next
            return result
        
    def quick_sort(self, node, first, last, key):
        
        if last <= first: # base case, jika indeks last lebih kecil atau sama dengan first maka data tidak perlu diurutkan lagi
            return node
                
        if first == last: # base case, jika indeks first dan last sama maka data tidak perlu diurutkan lagi
            return node

        part = self.partition(node, first, last, key) # pemisahan data menjadi dua bagian berdasarkan pivot
        self.quick_sort(node, first, part - 1, key) # melakukan rekursi untuk bagian kiri dari pivot
        self.quick_sort(node, part, last, key) # melakukan rekursi untuk bagian kanan dari pivot
        
        return node
    
    def partition(self, node, first, last, key):
        pivot = node[first][key]
        batas = first + 1

        for i in range(first+1, last):
            if node[i][key] < pivot:
                node[batas], node[i] = node[i], node[batas]
                batas += 1

        node[batas-1], node[first] = node[first], node[batas-1]
        return batas
    
    def sort_node(self,key):
        list_nodes = [] # inisialisasi list kosong untuk menyimpan data dari setiap node
        n = self.head # assign node pertama pada variabel n

        # mengambil data dari setiap node dan memasukkannya ke dalam list_nodes
        while n is not None:
            convert_array = list(n.data.values()) # mengambil data dari dictionary node dan mengkonversinya menjadi list
            list_nodes.append(convert_array) # memasukkan data ke dalam list_nodes
            n = n.next # memindahkan pointer ke node berikutnya

        # melakukan sorting menggunakan quick sort pada list_nodes berdasarkan key yang dipilih
        sort = self.quick_sort(list_nodes, 0, len(list_nodes), key)
        return sort