import random  # Import the random module for random number generation

# Constants
MAX_LINES = 3  # Maximum number of lines to bet on
MAX_BET = 100  # Maximum bet per line
MIN_BET = 1    # Minimum bet per line

ROWS = 3       # Number of rows in the slot machine
COLS = 3       # Number of columns in the slot machine

# Dictionary to keep track of how many of each symbol are available
symbol_count = {
    "A": 2,    # Symbol "A" appears 2 times
    "B": 4,    # Symbol "B" appears 4 times
    "C": 6,    # Symbol "C" appears 6 times
    "D": 8     # Symbol "D" appears 8 times
}

# Dictionary to store the value of each symbol if matched on a line
symbol_value = {
    "A": 5,    # "A" is worth $5 per line
    "B": 4,    # "B" is worth $4 per line
    "C": 3,    # "C" is worth $3 per line
    "D": 2     # "D" is worth $2 per line
}

def deposit():
    # Function to handle user's deposit
    while True:  # Keep asking until a valid amount is entered
        amount = input("What would you like to deposit? $")  # Ask user for deposit
        if amount.isdigit():  # Check if input is a digit
            amount = int(amount)  # Convert to integer
            if amount > 0:  # Ensure deposit is positive
                break  # Exit the loop if valid
            else:
                print("Amount must be greater than 0.")  # Print error for non-positive amount
        else:
            print("Please enter a valid number.")  # Print error for non-digit input
    return amount  # Return the deposited amount

def get_number_of_lines():
    # Function to get number of lines the user wants to bet on
    while True:  # Keep asking until valid number is entered
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")  # Prompt user
        if lines.isdigit():  # Check if input is a digit
            lines = int(lines)  # Convert to integer
            if 1 <= lines <= MAX_LINES:  # Check if within allowed range
                break  # Exit loop if valid
            else:
                print("Enter a valid number of lines.")  # Error for invalid range
        else:
            print("Please enter a number.")  # Error for non-digit input
    return lines  # Return number of lines

def get_bet():
    # Function to get the bet per line from user
    while True:  # Loop until valid input
        amount = input(f"What would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ")  # Prompt
        if amount.isdigit():  # Check if input is a digit
            amount = int(amount)  # Convert to integer
            if MIN_BET <= amount <= MAX_BET:  # Ensure it's in range
                break  # Exit if valid
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")  # Error if not in range
        else:
            print("Please enter a valid number.")  # Error for non-digit
    return amount  # Return bet amount

def get_slot_machine_spin(rows, cols, symbols):
    # Function to generate a slot machine spin
    all_symbols = []  # List to hold all symbols according to their counts
    for symbol, symbol_count_ in symbols.items():  # Loop through symbols
        all_symbols.extend([symbol] * symbol_count_)  # Add symbol the number of times it appears

    columns = []  # List to hold columns of the slot machine
    for col in range(cols):  # Loop for each column
        column = []  # List to hold symbols for current column
        current_symbols = all_symbols[:]  # Copy of all symbols for each column
        for row in range(rows):  # Loop for each row in current column
            value = random.choice(current_symbols)  # Randomly select a symbol
            current_symbols.remove(value)  # Remove selected symbol so it can't appear again in this column
            column.append(value)  # Add selected symbol to the column
        columns.append(column)  # Add completed column to columns list
    return columns  # Return the columns representing the slot machine spin

def print_slot_machine(columns):
    # Function to print the slot machine in a nice way
    for row in range(len(columns[0])):  # Loop through each row (transposed)
        for i, column in enumerate(columns):  # Loop through each column
            if i != len(columns) - 1:  # If not the last column
                print(column[row], end=" | ")  # Print symbol with separator
            else:
                print(column[row], end="")  # Print symbol without separator
        print()  # Newline after each row

def check_winnings(columns, lines, bet, values):
    # Function to check how much the user has won
    winnings = 0  # Track total winnings
    winning_lines = []  # Track which lines won
    for line in range(lines):  # Loop through lines user bet on
        symbol = columns[0][line]  # Get the symbol in first column for this line
        for column in columns:  # Loop through each column in this line
            if column[line] != symbol:  # If any symbol doesn't match, not a win
                break  # Break out of loop if not a win
        else:  # This runs if no break occurred, meaning all symbols matched
            winnings += values[symbol] * bet  # Add winnings for this line
            winning_lines.append(line + 1)  # Track which line won (1-based index)
    return winnings, winning_lines  # Return total winnings and winning lines

def main():
    # Main function to control the game flow
    balance = deposit()  # User deposits money and balance is set
    while True:  # Main game loop, continues until break
        print(f"\nCurrent balance: ${balance}")  # Show current balance
        answer = input("Press Enter to play (q to quit): ")  # Ask if user wants to play
        if answer.lower() == "q":  # If user types 'q', exit game
            break  # Exit the main game loop

        lines = get_number_of_lines()  # Ask user for lines to bet on
        while True:  # Loop to get a valid bet
            bet = get_bet()  # Ask user for bet per line
            total_bet = bet * lines  # Calculate total bet
            if total_bet > balance:  # Check if user has enough money
                print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")  # Error if not enough
            else:
                break  # Valid bet, exit inner loop

        print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")  # Show user bet details

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Spin the slot machine
        print_slot_machine(slots)  # Print the slot machine
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Check winnings
        print(f"You won ${winnings}.")  # Show how much was won this round
        if winnings > 0:  # If there are winning lines
            print(f"You won on lines:", ", ".join(map(str, winning_lines)))  # Show which lines won
        else:
            print("No winning lines this spin.")  # If no lines won

        balance += winnings - total_bet  # Update balance: add winnings, subtract bet

        if balance <= 0:  # If balance is empty or negative
            print("You ran out of money!")  # Inform user
            break  # Exit the main game loop

    print(f"You left with ${balance}")  # Show final balance after game ends

if __name__ == "__main__":  # Check if this is the main script
    main()  # Run the main function
