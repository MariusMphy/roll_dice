"""
Rollin Dice
Input:
    - user enters amount of dices (from 1 to 6) to roll

Output:
    - display drawing of rolled dices
"""


class Main:
    def __init__(self, number: int):
        self.number = number


if __name__ == "__main__":
    user_input = int(input("How many dice do you want to roll? [1-6] "))
    roll_dice = Main(user_input)
    print(roll_dice.number)


