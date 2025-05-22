import random


def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']
    return [random.choice(symbols)for _ in range(3)]

def print_row(row):
     print('***********')
     print('  '.join(row))
     print('***********')

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0]=='🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 50
    return 0
    

def main():
    balance = 100
    
    print('***********************')
    print('Welcome to Python Slots')
    print('Symbols:🍒🍉🍋🔔⭐')
    print('***********************')
    
    while balance > 0:
        print (f"Current Balance:${balance}")
        bet = int(input("Place your bet amount:"))
        
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("Spining...\n")    
        print_row(row)
        
        payout = get_payout(row,bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print(f"You lost this round")
        
        balance += payout
        
        play_again = input("Do you want to spin again?(Y/N):")
        if play_again != 'y':
            print(f"Game Over! Your final balance is ${balance}")
            break
        

if __name__ == "__main__":
    main()