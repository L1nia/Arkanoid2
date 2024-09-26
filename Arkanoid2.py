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
        self.master.title("Ball Collision Game")

        self.start_button = tk.Button(master, text="Пуск", command=self.start)
        self.start_button.pack()

        self.update()

    def start(self):
        if not self.is_running:
            self.is_running = True

    def update(self):
        if self.is_running:
            pos1 = self.ball1.move()
            pos2 = self.ball2.move()

            # Проверка на столкновение
            if self.check_collision(pos1, pos2):
                # Простая обработка столкновения - меняем направление
                self.ball1.dx = -self.ball1.dx  
                self.ball1.dy = -self.ball1.dy
                self.ball2.dx = -self.ball2.dx  
                self.ball2.dy = -self.ball2.dy

                # Перемещаем шары, чтобы они не застревали друг в друге
                overlap_x = (pos1[2] - pos2[0]) / 2
                overlap_y = (pos1[3] - pos2[1]) / 2
                self.canvas.move(self.ball1.id, overlap_x, overlap_y)
                self.canvas.move(self.ball2.id, -overlap_x, -overlap_y)

        self.master.after(20, self.update)  

    def check_collision(self, pos1, pos2):
        return (pos1[0] < pos2[2] and pos1[2] > pos2[0] and
                pos1[1] < pos2[3] and pos1[3] > pos2[1])

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

