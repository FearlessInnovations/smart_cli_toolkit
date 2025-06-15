# Import standard library for parsing arguments
import argparse

def main():
    """
    This is the main function of our program.
    It now accepts and processes command-line arguments.
    """

    # The description will be showen to users if they ask for help.
    parser = argparse.ArgumentParser(description="A smart command-line toolkit by FearlessInnovations.")

    # We add a '--name' argument. We give it a default value and a help message.
    parser.add_argument("--name", default="Innovator", help="The name to greet.")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # We use an f-string for clean and easy-to-read formatting.
    print(f"Hello, {args.name}! The journey has begun.")

if __name__ == "__main__" :
    main()