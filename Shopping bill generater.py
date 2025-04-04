import time
from datetime import datetime
import random
from colorama import init, Fore, Back, Style
from tqdm import tqdm
import sys
import time

init(autoreset=True)  # Initialize colorama

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + """
    ╔══════════════════════════════════════════════════╗
    ║             SHOPPING MALL BILLING                ║
    ║                                                  ║
    ║  Your One-Stop Shop for All Your Needs!          ║
    ╚══════════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def loading_spinner():
    chars = "/—\\|"
    for char in chars:
        sys.stdout.write('\r' + Fore.YELLOW + 'Processing ' + char)
        sys.stdout.flush()
        time.sleep(0.1)

def print_section(title):
    print(Fore.BLUE + "\n" + "═" * 50)
    print(Fore.WHITE + Style.BRIGHT + f"  {title}")
    print(Fore.BLUE + "═" * 50 + "\n")

def Time():
    import time
    timestamp = int(time.strftime('%H'))
    greeting = "\n"
    if 4 <= timestamp <= 10:
        greeting += Fore.YELLOW + "🌅 Good Morning Sir" + Style.BRIGHT + " 🥱"
    elif 10 < timestamp <= 15:
        greeting += Fore.YELLOW + "☀️ Good Afternoon Sir" + Style.BRIGHT + " 🤨"
    elif 15 < timestamp <= 20:
        greeting += Fore.MAGENTA + "🌅 Good Evening Sir" + Style.BRIGHT + " 🫡"
    else:
        greeting += Fore.BLUE + "🌙 Good Night Sir" + Style.BRIGHT + " 😴"
    print(greeting + Style.RESET_ALL)

def validate_price(price_str):
    try:
        price = float(price_str)
        return price if price >= 0 else None
    except ValueError:
        return None

def calculate_discount(total):
    if total >= 5000:
        return total * 0.10
    elif total >= 3000:
        return total * 0.05
    return 0

def generate_receipt_number():
    return f"BILL-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"

# Initialize variables
sum = 0
item_prize = {}
item_qty = {}
receipt_no = generate_receipt_number()

# Print welcome message
print_banner()
Time()
print(Fore.GREEN + "\n\tWelcome to our shopping mall\n")

print_section("ITEM ENTRY")
# Item input loop
while True:
    print(Fore.CYAN + "─" * 40)
    item_input = input(Fore.YELLOW + "Enter the Item name or Q for quit: ").capitalize()
    if item_input == "Q":
        break
    
    qty = input(Fore.YELLOW + f"Enter quantity for {item_input}: ")
    try:
        qty = int(qty)
        if qty <= 0:
            print(Fore.RED + "Invalid quantity! Please enter a positive number.")
            continue
    except ValueError:
        print(Fore.RED + "Invalid quantity! Please enter a number.")
        continue

    while True:
        price_input = input(Fore.YELLOW + "Enter the price of this item: ")
        price = validate_price(price_input)
        if price is not None:
            break
        print(Fore.RED + "Invalid price! Please enter a valid positive number.")

    item_prize[item_input] = price
    item_qty[item_input] = qty
    sum += price * qty
    print(Fore.GREEN + "✓ Item added successfully!")

# Show processing animation
print_section("GENERATING BILL")
for _ in range(3):
    loading_spinner()

# Calculate totals
discount = calculate_discount(sum)
subtotal = sum - discount
gst = subtotal * 0.18
final_total = subtotal + gst

# Print bill with enhanced formatting
print_section("FINAL BILL")
print(Fore.BLUE + "╔" + "═"*50 + "╗")
print(Fore.BLUE + f"║{Fore.WHITE} Receipt No: {receipt_no:<37}{Fore.BLUE}║")
print(Fore.BLUE + f"║{Fore.WHITE} Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<43}{Fore.BLUE}║")
print(Fore.BLUE + "╚" + "═"*50 + "╝\n")

print(Fore.CYAN + f"{'Item':<20}{'Qty':>8}{'Price':>10}{'Total':>12}")
print(Fore.BLUE + "─"*50)

for item in item_prize:
    qty = item_qty[item]
    price = item_prize[item]
    total = qty * price
    print(f"{Fore.WHITE}{item:<20}{Fore.YELLOW}{qty:>8}{price:>10.2f}{total:>12.2f}")

print(Fore.BLUE + "─"*50)
print(f"{Fore.WHITE}{'Subtotal':<38}{sum:>12.2f}")
print(f"{Fore.WHITE}{'Discount':<38}{discount:>12.2f}")
print(f"{Fore.WHITE}{'GST (18%)':<38}{gst:>12.2f}")
print(Fore.BLUE + "═"*50)
print(f"{Fore.WHITE}{'Final Total':<38}{final_total:>12.2f}")
print(Fore.BLUE + "═"*50)

# Show final message with progress bar
print("\n" + Fore.GREEN + "Processing payment", end='')
for _ in tqdm(range(10), desc="Finalizing", ncols=75):
    time.sleep(0.1)

print(Fore.GREEN + Style.BRIGHT + "\n✨ Thank you for shopping with us! ✨")
print(Fore.CYAN + "Please visit again!\n")