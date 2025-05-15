class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    @property
    def judul(self):
        return self.__judul

    @property
    def penulis(self):
        return self.__penulis

    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []

    def tambah_buku(self, judul, penulis, jumlah_halaman):
        buku = Buku(judul, penulis, jumlah_halaman)
        self.__daftar_buku.append(buku)

    def tampilkan_buku(self):
        if not self.__daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("\nDaftar Buku:")
            for idx, buku in enumerate(self.__daftar_buku, start=1):
                print(f"\nBuku {idx}:")
                print(f"  Judul          : {buku.judul}")
                print(f"  Penulis        : {buku.penulis}")
                print(f"  Jumlah Halaman : {buku.jumlah_halaman}")


def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            try:
                jumlah_halaman = int(input("Masukkan jumlah halaman: "))
                perpustakaan.tambah_buku(judul, penulis, jumlah_halaman)
                print("Buku berhasil ditambahkan!")
            except ValueError:
                print("Jumlah halaman harus berupa angka.")
        elif pilihan == '2':
            perpustakaan.tampilkan_buku()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

main()