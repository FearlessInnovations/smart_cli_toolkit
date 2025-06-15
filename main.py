# Import standard library for parsing arguments
import argparse

def greet(args):
    """
    Handles the logic for the 'greet' command.
    """
    print(f"Hello, {args.name}! The Journey has begun.")

def main():
    """
    This is the main function of our program.
    It now accepts and processes command-line arguments.
    """

    # The description will be showen to users if they ask for help.
    parser = argparse.ArgumentParser(description="A smart command-line toolkit by FearlessInnovations.")
    # This is the special object that will hold sub-commmands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Create the parser for the "greet" command ---
    parser_greet = subparsers.add_parser("greet", help="prints a personalized greeting.")
    # We add a '--name' argument. We give it a default value and a help message.
    parser_greet.add_argument("--name", default="Innovator", help="The name to greet.")

    # --- Add more command parsers here in the future ---
    # Example: parser_weather = subparsers.add_parser("weather, help="Gets the weather.")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # We check which command the user ran and call the appropriate function
    if args.command == "greet":
        greet(args)
    # Add more commmand checks here in the future
    # elif args.commmand == "weather":
    #     get_weather(args)
    else:
        # If no command was provided, print the help message
        parser.print_help()


if __name__ == "__main__" :
    main()