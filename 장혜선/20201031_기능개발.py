def solution(progresses, speeds):
    
    # 1. 진척률 길이, 완료된 수, 정답 리스트 생성
    # ---------------------------------------------------------
    prog_len = len(progresses)
    fin_item_count = 0
    answer_list = []

    while True:
        # 진척률 = 진척률 + (스피드 * n days)
        progresses = [(progresses[i] + speeds[i]) for i in range(prog_len)]
	
        # 2-1. 가장 앞의 작업 진척률이 100이상 되면
        # ---------------------------------------------------------
        if progresses[0] >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            fin_item_count += 1
            prog_len -= 1
		    
		    # while progress(파이썬에서는 리스트가 비어있으면 False를 리턴한다)
            while progresses :
                # 2-2. 완료된 업무 직후의 업무가 100 이상(연속해서)인 경우만
                # ---------------------------------------------------------
                if progresses[0] >= 100 :
                    progresses.pop(0)
                    speeds.pop(0)
                    fin_item_count +=1
                    prog_len -=1
                else : 
                    break
                    
            # 3. 완료된 업무 개수를 정답 리스트에 append 
            # ---------------------------------------------------------
            answer_list.append(fin_item_count)
            
            # 진척률 길이가 0이 되면(모든 작업 완료)
            if prog_len == 0 :
                break
            else :
                # 완료된 작업 개수 초기화
                fin_item_count = 0
                
    
    return answer_list
