import turtle

class MyTurtle:
    def __init__(self, color, shape):
        # Membuat objek turtle
        self.t = turtle.Turtle()  # Object dari class Turtle
        self.t.color(color)  # Mengatur warna turtle
        self.t.shape(shape)  # Mengatur bentuk turtle

    def maju(self, jarak):
        # Method untuk menggerakkan turtle maju
        self.t.forward(jarak)

    def putar_kanan(self, sudut):
        # Method untuk memutar turtle ke kanan
        self.t.right(sudut)

    def buat_segi_sembilan(self, ukuran):
        # Method untuk menggambar segi sembilan (nonagon)
        sudut = 360 / 9  # Sudut putar untuk segi sembilan
        for _ in range(9):
            self.maju(ukuran)
            self.putar_kanan(sudut)

    def selesai(self):
        # Method untuk menyelesaikan gambar
        turtle.done()

# Membuat objek turtle dengan warna dan bentuk tertentu
turtle1 = MyTurtle("blue", "turtle")

# Menggambar segi sembilan dengan ukuran sisi 100
turtle1.buat_segi_sembilan(100)

# Menyelesaikan gambar
turtle1.selesai()
