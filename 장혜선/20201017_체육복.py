def solution(n, lost, reserve) :
    # 전체 학생수+2 만큼 1로 리스트 생성
    # 학생수 5이면 : [1, 1, 1, 1, 1, 1, 1]
    all_student = [1]*(n+2)

    # 여벌 체육복이 있는 학생은 체육복 갯수를 1개 늘림
    for num in reserve :
        all_student[num] +=1

    # 분실한 학생은 체육복 갯수를 1개 줄임
    for num in lost :
        all_student[num] -=1

    # 학생 번호가 1부터 n가지 있으니까 1부터 시작
    for num in range(1, n+1):
        # num 번째 학생이 체육복이 없을 때
        if all_student[num] == 0 :
            # (if) num -1 번째 학생이 체육복 2개이면 num에게 나눠준다
            if all_student[num-1] == 2:
                all_student[num-1] -=1
                all_student[num] +=1
            # (elif) num +1 번째 학생이 체육복 2개이면 num에게 나눠준다
            elif all_student[num+1] == 2:
                all_student[num+1] -= 1
                all_student[num] +=1
            # 앞 뒤 학생이 2개의 체육복이 없는 경우는 넘어간다
            else : pass

    # 1부터 n번까지 학생 중 체육복을 1개 이상 가지고 있을 경우에 student_full에 1로 할당
    student_full = [1 for x in all_student[1:n+1] if x>0]

    # 수업 들을 수 있는 학생 수 리턴
    return sum(student_full)
