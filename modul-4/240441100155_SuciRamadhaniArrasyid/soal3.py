class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def nama(self):
        return self.__nama

    @property
    def umur(self):
        return self.__umur

    @property
    def keluhan(self):
        return self.__keluhan


class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan):
        pasien = Pasien(nama, umur, keluhan)
        self.__daftar_pasien.append(pasien)
        print("Pasien berhasil ditambahkan.")

    def tampilkan_pasien(self):
        if not self.__daftar_pasien:
            print("Belum ada pasien yang terdaftar.")
        else:
            print("\n=== Daftar Pasien ===")
            for idx, pasien in enumerate(self.__daftar_pasien, start=1):
                print(f"\nPasien {idx}:")
                print(f"  Nama     : {pasien.nama}")
                print(f"  Umur     : {pasien.umur}")
                print(f"  Keluhan  : {pasien.keluhan}")


def main():
    klinik = Klinik()

    while True:
        print("\n=== MENU KLINIK ===")
        print("1. Tambah Pasien")
        print("2. Lihat Daftar Pasien")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            try:
                umur = int(input("Masukkan umur pasien: "))
                keluhan = input("Masukkan keluhan pasien: ")
                klinik.tambah_pasien(nama, umur, keluhan)
            except ValueError:
                print("Umur harus berupa angka.")
        elif pilihan == '2':
            klinik.tampilkan_pasien()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem klinik!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

main()