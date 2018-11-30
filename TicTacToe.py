player1 = "[O]"
player2 = "[X]"
empty = "[%d]"


def print_stage(stage):
    for index in range(0, 9):
        if index % 3 == 2:
            end = "\n"
        else:
            end = " "

        print(stage[index], end=end)


def stage_init():
    stage = []
    for i in range(0, 9):
        stage.append(empty % (i + 1))
    return stage


def is_placed(cell):
    return cell == player1 or cell == player2


def ended(stage):
    winner = ""
    if is_placed(stage[4]) \
            and ((stage[0] == stage[4] and stage[8] == stage[4]) or (stage[2] == stage[4] and stage[6] == stage[4])):
            winner = stage[4]
    else:
        for i in range(0, 3):
            row = i * 3
            if is_placed(stage[row]) and stage[row] == stage[row + 1] and stage[row] == stage[row + 2]:
                winner = stage[row]
                break
            if is_placed(stage[i]) and stage[i] == stage[i + 3] and stage[i] == stage[i+6]:
                winner = stage[i]
                break
    ret = 0
    if winner == player1:
        ret = 1
    elif winner == player2:
        ret = 2
    return ret


game = stage_init()
print_stage(game)
wins = 0

for turn in range(0, 9):

    player = ' '
    if turn % 2 == 0:
        print("유저 1의 차례입니다.")
        player = player1
    else:
        print("유저 2의 차례입니다.")
        player = player2
    location = 0
    while True:
        location = int(input("놓을 위치를 입력하세요 : ")) - 1
        if location < 0 or location > 8:
            print("잘못된 값입니다.")
        elif is_placed(game[location]):
            print("이미 놓인 자리입니다.")
        else:
            game[location] = player
            break

    print_stage(game)
    wins = ended(game)
    if wins != 0:
        print("유저 %d가 승리하였습니다." % wins)
        break

if wins == 0:
    print("무승부입니다.")
