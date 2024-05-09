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
    # Check if any row or column has all X's
    row_bingo = sum(rows) >= 5
    col_bingo = sum(cols) >= 5
    return row_bingo or col_bingo


def mark_number_in_all_cards(users_cards, number):
    for card in users_cards:
        for i in range(5):
            for j in range(5):
                if card[i][j] == number:
                    card[i][j] = 'X'
                    return  # Only mark one occurrence of the number per card

def main():
    init()  # Initialize colorama
    clear_screen()
    print("Welcome to Bingo Game!")
    while True:
        num_users = int(input("Enter the number of users: "))

        # Generate bingo cards for each user
        users_cards = [generate_bingo_card() for _ in range(num_users)]

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
