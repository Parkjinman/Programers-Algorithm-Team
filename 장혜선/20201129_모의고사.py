# 모의고사(https://programmers.co.kr/learn/courses/30/lessons/42840)
def solution(answers):
    # 수포자별로 찍는 방식 리스트 생성
    ans_one = [1,2,3,4,5] # 1번 수포자 1,2,3,4,5 
    ans_two = [2,1,2,3,2,4,2,5] # 2번 수포자 2,1,2,3,2,4,2,5
    ans_thr = [3,3,1,1,2,2,4,4,5,5] # 3번 수포자 3,3,1,1,2,2,4,4,5,5
    ans_list = [ans_one, ans_two, ans_thr] # 찍는 방식 모음
    ans_len_list = [5,8,10] # 찍는 방식 길이
    correct_list = [0,0,0] # 정답 맞춘 갯수
    real_ans_len = len(answers) # 진짜 정답의 길이
    
    # 수포자 하나씩 순회하면서 정답 갯수를 체크한다
    for no_person in range(3):
        # 정답 길이 / 정답
        ans_len = ans_len_list[no_person]
        ans_per = ans_list[no_person]
        # 정답이 맞는지 체크
        for ques in range(real_ans_len):
            # 정답이 맞다면
            if answers[ques] == ans_per[ques%ans_len] :
                correct_list[no_person] += 1
            else : pass
    
    # 정답수를 key로, 사람 번호를 value로 갖는 dict를 생성(앞에서 부터 집어넣으면 오름차순으로 자동 정렬됨
    ans_count_dict = {}
    for no_person in range(3):
        # 맞춘 정답수
        answer_count = correct_list[no_person]
        # 정답수가 이미 있으면 동점자에 사람 번호 append
        # no_person+1 하는 이유-인덱스는 0부터인데 사람 번호는 1부터여서
        if answer_count in ans_count_dict:
            ans_count_dict[answer_count] = ans_count_dict[answer_count]+[no_person+1]
        else : 
            ans_count_dict[answer_count] = [no_person+1]
            
    return ans_count_dict[max(ans_count_dict.keys())] # 정답수가 가장 큰 사람들 리스트 리턴