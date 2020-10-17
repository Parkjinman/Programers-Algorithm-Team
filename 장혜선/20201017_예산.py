def solution(d, budget):
    # sort d
    d.sort()
    answer = 0

    # if nothing in d
    if len(d) == 0 :
        return 0

    for item in d :
        budget -= item
        if budget >=0 :
            answer += 1
        else :
            return answer

    return answer
