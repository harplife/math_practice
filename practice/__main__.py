# __main__.py

import random, sys, signal
import pathlib
import json
from datetime import datetime
from practice import probs_bank as pb

def signal_handler(signal, frame):
    print('\nProgram exiting gracefully.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def insert_coin(end_report):
    while True:
        print('Would you like to continue? (yes/no)')
        user_cont = input()
        if user_cont.lower() == 'yes':
            break
        elif user_cont.lower() == 'no':
            print('Bye bye~')
            # TODO: print score, then wait for user key press to exit
            # TODO: generate report (problems and answers) and save to file
            name = end_report['name']
            tried = end_report['tried']
            correct = end_report['correct']
            grade = correct*100/tried
            end_report['grade'] = f'{grade:.0f}%'
            report_path = pathlib.Path('./record/')
            report_path.mkdir(parents=True, exist_ok=True)
            now = datetime.now()
            dt = now.strftime('%m%d%Y_%H%M%S')
            report_fn = f'report_{name}_{dt}.json'
            report_fpath = report_path / report_fn
            with report_fpath.open('w', encoding='utf-8') as f:
                json.dump(end_report, f, ensure_ascii=False, indent=4)
            sys.exit(0)
        else:
            print('Invalid input.')
            continue

def main():
    print('What is your name?')
    name = input()
    print(f'Hello, {name}. Do some math.')
    game_time = True
    tried = 0
    correct = 0
    end_report = {}
    end_report['name'] = name
    end_report['problems'] = {}
    end_report['tried'] = tried
    end_report['correct'] = correct
    while game_time:
        tried += 1
        equations = [pb.simple_addition, pb.simple_subtraction]
        chosen = random.choice(equations)
        report = chosen()
        end_report['problems'][f'problem_{tried}'] = report
        if report['result']:
            print('You are correct!')
            correct += 1
            print(f'Current score: {correct}/{tried}')
            end_report['tried'] = tried
            end_report['correct'] = correct
            insert_coin(end_report)
        else:
            print('You are incorrect!')
            print(f'Current score: {correct}/{tried}')
            end_report['tried'] = tried
            end_report['correct'] = correct
            insert_coin(end_report)

if __name__=="__main__":
    main()