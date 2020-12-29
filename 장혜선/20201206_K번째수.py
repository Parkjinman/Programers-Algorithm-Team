# K번째 수 (https://programmers.co.kr/learn/courses/30/lessons/42748)
def solution(array, commands):
    # 정답을 담을 리스트
    full_answer =[]

    for command_item in commands:
        i = command_item[0]
        j = command_item[1]
        k = command_item[2]
        # i와 k가 같으면 [i번째수(=k번째수)]로 생성
        if i == j :
            new_array = [array[i-1]]
        # 아니면 i번째~j번째 수로 리스트 생성
        else : 
            new_array = array[i-1:j]
            new_array.sort()
        
        # 전체 정답 리스트에 이어붙임(k번째 수)
        full_answer.append(new_array[k-1])
    
    return full_answer