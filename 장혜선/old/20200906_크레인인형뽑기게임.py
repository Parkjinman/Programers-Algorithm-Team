def solution(board, moves):
    move_row = 0
    doll_bucket = []
    result = 0
    board_size = len(board)

    # 작동시킬 위치 배열을 앞에서부터
    for move_row in range(len(moves)) :
        # 실제 작동시킬 위치의 인덱스는 -1 해주어야 함
        move_index = moves[move_row]-1
        board_row = 0

        # move_index 위치에 인형이 존재할 때 까지
        while board[board_row][move_index] == 0:
            # 인형이 존재하지 않으면
            board_row += 1
            # 마지막 인덱스까지 순회했을 때
            if board_row == board_size :
                break

        # 인형을 지정한다.
        # board_row가 board_size일 경우(해당 열에 인형이 하나도 없는 경우)
        # 인형이 선택되지 않고 오류 발생하므로 다음 루프를 돌게 함
        try :
            doll = board[board_row][move_index]
        except :
            print('no move')
            continue

        # 인형이 있던 자리의 원소를 0 으로 대치한다.
        board[board_row][move_index] = 0

        # 인형 바구니에 인형이 하나도 없으면
        if len(doll_bucket) == 0 :
            doll_bucket.append(doll)

        # 제일 위에 있던 인형이랑 지금 인형이랑 같으면 인형을 꺼내고 result에 +2
        elif doll_bucket[-1] == doll :
            doll_bucket.pop()
            result +=2

        # 그렇지 않은 경우 인형 바구니에 인형을 추가한다.
        else :
            doll_bucket.append(doll)

    return result
