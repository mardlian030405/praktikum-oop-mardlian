import turtle

class TurtleBalap:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color("blue")
        
    def membuat_bulat(self, radius):
        self.t.circle(radius)
        
    def selesai(self):
        turtle.done()
        
buat = TurtleBalap()

buat.membuat_bulat(radius=200)

buat.selesai()