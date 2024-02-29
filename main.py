import tkinter as tk
from random import randint

# Create a Tkinter window
root = tk.Tk()
root.title("Drawing with Tkinter")

# Create a Canvas widget
canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()


class RollDice:
    def __init__(self, rct1=20, rct2=20, rct3=120, rct4=120):
        self.rct1 = rct1
        self.rct2 = rct2
        self.rct3 = rct3
        self.rct4 = rct4
        self.s1a = 45
        self.s1b = 45
        self.s2a = 45
        self.s2b = 70
        self.s3a = 45
        self.s3b = 95
        self.s4a = 95
        self.s4b = 45
        self.s5a = 95
        self.s5b = 70
        self.s6a = 95
        self.s6b = 95
        self.s7a = 70
        self.s7b = 70
        self.circle_radius = 4
        self.dot_list = [self.s1a, self.s1b, self.s2a, self.s2b, self.s3a, self.s3b, self.s4a, self.s4b,
                         self.s5a, self.s5b, self.s6a, self.s6b, self.s7a, self.s7b]

    def count(self, cnt: int):
        for item in range(cnt):
            canvas.create_rectangle(self.rct1, self.rct2, self.rct3, self.rct4)
            self.rct1 += 120
            self.rct3 += 120
            rolled = randint(1, 6)
            print(f"Rolled now: {rolled}")
            if rolled == 1:
                roll.draw1()
            elif rolled == 2:
                roll.draw2()
            elif rolled == 3:
                roll.draw3()
            elif rolled == 4:
                roll.draw4()
            elif rolled == 5:
                roll.draw5()
            elif rolled == 6:
                roll.draw6()
            self.dot_list = [cord + 120 for cord in self.dot_list]
            print(f"dot_list now: {self.dot_list}")

    def draw1(self):
        return (
            canvas.create_oval(self.s7a - self.circle_radius, self.s7b - self.circle_radius,
                               self.s7a + self.circle_radius, self.s7b + self.circle_radius, fill="black"),
        )

    def draw2(self):
        return (
            canvas.create_oval(self.s1a - self.circle_radius, self.s1b - self.circle_radius,
                               self.s1a + self.circle_radius, self.s1b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6a - self.circle_radius, self.s6b - self.circle_radius,
                               self.s6a + self.circle_radius, self.s6b + self.circle_radius, fill="black"),
        )

    def draw3(self):
        return (
            canvas.create_oval(self.s1a - self.circle_radius, self.s1b - self.circle_radius,
                               self.s1a + self.circle_radius, self.s1b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s7a - self.circle_radius, self.s7b - self.circle_radius,
                               self.s7a + self.circle_radius, self.s7b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6a - self.circle_radius, self.s6b - self.circle_radius,
                               self.s6a + self.circle_radius, self.s6b + self.circle_radius, fill="black")
        )

    def draw4(self):
        return (
            canvas.create_oval(self.s1a - self.circle_radius, self.s1b - self.circle_radius,
                               self.s1a + self.circle_radius, self.s1b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s3a - self.circle_radius, self.s3b - self.circle_radius,
                               self.s3a + self.circle_radius, self.s3b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s4a - self.circle_radius, self.s4b - self.circle_radius,
                               self.s4a + self.circle_radius, self.s4b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6a - self.circle_radius, self.s6b - self.circle_radius,
                               self.s6a + self.circle_radius, self.s6b + self.circle_radius, fill="black"),

        )

    def draw5(self):
        return (
            canvas.create_oval(self.s1a - self.circle_radius, self.s1b - self.circle_radius,
                               self.s1a + self.circle_radius, self.s1b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s3a - self.circle_radius, self.s3b - self.circle_radius,
                               self.s3a + self.circle_radius, self.s3b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s4a - self.circle_radius, self.s4b - self.circle_radius,
                               self.s4a + self.circle_radius, self.s4b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s7a - self.circle_radius, self.s7b - self.circle_radius,
                               self.s7a + self.circle_radius, self.s7b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6a - self.circle_radius, self.s6b - self.circle_radius,
                               self.s6a + self.circle_radius, self.s6b + self.circle_radius, fill="black")
        )

    def draw6(self):
        return (
            canvas.create_oval(self.s1a - self.circle_radius, self.s1b - self.circle_radius,
                               self.s1a + self.circle_radius, self.s1b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s2a - self.circle_radius, self.s2b - self.circle_radius,
                               self.s2a + self.circle_radius, self.s2b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s3a - self.circle_radius, self.s3b - self.circle_radius,
                               self.s3a + self.circle_radius, self.s3b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s4a - self.circle_radius, self.s4b - self.circle_radius,
                               self.s4a + self.circle_radius, self.s4b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s5a - self.circle_radius, self.s5b - self.circle_radius,
                               self.s5a + self.circle_radius, self.s5b + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6a - self.circle_radius, self.s6b - self.circle_radius,
                               self.s6a + self.circle_radius, self.s6b + self.circle_radius, fill="black"),
        )


roll = RollDice()
roll.count(2)

# Start the Tkinter event loop
root.mainloop()
