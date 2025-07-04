def Game():
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
                if num == 31:
                    return('A')
                print(f'playerA: {num}')
            player = 'B'
            continue

        if player == 'B':
            for _ in range(n):
                num = num + 1
                if num == 31:
                    return('B')
                print(f'playerB: {num}')
            player = 'A'

Game()