import turtle

class Kotak:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color("blue")
        
    def kotak_balap(self, size):
        for _ in range(4):
            self.t.forward(size)
            self.t.left(90)
            
    def selesai(self):
        turtle.done()
            
persegi = Kotak()

persegi.kotak_balap(400)

persegi.selesai()    