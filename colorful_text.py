from colorama import Fore, Style

def print_colored_text(text, color):
    """
    Prints the provided text in the specified color.
    
    Args:
        text (str): The text to print.
        color (str): The color name (e.g., 'red', 'green', 'blue').
    """
    colors = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "reset": Style.RESET_ALL,
    }
    color_code = colors.get(color.lower(), Fore.WHITE)  # Default to white if color not found
    print(color_code + text + Style.RESET_ALL)

if __name__ == "__main__":
    # Example usage of the function
    print_colored_text("This is red text!", "red")
    print_colored_text("This is green text!", "green")
    print_colored_text("This is blue text!", "blue")
    print_colored_text("This is yellow text!", "yellow")
    print_colored_text("This is magenta text!", "magenta")
    print_colored_text("This is cyan text!", "cyan")
    print_colored_text("This is white text!", "white")
    print_colored_text("This is default color (black) text!", "black")
