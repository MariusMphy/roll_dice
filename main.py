"""
Rollin Dice
Input:
    - user enters amount of dices (from 1 to 6) to roll

Output:
    - display drawing of rolled dices
"""


class Main:
    def __init__(self):
        self.number = 0

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


if __name__ == "__main__":
    rd = Main()
    user_input = input("How many dice do you want to roll? [1-6] ")
    rd.input_validation(user_input)

    print(rd.number)



