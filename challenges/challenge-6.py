import os
from time import sleep

class Warehouse:
    def __init__(self):
        self.data = []
        self.current_number = 1  # Keep track of the current product number
        # kenapa self.current_number ada di __init__? supaya nilainya ga berubah tiap kali kita panggil fungsi create

    def create(self, name: str, stock: int):
        product = {
            "number": self.current_number,
            "name": name,
            "stock": stock
        }
        self.current_number += 1  # Increment the product number for the next product
        self.data.append(product)
    
    def read(self):
        os.system('clear')
        print("-------------------------------------------")
        print(f"{'No':<5} | {'Product Name':<25} | {'Stock':<5} |")
        print("-------------------------------------------")
        for item in self.data:
            product_number = f"{item['number']:<5} "
            product_name = f"| {item['name']:<25} "
            stocks = f"| {item['stock']:<5} |"
            print(product_number + product_name + stocks)
         #   print(f"{item['number']} | {item['name']}")
         #   print(f"Stock: {item['stock']}")

    def delete(self):
        os.system('clear')
        optDel = input("Pilih nomor barang yang ingin didelete: ")
        optDel = int(optDel)
        self.data.pop(optDel - 1)
        self.current_number -= 1
warehouse = Warehouse()

while True:
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Update Stok Barang")
    print("4. Hapus Barang")
    print("5. Exit")
    opt = input(" >> ")

    if opt == "1":
        os.system('clear')
        amount = input("How much product you want to input: ")
        amount = int(amount)

        os.system("clear")
        for i in range(amount):
            name = input("Input product name: ")
            stock = input("Input the stock: ")
            stock = int(stock)

            warehouse.create(name, stock)
        os.system("clear")
    elif opt == "2":
        warehouse.read()
        sleep(3)
        os.system("clear")
    #elif opt == "3":

    elif opt == "4":
        warehouse.delete()
    elif opt == "5":
        print("Program akan keluar")
        sleep(2)
        exit()
    else:
        opt = input("Pilihan tidak valid.\n >> ")
