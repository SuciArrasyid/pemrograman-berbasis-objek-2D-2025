class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.jenis = "Kucing"
        self.warna = warna
        self.suara = "Meow"

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Jenis: {self.jenis}, Warna: {self.warna}")

    def bersuara(self):
        print(f"{self.nama} bersuara: {self.suara}")


class Kambing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.jenis = "Kambing"
        self.warna = warna
        self.suara = "Mbeeek"

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Jenis: {self.jenis}, Warna: {self.warna}")

    def bersuara(self):
        print(f"{self.nama} bersuara: {self.suara}")


class Burung:
    def __init__(self, nama, warna_bulu):
        self.nama = nama
        self.jenis = "Burung"
        self.warna_bulu = warna_bulu
        self.suara = "Cuit cuit"

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Jenis: {self.jenis}, Warna Bulu: {self.warna_bulu}")

    def bersuara(self):
        print(f"{self.nama} bersuara: {self.suara}")


hewan_list = []
data_hewan = [
    ("Kitty", "Hitam", Kucing),
    ("Billy", "Putih", Kambing),
    ("Tety", "Kuning", Burung)
]

#membuat objek dan menyimpannya ke list
for data in data_hewan:
    hewan = data[2](data[0], data[1])
    hewan_list.append(hewan)

print("Data Hewan:")
print("=" * 50)
for hewan in hewan_list:
    hewan.tampilkan_info()
    hewan.bersuara()
print("=" * 50)
