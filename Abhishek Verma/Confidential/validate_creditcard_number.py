import re

def is_valid_credit_card(card):
    # Define the regex pattern for a valid credit card
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    
    # Check if the card matches the pattern
    if not re.match(pattern, card):
        return False
    
    # Remove hyphens to check for consecutive repeating digits
    card = card.replace("-", "")
    
    # Check for consecutive repeating digits
    for i in range(len(card) - 3):
        if card[i] == card[i + 1] == card[i + 2] == card[i + 3]:
            return False
    
    return True

# Read the number of credit card entries
n = int(input().strip())

# Read and validate each credit card number
for _ in range(n):
    card_number = input().strip()
    if is_valid_credit_card(card_number):
        print("Valid")
    else:
        print("Invalid")
