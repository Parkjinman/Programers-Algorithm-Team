# 다리를 지나는 트럭(https://programmers.co.kr/learn/courses/30/lessons/42583)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0 #시간
    truck_pos = 0 # 트럭의 위치
    bridge = deque([0] * bridge_length) # 다리길이 만큼 큐 생성
    len_truck_weights = len(truck_weights) # 대기 트럭 길이 
    weight_sum = 0 # 다리 위 트럭 무게
    
    while truck_pos < len_truck_weights: 
        time += 1
        first_truck = bridge.popleft() #시간이 지나서 빠져나오는 트럭
        weight_sum -= first_truck #트럭이 빠져나왔으므로 다리 위 무게에서 빼줌
        
        # 다리 위 무게 + 들어갈 트럭 무게가 견딜 수 있는 무게이면
        if weight_sum + truck_weights[truck_pos] <= weight:
            bridge.append(truck_weights[truck_pos]) # 다리에 트럭 추가
            weight_sum += truck_weights[truck_pos] #다리 위 트럭 무게
            truck_pos += 1 # 다음 트럭으로 이동
            
        # 아니면 0을 붙임
        else:
            bridge.append(0)
            
    # 마지막 트럭까지 다리를 건너는 시간 = 제일 마지막 트럭이 다리에 진입한 시간(time) + 다리 길이(bridge_length)
    return time + bridge_length