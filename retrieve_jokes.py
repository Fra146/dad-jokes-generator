import json
from requests import get
DEFAULT_URL = 'https://raw.githubusercontent.com/wesbos/dad-jokes/master/readme.md'
url = input('Get jokes from URL [default: ...wesbos/dad-jokes...]: ') or DEFAULT_URL


r = get(url)
raw = r.text
print(f'The jokes were retrieved [{r.status_code} {r.reason}]')
jokes = []


if url == DEFAULT_URL:
    rjokes = raw.split('---')
    del rjokes[0]
    del rjokes[0]
    del rjokes[-1]
    for joke in rjokes:
        # replace * with nothing
        joke = joke.replace('*', '')
        # replace \n with space but not if there are two \n
        joke = joke.replace('\n\n', '\n')
        joke = joke.replace('\n', ' ')
        joke = joke.replace('\u2019', '\'')
        joke = joke.strip()
        joke.replace('```', '')
        divide_question_and_answer = joke.split('A:')
        question = divide_question_and_answer[0]
        try:
            answer = divide_question_and_answer[1]
            question = question.replace('Q: ', '')
            question = question.strip()
            answer = answer.strip()
            jokes.append([question, answer])
        except IndexError:
            question = question.replace('Q: ', '')
            question = question.strip()
            jokes.append([question])


else:
    rjokes = raw.split('\n')
    for joke in rjokes:
        jokes.append([joke])


print('Saving jokes to jokes.json')
with open('jokes.json', 'w') as f:
    json.dump(jokes, f)

print('Jokes saved!')