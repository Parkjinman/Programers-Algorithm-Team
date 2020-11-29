# 영어끝말잇기(https://programmers.co.kr/learn/courses/30/lessons/12981)
def solution(n, words):
    # 끝말잇기 규칙 : 단어 끝글자 > 단어 앞글자
    # 전체 단어 길이 저장
    len_words = len(words)
    # 단어 바구니(가장 첫번째 단어를 넣어둔다) (동일한 단어 발견시 break하기 위함)
    word_bucket = [words[0]]
    # 규칙 체크하면서 몇번째 순서에서 멈췄는지 확인
    # 두번째 단어 위치부터 순회
    for pos in range(1, len_words):
        word_bef = words[pos-1]
        word_now = words[pos] 
        # 규칙에 맞을 경우 단어 주머니에 단어를 담는다.
        if (word_bef[-1] == word_now[0]) and (word_now not in word_bucket):
            word_bucket.append(word_now)    
        else : 
        # n으로 숫자를 나눈 나머지 + 1 : 틀린 사람 위치
        # n으로 나눈 몫 + 1 : 틀린 사람이 말한 단어 위치
            return [(pos%n)+1,(pos//n)+1]
    # 끝까지 모두 통과하는 경우
    return [0,0]