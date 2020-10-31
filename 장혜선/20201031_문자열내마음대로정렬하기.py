def solution(strings, n):
    # 0. 알파벳 리스트 생성
    alp_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alp_list = alp_list.split()
	
	# 1. 문자열의 n번째 원소로 이루어진 리스트
    # -----------------------------------------
    n_str_list = [word[n] for word in strings ]
    
    # 2. word_dict 의 key가 알파벳 위치 인덱스 번호고 value가 단어(strings)의 위치(pos)가 되도록 생성
    # -----------------------------------------
    word_dict = {}
    for pos in range(len(n_str_list)):
        # n_str_key: 알파벳 위치
        n_str_key = alp_list.index(n_str_list[pos])
        # 만약 dict에 알파벳 위치 인덱스가 없다면
        if n_str_key not in word_dict :
            word_dict[n_str_key] = [pos]
        # 똑같은 알파벳 위치 인덱스가 존재할 때
		# ['기존 단어 인덱스'] +['현재 단어 인덱스']
        else :
            word_dict[n_str_key] = word_dict[n_str_key]+[pos]
	
    
    # 3. answer_list 생성
    # ----------------------------------------
    # value_set: key를 오름차순 정렬
    value_set = sorted(word_dict.keys())
    answer_list = []
    # 알파벳 위치 인덱스를 오름차순으로 순회하면서
    for value in value_set :
        # 동일한 알파벳 위치 인덱스를 가진 단어가 1개만 있으면
        if len(word_dict[value]) == 1 :
            answer_list.append(strings[word_dict[value][0]])
        # 마지막 제한조건
        else :
            strs = [strings[pos] for pos in word_dict[value]]
            answer_list.extend(sorted(strs))
	
    return answer_list
