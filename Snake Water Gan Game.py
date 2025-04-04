import random
from colorama import init, Fore, Style
from tqdm import tqdm
import time

init(autoreset=True)  # Initialize colorama

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + """
    ╔══════════════════════════════════════════════════╗
    ║             SNAKE WATER GUN GAME                 ║
    ║                                                  ║
    ║       Can you beat the computer? 🎮              ║
    ╚══════════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def move_to_string(move):
    return {0: "🐍 Snake", 1: "💧 Water", 2: "🔫 Gun"}[move]

def check(comp, user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
    return 1

def get_valid_move():
    while True:
        try:
            print(Fore.YELLOW + "\nChoose your move:")
            print("0 - 🐍 Snake")
            print("1 - 💧 Water")
            print("2 - 🔫 Gun")
            user = int(input(Fore.WHITE + "Enter your choice: "))
            if user in [0, 1, 2]:
                return user
            print(Fore.RED + "Invalid choice! Please enter 0, 1, or 2.")
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")

def main():
    print_banner()
    player_score = computer_score = 0
    
    while True:
        print(Fore.BLUE + "\n" + "═" * 50)
        print(Fore.GREEN + f"Score - You: {player_score} | Computer: {computer_score}")
        print(Fore.BLUE + "═" * 50)
        
        comp = random.randint(0, 2)
        user = get_valid_move()
        
        print("\nProcessing move", end='')
        for _ in range(3):
            print(".", end='', flush=True)
            time.sleep(0.3)
        print("\n")
        
        print(Fore.CYAN + f"Your move: {move_to_string(user)}")
        print(Fore.YELLOW + f"Computer's move: {move_to_string(comp)}")
        
        score = check(comp, user)
        if score == 0:
            print(Fore.BLUE + "\n🤝 It's a draw!")
        elif score == -1:
            print(Fore.RED + "\n❌ You Lose!")
            computer_score += 1
        else:
            print(Fore.GREEN + "\n✨ You Won!")
            player_score += 1
            
        x = input(Fore.YELLOW + "\nPress 'Q' to quit or any other key to play again: ").lower()
        if x == 'q':
            print(Fore.GREEN + "\nFinal Score:")
            print(f"You: {player_score} | Computer: {computer_score}")
            print(Fore.CYAN + "\nThanks for playing! 👋\n")
            
            print("Closing game", end='')
            for _ in tqdm(range(5), desc="Closing", ncols=75):
                time.sleep(0.1)
            break

if __name__ == "__main__":
    main()
