"""
Roll dice.
It rolls the dice from 1 to 6 times, depending on user input.
And it draws dice drawings.

Input:
    - User gives a number from 1 to 6.

Output:
    - roll specified number of dices [1-6]
    - print dices using tkinter

"""

import tkinter as tk
from random import randint

# Create a Tkinter window
root = tk.Tk()
root.title("Rolling dice")

# Create a Canvas widget
canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()


class RollDice:
    """ Get input from user. Expect integer from 1 to 6.
        1. Try to convert to integer. Raise Exception if not.
        2. Check if it is between 1 and 6. Print message if not.

        :return: integer form 1 to 6
        :rtype: int
        """
    def __init__(self, rct1=20, rct2=20+70, rct3=120, rct4=120+70):
        # all rct are rectangle starting and ending positions
        self.rct1 = rct1
        self.rct2 = rct2
        self.rct3 = rct3
        self.rct4 = rct4
        # all s1x and similar are dots in rectangles starting and ending positions.
        self.s1x = 45
        self.s1y = 45+70
        self.s2x = 45
        self.s2y = 70+70
        self.s3x = 45
        self.s3y = 95+70
        self.s4x = 95
        self.s4y = 45+70
        self.s5x = 95
        self.s5y = 70+70
        self.s6x = 95
        self.s6y = 95+70
        self.s7x = 70
        self.s7y = 70+70
        self.circle_radius = 4
        self.dot_list_x = [self.s1x, self.s2x, self.s3x, self.s4x, self.s5x, self.s6x, self.s7x]
        self.dot_list_y = [self.s7y, self.s6y, self.s5y, self.s4y, self.s3y, self.s2y, self.s1y]

    @staticmethod
    def input_validation(a: str):
        """ Get input from user. Expect integer from 1 to 6.
            1. Try to convert to integer. Raise Exception if not.
            2. Check if it is between 1 and 6. Print message if not.

            :return: integer form 1 to 6
            :rtype: int
            """
        try:
            b = int(a)
            if 6 >= b >= 1:
                return b
            print("Invalid number. Enter number from 1 to 6.")
        except ValueError:
            print("Not integer. Enter number from 1 to 6.")

    def count(self, cnt: int):
        """ Our main function.
            Input:
                - Receive integer from 1 to 6.

            1. Draw square, next to each other after every iteration. How many, depends on input.
            2. Get random dice roll from 1 to six with each iteration.
            3. Print number of dots rolled inside every square.
            (adding +120 to x_axis values, makes it printed 120 steps more to the right)

            """
        for item in range(cnt):
            canvas.create_rectangle(self.rct1, self.rct2, self.rct3, self.rct4)
            self.rct1 += 120
            self.rct3 += 120
            rolled = randint(1, 6)
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
            self.dot_list_x = [cord + 120 for cord in self.dot_list_x]
            self.s1x, self.s2x, self.s3x, self.s4x, self.s5x, self.s6x, self.s7x = self.dot_list_x
        self.draw_text(cnt)

    @staticmethod
    def draw_text(cnt: int):
        """Draw the results text."""
        if cnt == 6:
            return (
                canvas.create_text(370, 65, text=f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                       , font=("Arial", 12), fill="black"))
        if cnt == 5:
            return (
                canvas.create_text(310, 65, text=f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                       , font=("Arial", 12), fill="black"))
        if cnt == 4:
            return (
                canvas.create_text(250, 65, text=f"~~~~~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~~~~~"
                       , font=("Arial", 12), fill="black"))
        if cnt == 3:
            return (
                canvas.create_text(190, 65, text=f"~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~"
                       , font=("Arial", 12), fill="black"))
        if cnt == 2:
            return (
                canvas.create_text(130, 65, text=f"~~~~~~~~~ RESULTS ~~~~~~~~~"
                       , font=("Arial", 12), fill="black"))
        if cnt == 1:
            return (
                canvas.create_text(70, 65, text=f"~~ RESULTS ~~"
                       , font=("Arial", 12), fill="black"))
    def draw1(self):
        """
        Draw one dot of dice

        :return:  print one dot and display it on tkinter popup window
        """
        return (
            canvas.create_oval(self.s7x - self.circle_radius, self.s7y - self.circle_radius,
                               self.s7x + self.circle_radius, self.s7y + self.circle_radius, fill="black"),
        )

    def draw2(self):
        """
        Draw one 2 dots of dice

        :return:  print 2 dots and display it on tkinter popup window
        """
        return (
            canvas.create_oval(self.s1x - self.circle_radius, self.s1y - self.circle_radius,
                               self.s1x + self.circle_radius, self.s1y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6x - self.circle_radius, self.s6y - self.circle_radius,
                               self.s6x + self.circle_radius, self.s6y + self.circle_radius, fill="black"),
        )

    def draw3(self):
        """
        Draw 3  dots of dice

        :return:  print 3 dots and display it on tkinter popup window
        """
        return (
            canvas.create_oval(self.s1x - self.circle_radius, self.s1y - self.circle_radius,
                               self.s1x + self.circle_radius, self.s1y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s7x - self.circle_radius, self.s7y - self.circle_radius,
                               self.s7x + self.circle_radius, self.s7y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6x - self.circle_radius, self.s6y - self.circle_radius,
                               self.s6x + self.circle_radius, self.s6y + self.circle_radius, fill="black")
        )

    def draw4(self):
        """
        Draw one 4 dots of dice

        :return:  print 4 dots and display it on tkinter popup window
        """
        return (
            canvas.create_oval(self.s1x - self.circle_radius, self.s1y - self.circle_radius,
                               self.s1x + self.circle_radius, self.s1y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s3x - self.circle_radius, self.s3y - self.circle_radius,
                               self.s3x + self.circle_radius, self.s3y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s4x - self.circle_radius, self.s4y - self.circle_radius,
                               self.s4x + self.circle_radius, self.s4y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6x - self.circle_radius, self.s6y - self.circle_radius,
                               self.s6x + self.circle_radius, self.s6y + self.circle_radius, fill="black"),

        )

    def draw5(self):
        """
        Draw one 5 dots of dice

        :return:  print 5 dots and display it on tkinter popup window
        """
        return (
            canvas.create_oval(self.s1x - self.circle_radius, self.s1y - self.circle_radius,
                               self.s1x + self.circle_radius, self.s1y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s3x - self.circle_radius, self.s3y - self.circle_radius,
                               self.s3x + self.circle_radius, self.s3y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s4x - self.circle_radius, self.s4y - self.circle_radius,
                               self.s4x + self.circle_radius, self.s4y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s7x - self.circle_radius, self.s7y - self.circle_radius,
                               self.s7x + self.circle_radius, self.s7y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6x - self.circle_radius, self.s6y - self.circle_radius,
                               self.s6x + self.circle_radius, self.s6y + self.circle_radius, fill="black")
        )

    def draw6(self):
        """
        Draw one 6 dots of dice

        :return:  print 6 dots and display it on tkinter popup window
        """
        return (
            canvas.create_oval(self.s1x - self.circle_radius, self.s1y - self.circle_radius,
                               self.s1x + self.circle_radius, self.s1y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s2x - self.circle_radius, self.s2y - self.circle_radius,
                               self.s2x + self.circle_radius, self.s2y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s3x - self.circle_radius, self.s3y - self.circle_radius,
                               self.s3x + self.circle_radius, self.s3y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s4x - self.circle_radius, self.s4y - self.circle_radius,
                               self.s4x + self.circle_radius, self.s4y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s5x - self.circle_radius, self.s5y - self.circle_radius,
                               self.s5x + self.circle_radius, self.s5y + self.circle_radius, fill="black"),
            canvas.create_oval(self.s6x - self.circle_radius, self.s6y - self.circle_radius,
                               self.s6x + self.circle_radius, self.s6y + self.circle_radius, fill="black"),
        )


if __name__ == "__main__":

    while True:
        user_input = input("How many dice do you want to roll? [1-6] ")
        canvas.create_text(10, 15, text="$ python dice.py", font=("Arial", 12), anchor ="w", fill="black")
        canvas.create_text(10, 40, text=f"How many dice do you want to roll? [1-6]   {user_input}", font=("Arial", 12), anchor ="w", fill="black")
        roll = RollDice()
        roll.count(roll.input_validation(user_input))

        # Start the Tkinter event loop
        root.mainloop()

