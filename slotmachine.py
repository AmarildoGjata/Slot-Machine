import random

def spin_row():
    """Generate a row of three random slot machine symbols."""
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    """Display the slot machine row with formatting."""
    print('\n***********')
    print(' | '.join(row))
    print('***********\n')

def get_payout(row, bet):
    """Calculate payout based on the row and bet amount."""
    payouts = {
        '🍒': 3,
        '🍉': 5,
        '🍋': 7,
        '🔔': 10,
        '⭐': 50
    }
    if row[0] == row[1] == row[2] and row[0] in payouts:
        return bet * payouts[row[0]]
    return 0

def main():
    """Run the slot machine game."""
    balance = 100
    print('*************************')
    print(' Welcome to Python Slots ')
    print(' Symbols: 🍒 🍉 🍋 🔔 ⭐ ')
    print('*************************')

    while balance > 0:
        print(f"\nCurrent Balance: ${balance:.2f}")
        while True:
            try:
                bet = input("Place your bet amount: ")
                bet = float(bet) 
                if bet <= 0:
                    print("Bet must be greater than 0.")
                    continue
                if bet > balance:
                    print("Insufficient balance.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout:.2f}!")
        else:
            print("You lost this round.")
        balance += payout

        while True:
            play_again = input("Do you want to spin again? (Y/N): ").strip().lower()
            if play_again in ['y', 'n']:
                break
            print("Please enter 'Y' or 'N'.")
        
        if play_again == 'n':
            print(f"\nGame Over! Your final balance is ${balance:.2f}")
            break

if __name__ == "__main__":
    main()