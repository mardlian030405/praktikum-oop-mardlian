import turtle

class TurtleMardlian:
    def __init__(self, shape, color, x, y):
        self.t=turtle.Turtle()
        self.t.shape(shape)
        self.t.color(color)
        self.t.penup()
        self.t.setpos(x,y)
        self.t.pendown()
     
    def maju(self,jarak):
        self.t.forward(jarak)
    
    def putar_kanan(self, sudut):
        self.t.right(sudut)

    def buat_bintang(self, ukuran):
        for _ in range(5):
            self.maju(ukuran)
            self.putar_kanan(144)

    def buat_bintangberjajar(self, ukuran, jumlah, jarak):
        for _ in range(jumlah):
            self.buat_bintang(ukuran)
            self.t.penup()
            self.maju(jarak)
            self.t.pendown()

    def selesai(self):
        turtle.done()

turtle1=TurtleMardlian("turtle","blue",0, 200)
turtle2=TurtleMardlian("turtle","red",200, 200 )
turtle1.buat_bintangberjajar(100, 3, 100)
turtle2.buat_bintangberjajar(100, 2, -100)
turtle1.selesai()
turtle2.selesai()
