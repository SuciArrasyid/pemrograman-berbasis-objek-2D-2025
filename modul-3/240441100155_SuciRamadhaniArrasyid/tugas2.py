class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        kendaraan = self.jenis_kendaraan.lower()
        if kendaraan == "truk":
            return 6 
        elif kendaraan == "mobil":
            return 4
        else:
            return 5


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        maskapai = self.maskapai.lower()
        if maskapai == "garuda":
            return 2
        elif maskapai == "lion air":
            return 3
        else:
            return 4


class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        kendaraan = self.jenis_kendaraan.lower()
        if kendaraan == "pesawat":
            estimasi = PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
        else:
            estimasi_darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan).estimasi_waktu()
            estimasi_udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
            estimasi = min(estimasi_darat, estimasi_udara)

        if self.asal.lower() != self.tujuan.lower():
            return estimasi + 3
        else:
            return estimasi

daftar_pengiriman = []

while True:
    print("\n=== Tambah Pengiriman Internasional ===")
    asal = input("Masukkan kota/negara asal: ")
    tujuan = input("Masukkan kota/negara tujuan: ")
    jenis_kendaraan = input("Masukkan jenis kendaraan (truk/mobil/pesawat/lain): ")
    maskapai = input("Masukkan nama maskapai (Garuda/Lion Air/lain): ")

    pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)
    daftar_pengiriman.append(pengiriman)

    lagi = input("Tambah pengiriman lagi? (ya/tidak): ")
    if lagi.lower() != 'ya':
        break

print("\n=== Daftar Semua Pengiriman ===")
for i, kirim in enumerate(daftar_pengiriman, start=1):
    print(f"\nPengiriman #{i}")
    print(f"Asal        : {kirim.asal}")
    print(f"Tujuan      : {kirim.tujuan}")
    print(f"Kendaraan   : {kirim.jenis_kendaraan}")
    print(f"Maskapai    : {kirim.maskapai}")
    print(f"Estimasi    : {kirim.estimasi_waktu()} hari")
