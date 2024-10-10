class LabMi:
    def __init__(self, nama_barang, kode_barang, jumlah_barang, kondisi_barang):
        self.nama_barang = nama_barang
        self.kode_barang = kode_barang
        self.jumlah_barang = jumlah_barang
        self.kondisi_barang = kondisi_barang
        
    def tampilkan_baranglab(self):
        print("-" * 45)
        print("     IVENTARISASI LAB MANAJEMEN INFORMATIKA      ")
        print("-" * 45)
        print(f"NAMA BARANG     :{self.nama_barang}")
        print(f"KODE BARANG     :{self.kode_barang}")
        print(f"JUMLAH BARANG   :{self.jumlah_barang}")
        print(f"KONDISI BARANG  :{self.kondisi_barang}")
        print("-" * 45)
        print("NAMA : M. MARDLIAN NUROFIQ")
        print("NIM  : 23091397105")
        
barang1 = LabMi("KOMPUTER", "KB001", "40", "baik")
barang2 = LabMi("PROYEKTOR", "PJ002", "1", "rusak")
barang3 = LabMi("MEJA", "MJ003", "55", "baik")

barang1.tampilkan_baranglab()
barang2.tampilkan_baranglab()
barang3.tampilkan_baranglab()