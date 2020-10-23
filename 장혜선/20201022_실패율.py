def solution(N, stages):
    #1. 제한사항 체크 / user_len 지정
    if 1 <= N <= 500 : pass
    else : exit()

    user_len = len(stages)
    if 1 <= user_len <= 200000 : pass
    else : exit()

    #2. 실패율 계산
    # 실패율 리스트 생성(인덱스 편의를 위해 0부터 N까지 N+1개를 생성)
    fail_list = [0]*(N+1)

    for level in range(1, N+1):
        # 실패자 수(fail_num)를 센다
        fail_num = stages.count(level)

        # 만약 실패한 사람이 없으면 pass (실패율 default value : 0)
        if fail_num == 0 : pass
        # 실패한 사람이 있다면 실패율은 (실패자 수 / user_len)
        else :
            fail_list[level] = (fail_num/user_len)
            # 다음 스테이지에 넘어간 사람
            user_len = user_len - fail_num

    #3. 실패율이 높은 스테이지순으로 정렬(동점처리 필요)
    # (key) 0~N까지 수를 실패율(fail_list[N]) 기준으로 내림차순 정렬, 실패율이 같을 경우 스테이지가 낮을수록 정렬(-x)
    fail_sorted = sorted(range(N+1), key=lambda x : (fail_list[x], -x) , reverse =True)

    # 인덱스 편의를 위해 사용했던 0을 제거한 후 리턴
    fail_sorted.remove(0)
    return fail_sorted
