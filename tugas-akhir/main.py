produk = [
    {"id": 1, "nama_produk": "Apel", "harga": 5000},
    {"id": 2, "nama_produk": "Anggur", "harga": 7000},
    {"id": 3, "nama_produk": "Jambu", "harga": 2000}
]

keranjang = []

def tampil_produk():
    print("-----------------------------------------")
    print("|No\t|Nama Produk\t|Harga per kg\t|")
    print("-----------------------------------------")
    for item in produk:
        print(f"|{item['id']}\t|{item['nama_produk']}\t\t|{item['harga']}\t\t|")
    print("-----------------------------------------")

def tambah_produk():
    nama = input("Masukkan nama produk baru: ")
    harga = int(input("Masukkan harga per kg produk baru: "))
    
    for item in produk:
        if produk:
            max_id = max(item['id'])
        else:
            max_id = 0

    id = max_id + 1
    produk.append({"id": id, "nama_produk": nama, "harga": harga})
    print(f"Produk {nama} berhasil ditambahkan!")

def update_produk():
    tampil_produk()

    produk_id = int(input("Masukkan ID produk yang akan diupdate: "))
    
    for item in produk:
        if item['id'] == produk_id:
            nama_baru = input(f"Masukkan nama baru untuk produk {item['nama_produk']} (kosongkan untuk tidak mengubah): ")
            harga_baru = input(f"Masukkan harga baru untuk produk {item['nama_produk']} (kosongkan untuk tidak mengubah): ")
            
            if nama_baru:
                item['nama_produk'] = nama_baru
            if harga_baru:
                item['harga'] = int(harga_baru)
            print(f"Produk dengan ID {produk_id} berhasil diupdate!")
            return
    
    print(f"Produk dengan ID {produk_id} tidak ditemukan.")

def delete_produk():
    tampil_produk()

    produk_id = int(input("Masukkan ID produk yang akan dihapus: "))
    
    for item in produk:
        if item['id'] == produk_id:
            produk.remove(item)
            print(f"Produk dengan ID {produk_id} berhasil dihapus!")
            return
    
    print(f"Produk dengan ID {produk_id} tidak ditemukan.")

def tampil_keranjang():
    if not keranjang:
        print("Keranjang belanja kosong.")
    else:
        print("\nIsi Keranjang Belanja:")
        print("No  | Nama Produk     | Harga per kg | Jumlah(kg) | Total Harga")
        print("-" * 60)
        total_belanja = 0
        for index, item in enumerate(keranjang, start=1):
            total_harga = item['harga'] * item['quantity']
            total_belanja += total_harga
            print(f"{index:2}  | {item['nama_produk']:15} | {item['harga']:15} | {item['quantity']:8} | {total_harga}")
        print("-" * 60)
        print(f"Total belanja: {total_belanja}")

def tambah_ke_keranjang():
    while True:
        tampil_produk()
        produk_id = int(input("Masukkan ID produk yang akan ditambahkan ke keranjang (0 untuk selesai): "))
        
        if produk_id == 0:
            break
        
        found = False
        for item in produk:
            if item["id"] == produk_id:
                qty = int(input(f"Masukkan jumlah {item['nama_produk']} yang akan dibeli (kg): "))
                keranjang.append({
                    "id": item["id"],
                    "nama_produk": item["nama_produk"],
                    "harga": item["harga"],
                    "quantity": qty
                })
                found = True
                print(f"{qty} kg {item['nama_produk']} ditambahkan ke keranjang.")
                break
        
        if not found:
            print("Produk dengan ID tersebut tidak ditemukan.")

    tampil_keranjang()

def update_keranjang():
    tampil_keranjang()

    produk_id = int(input("Masukkan ID produk yang akan diupdate di keranjang: "))
    
    for item in keranjang:
        if item['id'] == produk_id:
            harga_baru = input(f"Masukkan harga baru untuk produk {item['nama_produk']} di keranjang (kosongkan untuk tidak mengubah): ")
            qty_baru = input(f"Masukkan jumlah(kg) baru untuk produk {item['nama_produk']} di keranjang (kosongkan untuk tidak mengubah): ")
            
            if harga_baru:
                item['harga'] = int(harga_baru)
            if qty_baru:
                item['quantity'] = int(qty_baru)
            print(f"Harga dan jumlah(kg) produk {item['nama_produk']} di keranjang berhasil diupdate!")
            return
    
    print(f"Produk dengan ID {produk_id} tidak ditemukan di keranjang.")

def delete_keranjang():
    tampil_keranjang()

    produk_id = int(input("Masukkan ID produk yang akan dihapus dari keranjang: "))
    
    for item in keranjang:
        if item['id'] == produk_id:
            keranjang.remove(item)
            print(f"Produk dengan ID {produk_id} berhasil dihapus dari keranjang!")
            return
    
    print(f"Produk dengan ID {produk_id} tidak ditemukan di keranjang.")

if __name__ == "__main__":
    while True:
        tampil_produk()
        
        print("\nProgram Kasir Sederhana")
        print("1. Tambah Produk")
        print("2. Update Produk")
        print("3. Hapus Produk")
        print("4. Tambah ke Keranjang")
        print("5. Update Keranjang")
        print("6. Hapus dari Keranjang")
        print("7. Keluar")
        
        option = int(input("Masukkan pilihan menu: "))
        
        match option:
            case 1:
                tambah_produk()
            case 2:
                update_produk()
            case 3:
                delete_produk()
            case 4:
                tambah_ke_keranjang()
            case 5:
                update_keranjang()
            case 6:
                delete_keranjang()
            case 7:
                break
            case _:
                print("Option tidak valid, silahkan masukan option yang valid(1-8)\n")