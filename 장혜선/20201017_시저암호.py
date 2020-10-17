def solution(s, n):
    # 알파벳 전체
    big_raw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 대문자 알파벳 리스트 생성
    big_list = [char for char in big_raw]
    # 0번째 인덱스에는 Z를 추가해서 A이전의 글자를 Z로 지정
    big_list.insert(0,'Z')

    # 소문자 알파벳 리스트 생성
    small_list = [char.lower() for char in big_raw]
    # 0번째 인덱스에는 z를 추가해서 a이전의 글자를 z로 지정
    small_list.insert(0,'z')

    # s에 빈 값이 들어올 경우
    if len(s) == 0 :
        return ''

    # result_list 생성
    result_list =[]

    # 입력된 문자열 s을 앞에서부터 item에 담는다.
    for item in s :
        #item이 공백이면 공백을 append
        if item == ' ':
            result_list.append(' ')
        #item이 소문자 글자라면
        elif item in small_list :
            # item_pos : 소문자 글자의 인덱스 번호
            item_pos = small_list.index(item)
            # new_pos : 밀린 이후 인덱스 번호(26 이상이 될 수 있으므로 26으로 나눈 나머지를 밀린 이후의 인덱스 값으로 지정)
            new_pos = (item_pos +n)%26
            # 밀린 위치의 인덱스의 소문자 글자를 append
            result_list.append(small_list[new_pos])
        else :
            # 소문자와 동일한 방식으로 진행
            item_pos = big_list.index(item)
            new_pos = (item_pos +n)%26
            result_list.append(big_list[new_pos])

    # result_list의 아이템을 모두 이어붙인 후 리턴
    return ''.join(result_list)
