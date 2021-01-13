# probs_bank.py

import random

def simple_addition():
    var_x = random.randint(1, 1000)
    var_y = random.randint(1, 1000)
    equation = f'{var_x} + {var_y}'
    true_answer = var_x + var_y
    while True:
        print(f'What is {equation}?')
        try:
            user_answer = int(input())
        except ValueError:
            print('Invalid input. Try again.')
            continue
        else:
            break
    result = user_answer == true_answer
    report = {
        'equation': equation,
        'true_answer': true_answer,
        'user_answer': user_answer,
        'result': result
    }
    return report

def simple_subtraction():
    var_x = random.randint(1, 1000)
    var_y = random.randint(1, 1000)
    equation = f'{var_x} - {var_y}'
    true_answer = var_x - var_y
    while True:
        print(f'What is {equation}?')
        try:
            user_answer = int(input())
        except ValueError:
            print('Invalid input. Try again.')
            continue
        else:
            break
    result = user_answer == true_answer
    report = {
        'equation': equation,
        'true_answer': true_answer,
        'user_answer': user_answer,
        'result': result
    }
    return report