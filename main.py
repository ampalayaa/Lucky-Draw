import random

def randomizer(max_num):
    return sorted(random.sample(range(1, max_num + 1), 6))

def get_user_bet_numbers(max_num):
    numbers = []
    print(f"Enter 6 numbers between 1 and {max_num}:")
    while len(numbers) < 6:
        try:
            num = int(input(f"Number {len(numbers) + 1}: "))
            if num < 1 or num > max_num:
                print(f"Please enter a number between 1-{max_num}.")
            elif num in numbers:
                print("Bet number not available")
            else:
                numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return numbers

def checker(bet, winning_combination):
    matches = set(bet) & set(winning_combination)
    return len(matches), matches

max_num = 50
winning_combination = randomizer(max_num)

print("Welcome to the Lotto Game!")
print("Pick 6 numbers between 1 and 50 (separated by spaces).")

bet = get_user_bet_numbers(max_num)

match_count, matched_numbers = checker(bet, winning_combination)

print(f"\nWinning combination: {winning_combination}")
print(f"Your bet: {bet}")

if match_count > 0:
    print(f"Congratulations! You matched {match_count} number(s): {sorted(matched_numbers)}")
else:
    print("Sorry, no matches this time. Better luck next time!")