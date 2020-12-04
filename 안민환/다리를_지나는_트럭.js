// https://programmers.co.kr/learn/courses/30/lessons/42583
function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    
    // 기본 조건
    if(bridge_length > 10000 || bridge_length < 1) return;
    if(weight > 10000 || weight < 1) return;
    if(truck_weights > 10000 || truck_weights < 1) return;
    if(truck_weights > weight) return;
    
    // ex) 다리길이:4 -> [0,0,0,0]
    var bridge = [];
    for(var i=0;i<bridge_length;i++){
        bridge.push(0);
    }
    
    // 다리 위 무게 총합
    var wtSum = 0;
    
    // 대기트럭이 없을 때까지 루프
    while(truck_weights.length > 0){
        var popVal = bridge.shift(); // ex) [0,0,1] -> popVal = 0, [0,1]
        if(popVal > 0){ // 트럭이 다리를 건너면
            wtSum -= popVal; // 무게 총합에서 해당 트럭 무게 빼줌
        }

        if(weight >= wtSum + truck_weights[0]){ // 허용 무게 이하면
            var truckWt = truck_weights.shift(); // 트럭 하나 더 빼냄
            bridge.push(truckWt); // 다리에 넣음
            wtSum += truckWt; // 무게 추가
        } else {
            bridge.push(0); // 트럭이 안 붙으므로 마지막 빈자리 0으로 채움
        }

        answer++; // 초 증가
     }
    
    answer += bridge_length; // 마지막 트럭이 출발하면 다리 길이만큼 초가 걸리므로 더해줌
    
    return answer;
}