def wrapper(f):
    def fun(l):
        # Standardize and format the phone numbers
        formatted_numbers = []
        for number in l:
            # Remove any prefixes and leading zeros
            number = number.lstrip('0').lstrip('+')
            # Add '+91' prefix and format
            formatted_number = '+91 ' + number[-10:-5] + ' ' + number[-5:]
            formatted_numbers.append(formatted_number)
        
        # Sort the formatted phone numbers
        sorted_numbers = sorted(formatted_numbers)
        
        # Call the original function with the sorted numbers
        f(sorted_numbers)
    
    return fun

@wrapper
def sort_phone(l):
    # The original function just prints the sorted numbers
    print(*l, sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
