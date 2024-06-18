from coolprint import coolprint as cprint
import json
import random


def get_next_line():
    with open('jokes.json', 'r') as f:
        jokes = json.load(f)
    
    # get a random joke
    if len(jokes) == 0:
        cprint('No more jokes found')
        return False
    
    joke = random.choice(jokes)
    if len(joke) == 2:
        cprint(f"\033[91m{joke[0]}\033[0m ")
        input()
        cprint(f"\033[96m{joke[1]}")
        cprint('\n\033[0m')
    else:
        cprint(f"\033[92m{joke[0]}")
        cprint('\n\033[0m')
    jokes.pop(jokes.index(joke))
    input()

def check_config():
    try:
        with open('jokes.json', 'r') as f:
            jokes = json.load(f)
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

    if not check_config():
        return
    cprint('Jokes loaded!')
    cprint('\n\n\n')
    input('Generate a joke? (Press Enter to continue)')
    cprint('\n\n\n')
    while True:
        if get_next_line() == False:
            break
    cprint('Goodbye!')


if __name__ == '__main__':
    main()