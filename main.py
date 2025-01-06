from enum import Enum
import random


class Option(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3


class Result(Enum):
    DRAW = 1
    USER_WINS = 2
    COMPUTER_WINS = 3


def rock_paper_scissor_game():
    while True:
        print("Enter your choice : \n 1 - Rock \n 2 - Paper \n 3 - Scissor")

        # Take the input from user
        # and Handle user input if out of options
        choice: int
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 3:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input! Please enter a valid number")

        # Initialize values of user choice
        choice_name: str
        if choice == Option.Rock.value:
            choice_name = Option.Rock.name
        elif choice == Option.Paper.value:
            choice_name = Option.Paper.name
        else:
            choice_name = Option.Scissor.name

        # Print user choices
        print("User choice is:", choice_name)
        print("Now it's Computer's Turn:")

        # Computer choose any value 1 to 3
        comp_choice: int
        comp_choice = random.randint(1, 3)

        # Initialize values of computer choices
        comp_choice_name: str
        if comp_choice == Option.Rock.value:
            comp_choice_name = Option.Rock.name
        elif comp_choice == Option.Paper.value:
            comp_choice_name = Option.Paper.name
        else:
            comp_choice_name = Option.Scissor.name

        # Print computer choices
        print("Computer choice is:", comp_choice_name)

        # Determine the winner
        print(choice_name, "vs", comp_choice_name)
        result: str
        if choice == comp_choice:
            result = Result.DRAW.name
        elif (
            choice > comp_choice
            and choice - comp_choice == 1
            or choice == Option.Rock.value
            and comp_choice == Option.Scissor.value
        ):
            result = Result.USER_WINS.name
        else:
            result = Result.COMPUTER_WINS.name

        # Print the result
        if result == Result.DRAW.name:
            print("<== It's a tie! ==>")
        elif result == Result.USER_WINS.name:
            print("<==User Wins! ==>")
        else:
            print("<==Computer Wins! ==>")

        # Ask user wanna play again?
        print("Do you want to play again? (Y/N)")
        ans: str
        ans = input().lower()
        if ans == "n":
            break


def main():
    # call the function
    rock_paper_scissor_game()


if __name__ == "__main__":
    main()
