class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")
    
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

#objek manusia
manusia1 = Manusia("Alda", 20, "Jakarta")
manusia2 = Manusia("ryan", 18, "Bandung")
manusia3 = Manusia("suci", 19, "Bangkalan")
manusia4 = Manusia("melly", 19, "Bangkalan")
manusia5 = Manusia("luluk", 20, "Surabaya")

#memanggil method berjaan dan berlari
manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()
