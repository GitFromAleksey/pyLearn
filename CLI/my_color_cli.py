from colorama import init, Fore, Back, Style

# Stile:
# Fore - цвет шрифта
# Back - цвет фона

def main():
    init()
    print(Style.DIM + Fore.GREEN + Back.MAGENTA + 'Green' + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.BLACK + Back.WHITE + 'White' + Style.RESET_ALL)
    print(Style.NORMAL + Fore.BLUE + Back.YELLOW + 'Blue' + Style.RESET_ALL)

if __name__ == '__main__':
    main()