player1 = "[O]"
player2 = "[X]"
empty = "[ ]"


def print_stage(stage):
    for i in range(0, 9):
        end = ""
        if i % 3 == 2:
            end = "\n"
        else:
            end = " "
        print(stage[i], end=end)


def stage_init():
    stage = []
    for i in range(0, 9):
        stage.append(empty)
    return stage


def ended(stage):
    winner = ""
    if stage[4] != empty \
            and ((stage[0] == stage[4] and stage[8] == stage[4]) or (stage[2] == stage[4] and stage[6] == stage[4])):
            winner = stage[4]
    else:
        for i in range(0, 3):
            row = i * 3
            if stage[row] != empty and stage[row] == stage[row + 1] and stage[row] == stage[row + 2]:
                winner = stage[row]
                break
            if stage[i] != empty and stage[i] == stage[i + 3] and stage[i] == stage[i+6]:
                winner = stage[i]
                break
    ret = 0
    if winner == player1:
        ret = 1
    elif winner == player2:
        ret = 2
    return ret


stage = stage_init()
print_stage(stage)
wins = 0

for i in range (0,9):

    player = ' '
    if i % 2 == 0 :
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
        elif stage[location] != empty:
            print("이미 놓인 자리입니다.")
        else:
            stage[location] = player
            break

    print_stage(stage)
    wins = ended(stage)
    if wins != 0:
        print("유저 %d가 승리하였습니다." % wins)
        break

if wins == 0:
    print("무승부입니다.")










