import random

def randomizer():
    return [random.randint(1, 50) for _ in range(6)]

def checker(bet, winning_combination):
    bet_numbers = list(map(int, bet.split()))
    matches = set(bet_numbers) & set(winning_combination)
    return len(matches), matches

winning_combination = randomizer()

print("Welcome to the Lotto Game!")
print("Pick 6 numbers between 1 and 50 (separated by spaces).")

bet = input("Enter your bet: ")

match_count, matched_numbers = checker(bet, winning_combination)

print(f"\nWinning combination: {winning_combination}")
print(f"Your bet: {bet.split()}")

if match_count > 0:
    print(f"Congratulations! You matched {match_count} number(s): {sorted(matched_numbers)}")
else:
    print("Sorry, no matches this time. Better luck next time!")