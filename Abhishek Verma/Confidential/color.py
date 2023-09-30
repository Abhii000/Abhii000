from colorama import init, Fore, Back, Style

def main():
    # Initialize colorama
    init()
    
    # Print colored text
    print(Fore.RED + "This is red text")
    print(Fore.YELLOW + "This is yellow text")
    print(Fore.GREEN + "This is green text")
    print(Fore.CYAN + "This is cyan text")
    print(Fore.BLUE + "This has a blue background")
    
    print(Style.RESET_ALL)  # Reset colors and styles

if __name__ == "__main__":
    main()
