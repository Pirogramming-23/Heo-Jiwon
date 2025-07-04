def brGame():
    num = 0
    player = 'A'

    while True:
        while True:
            try:
                n = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
                if n < 1 or n > 3:
                    raise Exception('1, 2, 3 중 하나를 입력하세요')
            except ValueError:
                print('정수를 입력하세요')
                continue
            except Exception as e:
                print(e)
            else:
                break
        if player == 'A':
            for _ in range(n):
                num = num + 1
                print(f'playerA: {num}')
                if num == 31:
                    return 'A'
            player = 'B'
            continue

        if player == 'B':
            for _ in range(n):
                num = num + 1
                print(f'playerB: {num}')
                if num == 31:
                    return 'B'
            player = 'A'

winner = brGame()
if winner == 'A':
    print('playerB win!')
else:
    print('playerA win!')