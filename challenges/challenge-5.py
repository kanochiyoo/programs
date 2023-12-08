carts = []

while True:
    print("Welcome...\nMenu e-Anya")
    print("1. Lihat keranjang")
    print("2. Menambahkan isi keranjang")
    print("3. Menghitung total isi keranjang")
    print("4. Exit")	

    option = input(int("Silahkan pilih nomor menu: "))

    carts = []
    if option == 1:
        for product in carts:
            print(f"Barang: {product['name']} | Harga: {product['price']} | Jumlah: {product['qty']}")

    if option == 2:
        name = input("Masukkan nama barang: ")
        