from enum import Enum
import random
import time


class Option(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class Result(Enum):
    DRAW = "It's a tie!!!"
    USER_WINS = "You Win!!!"
    COMPUTER_WINS = "You Lose!!!"
        

def get_choice_name(choice: int) -> str:
    return Option(choice).name
    
def determine_the_winner(user_choice: int, comp_choice: int) -> str:
    if user_choice == comp_choice:
        return Result.DRAW.value
    elif (
        user_choice > comp_choice
        and user_choice- comp_choice == 1
        or user_choice == Option.ROCK.value
        and comp_choice == Option.SCISSOR.value
    ):
        return Result.USER_WINS.value
    else:
        return Result.COMPUTER_WINS.value

def main():
    while True:
        print("Enter your choice : \n 1 - Rock \n 2 - Paper \n 3 - Scissor")

        user_choice: int
        while True:
            try:
                user_choice = int(input("Enter your choice: "))
                if user_choice < 1 or user_choice > 3:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input! Please enter a valid number")

        comp_choice: int = random.randint(1, 3)
        user_choice_name: str = get_choice_name(user_choice)
        comp_choice_name: str = get_choice_name(comp_choice)
        result = determine_the_winner(user_choice, comp_choice)

        print("\nUser choice is:", user_choice_name)
        print("Computer choice is:", comp_choice_name)
        print(user_choice_name, "vs", comp_choice_name)
        print("Calculating result...")
        time.sleep(3)
        print("\n", result, "\n")
        print("Do you want to play again? (Y/N)")
        
        ans: str
        ans = input().lower()
        if ans == "n":
            break

if __name__ == "__main__":
    main()
