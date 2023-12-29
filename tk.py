import tkinter as tk


class Cercle:
    def __init__(self, canevas, x, y, r, color):
        self.canevas = canevas
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = 2  # vitesse de déplacement en x
        self.dy = 2  # vitesse de déplacement en y
        self.dessiner_cercle()

    def dessiner_cercle(self):
        self.cercle_id = self.canevas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def move(self):
        self.x += self.dx*2
        self.y += self.dy
        self.canevas.move(self.cercle_id, self.dx, self.dy)
        # Rebondir sur les bords
        if self.x + self.r >= self.canevas.winfo_width() or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r >= self.canevas.winfo_height() or self.y - self.r <= 0:
            self.dy = -self.dy
        self.canevas.after(5, self.move)
        Cercle.pos(self)

    def pos(self):
        print({"color": self.color, "x": self.x, 'y': self.y})


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

b = Cercle(canvas, 200, 200, 40, "blue")
a = Cercle(canvas, 100, 100, 40, "red")
a.move()  # Commencez le mouvement qui inclut le rebond
b.move()  # Commencez le mouvement qui inclut le rebond
root.mainloop()
