
#MINI PROJECT 2 MANAJEMEN DAFTAR WISATA DI KALTIM
users = {
    "manajer": {"password": "97623", "role": "manajer"},
    "karyawan": {"password": "sukichan", "role":  "karyawan"}

}

daftar_wisata = {
    "pulau beras basah": {"lokasi": "bontang", "tiket": 5000},
    "pantai kemala": {"lokasi": "samarinda", "tiket": 10000},
    "danau ubur ubur": {"lokasi": "pulau kakaban", "tiket": 7000},
    "teluk lerong gerdon": {"lokasi": "samarinda ulu", "tiket": 8000},
    "danau labuan cermin": {"lokasi": "berau", "tiket": 15000}

}


#READ
def read_data():
    if not daftar_wisata:
        print("belum ada di daftar tempat wisata.")
        return
    print("\n---Daftar tempat wisata di kaltim---")
    for nama, info in daftar_wisata.items():
        print(f"nama: {nama}")
        print(f"lokasi: {info['lokasi']}")
        print(f"tiket: {info['tiket']}")
        print("=" * 30)

#CREATE
def create_data():
    nama = input("masukan nama tempat wisata: ")
    if nama in daftar_wisata :
        print("tempat wisata ini sudah ada. ")
        return 
    lokasi = input("masukan lokasi: ")
    try:
        tiket = int(input("masukan harga tiket: "))
    except ValueError:
        print("inputnya harus berupa angka")
        return
    daftar_wisata[nama] = {"lokasi": lokasi, "tiket": tiket}
    print("data tempat wisata berhasil di tambahkan")

#UPDATE
def update_data():
    read_data()
    nama = input("masukan nama wisata yang ingin di ubah: ")
    if nama in daftar_wisata:
        lokasi = input("masukan lokasi baru: ")
        try:
            tiket = int(input("masukan harga tiket baru: "))
        except ValueError:
            print("harus input angka yahhhh")
            return
        daftar_wisata[nama] = {"lokasi": lokasi, "tiket": tiket}
        print(f"wisata {nama.title()} berhasil di perbarui")   

    else:
        print("wisata tidak di temukan")

#DELETE
def delete_data():
    try:
        read_data()
        nama = input("masukan wisata yang ingin di hapus: ")
        if nama in daftar_wisata:
            del daftar_wisata[nama]
            print(f"wisata {nama.title()} berhasil di hapus")
    except KeyboardInterrupt:
        print("JANGAN CRTL+C YAHHHH")

    else:
        print("wisata tidak di temukan")

#MENUUU
def menu(role):
    while True:
        if role == "manajer":
            print("===MENU UTAMAA===")
            print("1.lihat daftar wisata")
            print("2.tambah tempat wisata")
            print("3.ubah data tempat wisata")
            print("4.hapus wisata")
            print("5.keluar program")
            try:
                pilihan = int(input("masukan pilihan 1-5: "))
            except ValueError:
                print("hanya bisa input angka ")
            except KeyboardInterrupt:
                print("JANGAN PENCET DENGAN CRTL+C")
                return
            

            if pilihan == 1:
                read_data()
            elif pilihan == 2:
                create_data()
            elif pilihan == 3:
                update_data()
            elif pilihan == 4:
                delete_data()
            elif pilihan == 5:
                print("keluar dari program")
                break
            else:
                print("input tidak valid,pilihlah sesuai akses 1-5")

        elif role == "karyawan":
            print("===MENU UTAMA===")
            print("1.lihat daftar wisata")
            print("2.keluar program")
            try:
                pilihan = int(input("masukan pilihan 1-2: "))
            except ValueError:
                print("harus berupa angka yahh inputnya")
            except KeyboardInterrupt:
                print("JANGAN TEKAN CRTL+C")
                return
            

            if pilihan == 1:
                read_data()
            elif pilihan == 2:
                print("keluar dari program")
                break
            else:
                print("input tidak valid,pilihlah akses dari 1-2")


def login():
    print("===SISTEM LOGIN MANAJEMEN WISATA KALTIM===")
    username = input("masukan username: ")
    password = input("masukan password: ")
    if username in users:
        if users [username] ["password"] == password: 
            role = users[username]["role"]
            print(f"login berhasil,selamat datang, {role} ")
            menu(role)
        else:
            print("password tidak di temukan silahkan coba lagi")
    else:
        print("username salah,silahkan coba lagi")


login()











