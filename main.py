import random

def randomizer(max_num):
    return sorted(random.sample(range(1, max_num + 1), 6))

def get_user_bet_numbers(max_num):
    numbers = []
    print(f"Enter 6 Bet Numbers between 1 and {max_num}:")
    while len(numbers) < 6:
        try:
            num = int(input(f"Number {len(numbers) + 1}: "))
            if num < 1 or num > max_num:
                print(f"Please enter a Bet Number between 1-{max_num}.")
            elif num in numbers:
                print("Bet number not available")
            else:
                numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a Bet Number.")
    return numbers

def checker(winning_numbers, player_numbers):
    matches = set(winning_numbers) & set(player_numbers)
    if len(matches) == 6:
        return "Jackpot! You've won the lottery!"
    elif len(matches) > 0:
        return f"You've matched {len(matches)} number(s): {sorted(matches)}"
    else:
        return "No matches. Better luck next time!"
    
def get_lotto_range(lotto_type):
    return int(lotto_type.split('/')[1])

# Main game loop
while True:
    # Lotto type selection
    lotto_types = ['6/58', '6/55', '6/49', '6/45', '6/42']
    print("Choose a lotto type:")
    for i, lotto in enumerate(lotto_types, 1):
        print(f"{i}. {lotto}")
    
    while True:
        try:
            choice = int(input("Choose Lotto Type (1-5): "))
            if 1 <= choice <= 5:
                lotto_type = lotto_types[choice - 1]
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number between 1 and 5.")
    
    max_num = get_lotto_range(lotto_type)
    print(f"\nYou chose {lotto_type}")
    
    # Get user's numbers
    print("\nEnter your 6 numbers:")
    player_numbers = get_user_bet_numbers(max_num)
    
    # Generate winning numbers
    winning_numbers = randomizer(max_num)
    
    # Display results
    print(f"\nWinning numbers: {winning_numbers}")
    print(f"Your Bet numbers: {player_numbers}")
    print(checker(winning_numbers, player_numbers))
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        break

print("Thanks for playing!")