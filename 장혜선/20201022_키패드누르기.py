def solution(numbers, hand):
    # ===============================================================
    # 1. 초기 변수 세팅
    # ===============================================================
    # 왼쪽, 가운데, 오른쪽 수 리스트 생성
    l_num = [1,4,7,'*']
    m_num = [2,5,8,0]
    r_num = [3,6,9,'#']
    # 왼손가락과 오른손가락의 현 위치
    l_pos = '*'
    r_pos = '#'
    # hand_nm에 어느 손잡이 인지 변수 할당
    if hand == 'right':
        hand_nm = 'R'
    else : hand_nm = 'L'
    # 누른 손 위치를 저장하는 리스트(num_result)생성
    num_result = []

    # ===============================================================
    # 2. 키패드 누르기
    # ===============================================================
    # 누를 번호를 순회
    for now_num in numbers :
        # --------------------------------------------------------
        # 누를 번호(now_num)가 왼쪽, 또는 오른쪽 숫자일 경우
        # --------------------------------------------------------
        if now_num in l_num :
            num_result.append('L')
            l_pos = now_num
        elif now_num in r_num :
            num_result.append('R')
            r_pos = now_num

        # --------------------------------------------------------
        # 가운데 숫자일 경우 왼/오른 손가락의 현위치와 누를 번호 사이의 거리를 구해야 함
        # --------------------------------------------------------
        else :
            # 왼손이 왼쪽 수에 있을 때 / 가운데에 있을 때
            if l_pos in l_num :
                # 왼쪽과 가운데간 거리는 인덱스 위치끼리 뺀후 +1
                l_len = abs(l_num.index(l_pos) - m_num.index(now_num))+1
            else :
                l_len = abs(m_num.index(l_pos) - m_num.index(now_num))

            # 오른손도 왼손과 동일하게 계산
            if r_pos in r_num :
                r_len = abs(r_num.index(r_pos) - m_num.index(now_num))+1
            else :
                r_len = abs(m_num.index(r_pos) - m_num.index(now_num))

            # 거리 비교
            # 같은 거리일 경우 hand 변수 활용, 현재 손가락 위치 변경
            if l_len == r_len :
                num_result.append(hand_nm)
                if hand_nm == 'R' :
                    r_pos = now_num
                else :
                    l_pos = now_num

            # 왼손의 거리가 더 가까울 경우
            elif l_len < r_len :
                num_result.append('L')
                l_pos = now_num
            else :
                num_result.append('R')
                r_pos = now_num

    # --------------------------------------------------------
    # 3. return answer
    # --------------------------------------------------------
    answer = ''.join(num_result)
    return answer
