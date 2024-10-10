import turtle

class Segitiga360px:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color("red")
        
    def bentuk_segitiga(self, size):
        for _ in range(3):
            self.t.forward(size)
            self.t.left(120)
            
    def selesai(self):
        turtle.done()
        
segitiga = Segitiga360px()

segitiga.bentuk_segitiga(350)

segitiga.selesai()