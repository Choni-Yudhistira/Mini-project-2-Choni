import os
import time
import pwinput

users = {
    "Admin": {
        "password": "choni123",
        "role": "Admin"
    },
    "Member": {
        "password": "member123",
        "role": "Member"
    }
}

data_laptop = {}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    time.sleep(1)

def login():
    clear()

    print("==============================")
    print("       SISTEM LAPTOP")
    print("==============================")
    print("           LOGIN")
    print("==============================")

    username = input("Username : ")
    password = pwinput.pwinput("Password : ")

    if username in users:
        if users[username]["password"] == password:
            print("\nLogin berhasil!")
            print("Role :", users[username]["role"])
            pause()
            return users[username]["role"]

    print("\nUsername atau password salah!")
    pause()
    return None

def lihat_data():
    clear()

    print("==============================")
    print("        DATA LAPTOP")
    print("==============================")

    if not data_laptop:
        print("Belum ada data laptop.")
    else:
        for kode, laptop in data_laptop.items():
            print("\nKode     :", kode)
            print("Nama     :", laptop["nama"])
            print("Kategori :", laptop["kategori"])
            print("Harga    : Rp", laptop["harga"])

    input("\nTekan Enter untuk kembali...")

def tambah_data():
    clear()

    print("==============================")
    print("        TAMBAH DATA")
    print("==============================")

    kode = input("Kode laptop : ")

    if kode == "":
        print("Kode tidak boleh kosong!")
        pause()
        return

    if kode in data_laptop:
        print("Kode laptop sudah digunakan!")
        pause()
        return

    nama = input("Nama merk : ")
    kategori = input("Kategori : ")

    if nama == "" or kategori == "":
        print("Nama dan kategori tidak boleh kosong!")
        pause()
        return

    try:
        harga = int(input("Harga : "))

        if harga <= 0:
            print("Harga harus lebih dari 0!")
            pause()
            return

    except ValueError:
        print("Harga harus berupa angka!")
        pause()
        return

    data_laptop[kode] = {
        "nama": nama,
        "kategori": kategori,
        "harga": harga
    }

    print("\nData laptop berhasil ditambahkan!")
    pause()

def ubah_data():
    clear()

    print("==============================")
    print("         UBAH DATA")
    print("==============================")

    kode = input("Kode laptop : ")

    if kode not in data_laptop:
        print("Data laptop tidak ditemukan!")
        pause()
        return

    print("\nData lama")
    print("Nama     :", data_laptop[kode]["nama"])
    print("Kategori :", data_laptop[kode]["kategori"])
    print("Harga    :", data_laptop[kode]["harga"])

    nama = input("\nNama merk baru : ")
    kategori = input("Kategori baru : ")

    if nama == "" or kategori == "":
        print("Data tidak boleh kosong!")
        pause()
        return

    try:
        harga = int(input("Harga baru : "))

        if harga <= 0:
            print("Harga harus lebih dari 0!")
            pause()
            return

    except ValueError:
        print("Harga harus berupa angka!")
        pause()
        return

    data_laptop[kode] = {
        "nama": nama,
        "kategori": kategori,
        "harga": harga
    }

    print("\nData berhasil diubah!")
    pause()

def hapus_data():
    clear()

    print("==============================")
    print("        HAPUS DATA")
    print("==============================")

    kode = input("Kode laptop : ")

    if kode not in data_laptop:
        print("Data laptop tidak ditemukan!")
        pause()
        return

    print("\nData yang akan dihapus:")
    print("Nama     :", data_laptop[kode]["nama"])
    print("Kategori :", data_laptop[kode]["kategori"])
    print("Harga    :", data_laptop[kode]["harga"])

    konfirmasi = input("\nYakin hapus data? (y/n) : ")

    if konfirmasi.lower() == "y":
        del data_laptop[kode]
        print("Data berhasil dihapus!")
    elif konfirmasi.lower() == "n":
        print("Penghapusan dibatalkan.")
    else:
        print("Pilihan tidak valid!")

    pause()

def menu_admin():
    while True:
        clear()

        print("==============================")
        print("          MENU ADMIN")
        print("==============================")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Logout")
        print("==============================")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            lihat_data()

        elif pilihan == "3":
            ubah_data()

        elif pilihan == "4":
            hapus_data()

        elif pilihan == "5":
            print("\nLogout berhasil!")
            pause()
            break

        else:
            print("\nPilihan menu tidak valid!")
            pause()

def menu_user():
    while True:
        clear()

        print("==============================")
        print("           MENU USER")
        print("==============================")
        print("1. Lihat Data")
        print("2. Logout")
        print("==============================")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            lihat_data()

        elif pilihan == "2":
            print("\nLogout berhasil!")
            pause()
            break

        else:
            print("\nPilihan menu tidak valid!")
            pause()


while True:
    role = login()

    if role == "Admin":
        menu_admin()

    elif role == "Member":
        menu_user()

    else:
        pilihan = input("\nCoba login lagi? (y/n) : ")

        if pilihan.lower() != "y":
            print("\nProgram selesai.")
            break