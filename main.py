import json
import random
from coolprint import coolprint as cprint

def get_next_joke():
    # Open the jokes.json file
    with open('jokes.json', 'r') as file:
        jokes = json.load(file)
    
    # Check if there are any jokes left
    if len(jokes) == 0:
        cprint('No more jokes found')
        return False
    
    # Select a random joke
    joke = random.choice(jokes)
    
    # Print the joke
    if len(joke) == 2:
        cprint(f"\033[91m{joke[0]}\033[0m ")
        input()
        cprint(f"\033[96m{joke[1]}")
        cprint('\n\033[0m')
    else:
        cprint(f"\033[92m{joke[0]}")
        cprint('\n\033[0m')
    
    # Remove the joke from the list
    input()

def check_config():
    try:
        # Open the jokes.json file
        with open('jokes.json', 'r') as file:
            jokes = json.load(file)
            
            # Check if the jokes.json file is empty
            if not jokes:
                print('jokes.json is empty')
                return False
            return True
    except FileNotFoundError:
        print('jokes.json not found')
        return False
    except json.JSONDecodeError:
        print('jokes.json is not a valid JSON file')
        return False

def main():
    cprint('\033[1mWelcome to \033[4mProgramming Dad Jokes Generator\033[0m')

    # Check the configuration
    if not check_config():
        return
    
    cprint('Jokes loaded!')
    input('Generate a joke? (Press Enter to continue)')
    cprint('\n\n')
    
    # Loop to generate jokes until there are no more left
    while True:
        if get_next_joke() == False:
            break
    
    cprint('Goodbye!')

if __name__ == '__main__':
    main()