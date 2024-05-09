# Install this before run ---> pip install colorama

import random
import os
from colorama import init, Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_bingo_card():
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
    for i in range(5): 
        for j in range(5):
            if chosen_number is not None and card[j][i] == chosen_number:
                if current_user_idx is not None:
                    card[j][i] = 'X'
                    print(f"│ {Fore.YELLOW}X {Style.RESET_ALL}", end=" ")
                else:
                    print(f"│ {Fore.YELLOW}X {Style.RESET_ALL}", end=" ")
            elif card[j][i] == 'X':
                print(f"│ {Fore.YELLOW}X {Style.RESET_ALL}", end=" ")
            else:
                print(f"│ {card[j][i]:2d}", end=" ")
        print("│")
        print("├────┼────┼────┼────┼────┤")
    print("└────┴────┴────┴────┴────┘")

def check_bingo(card):
    # Check rows
    rows = [all(cell == 'X' for cell in row) for row in card]
    # Check columns
    cols = [all(card[j][i] == 'X' for j in range(5)) for i in range(5)]
    # Check diagonals
    diagonals = [all(card[i][i] == 'X' for i in range(5)), all(card[i][4-i] == 'X' for i in range(5))]
    return rows, cols, diagonals

def update_title_letters(title, rows, cols):
    print("Rows:", rows)
    print("Cols:", cols)
    if all(rows) or all(cols):
        for i, row_complete in enumerate(rows):
            print("Row", i, "Complete:", row_complete)
            if row_complete:
                if i < len(title):
                    title[i] = 'X'
        for i, col_complete in enumerate(cols):
            print("Col", i, "Complete:", col_complete)
            if col_complete:
                if i < len(title):
                    title[i + 5] = 'X'
        if all(rows):
            title[0] = 'X'
        if all(cols):
            title[1] = 'X'
    print("Updated Title:", title)
    return title


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
        num_users = int(input("Enter the number of users: "))

        # Generate bingo cards for each user
        users_cards = [generate_bingo_card() for _ in range(num_users)]
        # Initialize title letters
        title = ['B', 'I', 'N', 'G', 'O']

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

                chosen_number = int(input("\nEnter the number you want to mark (1-25): "))

                # Mark the chosen number in all cards
                mark_number_in_all_cards(users_cards, chosen_number)

                clear_screen()
                print("\nUpdated bingo cards after marking the number:")
                for idx, card in enumerate(users_cards):
                    print(f"\nBingo Card for User {idx + 1}:")
                    print_bingo_card(card, chosen_number)

                # Check if anyone has bingo
                for idx, card in enumerate(users_cards):
                    rows, cols, diagonals = check_bingo(card)
                    title = update_title_letters(title, rows, cols)
                    if all(cell == 'X' for cell in title):
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
