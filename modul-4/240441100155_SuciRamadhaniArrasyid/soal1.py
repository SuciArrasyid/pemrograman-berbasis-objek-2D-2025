class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    @property
    def no_rek(self):
        return self.__no_rek

    @property
    def nama_pemilik(self):
        return self.__nama_pemilik

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False

    def tampilkan_data(self):
        print(f"No Rek: {self.no_rek}, Nama: {self.nama_pemilik}, Saldo: {self.saldo}")


class Bank:
    def __init__(self):
        self.__rekening_list = []

    def tambah_rekening(self, no_rek, nama_pemilik, saldo_awal):
        rek = RekeningBank(no_rek, nama_pemilik, saldo_awal)
        self.__rekening_list.append(rek)

    def cari_rekening(self, no_rek):
        for rek in self.__rekening_list:
            if rek.no_rek == no_rek:
                return rek
        return None

    def setor(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            rek.setor(jumlah)
            print("Setoran berhasil.")
        else:
            print("Rekening tidak ditemukan.")

    def tarik(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            if rek.tarik(jumlah):
                print("Penarikan berhasil.")
            else:
                print("Saldo tidak cukup.")
        else:
            print("Rekening tidak ditemukan.")

    def tampilkan_semua_rekening(self):
        print("\nData Rekening di Bank:")
        for rek in self.__rekening_list:
            rek.tampilkan_data()


def main():
    bank = Bank()

    while True:
        print("\n--- MENU BANK ---")
        print("1. Tambah Rekening")
        print("2. Setor")
        print("3. Tarik")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            no_rek = input("Masukkan No Rekening: ")
            nama = input("Masukkan Nama Pemilik: ")
            saldo_awal = float(input("Masukkan Saldo Awal: "))
            bank.tambah_rekening(no_rek, nama, saldo_awal)

        elif pilihan == "2":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = float(input("Masukkan Jumlah Setor: "))
            bank.setor(no_rek, jumlah)

        elif pilihan == "3":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = float(input("Masukkan Jumlah Tarik: "))
            bank.tarik(no_rek, jumlah)

        elif pilihan == "4":
            bank.tampilkan_semua_rekening()

        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

main()