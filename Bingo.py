import random
import os
from colorama import init, Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input_for_card():
    card = []
    print("Enter your numbers for the Bingo card:")
    for i in range(5):
        column = []
        for j in range(5):
            while True:
                try:
                    num = int(input(f"Enter number for row {i+1}, column {j+1} (1-25): "))
                    if 1 <= num <= 25 and num not in column and not any(num in col for col in card):  # Check if number is within range, not in same column, and not in same row
                        column.append(num)
                        break
                    elif num in column:
                        print("Number already used in this column. Please enter a different number.")
                    elif any(num in col for col in card):
                        print("Number already used in this row. Please enter a different number.")
                    else:
                        print("Please enter a valid number between 1 and 25 that hasn't been used already.")
                except ValueError:
                    print("Please enter a valid number.")
        card.append(column)
        print("\nUpdated Bingo Card:")
        print_bingo_card(card)
    return card

def generate_bingo_card():
    print("\nGenerating random numbers for the Bingo card:")
    card = []
    nums = random.sample(range(1, 26), 25)
    for i in range(5):
        column = nums[i*5: (i+1)*5]
        card.append(column)
    return card

def print_bingo_card(card, chosen_number=None, current_user_idx=None):
    print("┌────┬────┬────┬────┬────┐")
    print("│  B │  I │  N │  G │  O │")
    print("├────┼────┼────┼────┼────┤")
    for i in range(len(card)):  # Adjust loop range here
        for j in range(5):
            if chosen_number is not None and i == chosen_number[0] and j == chosen_number[1]:
                if current_user_idx is not None:
                    card[i][j] = 'X'
                    print(f"│ {Fore.YELLOW}X {Style.RESET_ALL}", end=" ")
                else:
                    print(f"│ {Fore.YELLOW}X {Style.RESET_ALL}", end=" ")
            elif card[i][j] == 'X':
                print(f"│ {Fore.YELLOW}X {Style.RESET_ALL}", end=" ")
            elif (i, j) == chosen_number:
                print(f"│ {Fore.GREEN}{card[i][j]:2d}{Style.RESET_ALL}", end=" ")
            else:
                print(f"│ {card[i][j]:2d}", end=" ")
        print("│")
        print("├────┼────┼────┼────┼────┤")
    print("└────┴────┴────┴────┴────┘")

def check_bingo(card):
    # Check rows
    rows = [all(cell == 'X' for cell in row) for row in card]
    # Check columns
    cols = [all(card[j][i] == 'X' for j in range(5)) for i in range(5)]
    # Check if any row or column has all X's
    print("rows", rows)
    print("cols", cols)

    print("sum(rows)", sum(rows))
    print("sum(cols)", sum(cols))

    row_bingo = sum(rows) >= 5
    col_bingo = sum(cols) >= 5

    print("row_bingo", row_bingo)
    print("col_bingo", col_bingo)

    print("ttl ", sum(rows) + sum(rows))

    return sum(rows) + sum(rows) >=5

def mark_number_in_all_cards(users_cards, number):
    for card in users_cards:
        for i in range(5):
            for j in range(5):
                if card[i][j] == number:
                    card[i][j] = 'X'

def main():
    init()  # Initialize colorama
    clear_screen()
    print("Welcome to Bingo Game!")
    while True:
        # Ask for a valid number of users input from the user
        while True:
            try:
                num_users = int(input("Enter the number of users: "))
                if num_users > 0:
                    break
                else:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        # Ask each user if they want to generate a random card or enter their own numbers
        users_cards = []
        for idx in range(num_users):
            print(f"\nUser {idx + 1}, do you want to generate a random Bingo card or enter your own numbers?")
            while True:
                choice = input("Enter 'random' for random card or 'enter' to enter your own numbers: ").lower()
                if choice == 'random' or choice == 'enter':
                    break
                else:
                    print("Please enter either 'random' or 'enter'.")

            if choice == 'random':
                users_cards.append(generate_bingo_card())
            else:
                users_cards.append(get_user_input_for_card())

        # Reveal all users' bingo cards
        print("\nRevealing all users' bingo cards:")
        for idx, card in enumerate(users_cards):
            print(f"\nBingo Card for User {idx + 1}:")
            print_bingo_card(card)

        # Main game loop
        while True:
            for user_idx in range(num_users):
                print(f"\nUser {user_idx + 1}, it's your turn!")
                input("Press Enter to continue...")

                # Ask for a valid number input from the user
                while True:
                    try:
                        chosen_number = int(input(f"\nEnter the number you want to mark (1-25): "))
                        if 1 <= chosen_number <= 25:
                            break
                        else:
                            print("Please enter a number between 1 and 25.")
                    except ValueError:
                        print("Please enter a valid number.")

                # Mark the chosen number in all cards
                mark_number_in_all_cards(users_cards, chosen_number)

                clear_screen()
                print("\nUpdated bingo cards after marking the number:")
                for idx, card in enumerate(users_cards):
                    print(f"\nBingo Card for User {idx + 1}:")
                    print_bingo_card(card)

                # Check if anyone has bingo
                for idx, card in enumerate(users_cards):
                    if check_bingo(card):
                        print(f"\nBingo! User {idx + 1} wins!")
                        break
                else:
                    continue
                break

            else:
                continue
            break

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
        clear_screen()

if __name__ == "__main__":
    main()
