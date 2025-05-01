class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Departemen : {self.departemen}")


class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan  : {self.tunjangan}")
        print("Status     : Karyawan Tetap\n")


class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja  : {self.jam_kerja} jam/hari")
        print("Status     : Karyawan Harian\n")


class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("\n=== Daftar Karyawan ===")
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

while True:
    print("\nTambah Karyawan:")
    print("1. Karyawan Tetap")
    print("2. Karyawan Harian")
    print("0. Selesai")
    pilihan = input("Pilih jenis karyawan (1/2/0): ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        gaji = int(input("Masukkan gaji: "))
        departemen = input("Masukkan departemen: ")
        tunjangan = int(input("Masukkan tunjangan: "))
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
        manajemen.tambah_karyawan(karyawan)

    elif pilihan == "2":
        nama = input("Masukkan nama: ")
        gaji = int(input("Masukkan gaji per hari: "))
        departemen = input("Masukkan departemen: ")
        jam_kerja = int(input("Masukkan jam kerja per hari: "))
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
        manajemen.tambah_karyawan(karyawan)

    elif pilihan == "0":
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")

manajemen.tampilkan_semua_karyawan()
