from random import randint

level_descriptions = ['1 - simple operations with numbers 2-9', '2 - integral squares of 11-29']

operators = ['+', '-', '*']

correct_answers = 0

try:
    print('Which level do you want? Enter a number:')
    print(level_descriptions[0])
    print(level_descriptions[1])
    level = int(input())
    assert level == 1 or level == 2
except:
    print('Incorrect format.')

for _ in range(5):
    answer = ''

    oper = randint(0, 2)

    if level == 1:
        number_1 = randint(2, 9)
        number_2 = randint(2, 9)

        if operators[oper] == '+':
            result = number_1 + number_2

            print(f'{number_1} + {number_2}')

            while answer == '':
                try:
                    answer = int(input())

                    assert answer == result
                    print('Right!')
                    correct_answers += 1
                except ValueError:
                    print('Incorrect format.')
                    answer = ''
                except AssertionError:
                    print('Wrong!')
                    answer = ''
                    break
        elif operators[oper] == '-':
            result = number_1 - number_2

            print(f'{number_1} - {number_2}')

            while answer == '':
                try:
                    answer = int(input())

                    assert answer == result
                    print('Right!')
                    correct_answers += 1
                except ValueError:
                    print('Incorrect format.')
                    answer = ''
                except AssertionError:
                    print('Wrong!')
                    answer = ''
                    break
        elif operators[oper] == '*':
            result = number_1 * number_2

            print(f'{number_1} * {number_2}')

            while answer == '':
                try:
                    answer = int(input())

                    assert answer == result
                    print('Right!')
                    correct_answers += 1
                except ValueError:
                    print('Incorrect format.')
                    answer = ''
                except AssertionError:
                    print('Wrong!')
                    answer = ''
                    break
    if level == 2:
        number_1 = randint(11, 29)
        result = number_1 ** 2

        print(number_1)

        while answer == '':
            try:
                answer = int(input())

                assert answer == result
                print('Right!')
                correct_answers += 1
            except ValueError:
                print('Incorrect format.')
                answer = ''
            except AssertionError:
                print('Wrong!')
                answer = ''
                break

    oper = randint(0, 2)


print(f'Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.')

answer = input()

if answer == 'yes' or answer == 'YES' or answer == 'y' or answer == 'Yes':
    name = input('What is your name?\n')
    file = open('results.txt', 'a')

    file.write(f'{name}: {correct_answers}/5 in level {level_descriptions[level - 1]}')
    file.close()
    print('The results are saved in "results.txt".')
