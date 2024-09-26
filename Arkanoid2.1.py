import tkinter as tk

class Ball:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.size = 20
        self.dx = 5  
        self.dy = -5  
        self.id = canvas.create_oval(x, y, x + self.size, y + self.size, fill=color)

    def move(self):
        # Передвигаем шар
        self.canvas.move(self.id, self.dx, self.dy)
        pos = self.canvas.coords(self.id)

        # Проверка на столкновение с границами
        if pos[1] <= 0 or pos[3] >= self.canvas.winfo_height():  # Верхняя и нижняя границы
            self.dy = -self.dy  

        if pos[0] <= 0 or pos[2] >= self.canvas.winfo_width():  # Левые и правые границы
            self.dx = -self.dx  

        return pos

class Game:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=400, bg='white')
        self.canvas.pack()
        self.ball1 = Ball(self.canvas, 100, 300, 'red')
        self.ball2 = Ball(self.canvas, 500, 300, 'blue')
        self.is_running = False
        self.master.title("Ball Passing Game")

        self.start_button = tk.Button(master, text="Пуск", command=self.start)
        self.start_button.pack()

        self.update()

    def start(self):
        if not self.is_running:
            self.is_running = True

    def update(self):
        if self.is_running:
            self.ball1.move()
            self.ball2.move()

        self.master.after(20, self.update)  

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

