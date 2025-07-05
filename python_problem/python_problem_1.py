import random

def brGame():
    num = 0
    player = 'computer'

    while True:
        while True:
            try:
                if player == 'player':
                    n = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
                    if n < 1 or n > 3:
                        raise Exception('1, 2, 3 중 하나를 입력하세요')
                else:
                    n = random.randint(1, 3)
            except ValueError:
                print('정수를 입력하세요')
                continue
            except Exception as e:
                print(e)
            else:
                break
        if player == 'computer':
            for _ in range(n):
                num = num + 1
                print(f'computer: {num}')
                if num == 31:
                    return 'computer'
            player = 'player'
            continue

        if player == 'player':
            for _ in range(n):
                num = num + 1
                print(f'player: {num}')
                if num == 31:
                    return 'player'
            player = 'computer'

winner = brGame()
if winner == 'computer':
    print('player win!')
else:
    print('computer win!')