import random
import time

more = True

while more:
    start = time.perf_counter()
    correct_answer = 0
    incorrect_answer = 0

    for _ in range(5):
        first = random.randint(1, 9)
        second = random.randint(1, 9)

        print(f'{first} x {second} = ?')
        answer = input('Please enter your answer: ')

        while not answer.isdigit():
            print('Please enter numbers only.')
            answer = input('Please enter your answer: ')

        if answer == str(first * second):
            correct_answer += 1
            print('Correct!')
        else:
            print('Incorrect.')
            incorrect_answer += 1

    end = time.perf_counter()

    print(f'\nResults:')
    print(f'Correct answers: {correct_answer}/5')
    print(f'Incorrect answers: {incorrect_answer}/5')
    print(f'Time taken: {round(end - start, 2)} seconds')

    more = input('\nWould you like to play again? (y/n): ').lower()
    if more == 'y':
        more = True
    else:
        more = False
        
    
        
        
    
