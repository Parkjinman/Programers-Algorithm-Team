/*
    0 <= progresses.length, speends.length <= 100
    0 < progresses[i] < 100
    0 < speeds[i] <= 100
    
    - progresses: 작업 진도 배열 (먼저 배포돼야할 것들 순)
    - speeds: 작업 속도 배열 (해당 작업의 하루 작업 속도)
    - 앞순의 작업이 안 끝났으면 뒷순의 작업이 끝났어도 배포 안 됨. (앞순작업 끝나는 날에 같이 배포)
*/

function solution(progresses, speeds) {
    var answer = [];
    var cnt = 0; // 같은 날짜에 배포되는 작업 수
    var distributeDay = 0; // 배포하는 날
    
    // 먼저 작업을 배열에서 하나씩 빼서 남은 날을 계산 (남은 진도 / 속도)
    for(var i in progresses){
        if(speeds[i] != 0){ // 작업속도가 0이 아니면
            var remainDay = Math.ceil((100 - progresses[i]) / speeds[i]); // 남은 날
            if(cnt==0) { // 맨 처음
                distributeDay = remainDay;
                cnt = 1;
            }
            else if(distributeDay >= remainDay) { // 현재 작업의 남은 날보다 이전 작업 배포날이 더 크면 -> 같은 날 배포 count 증가
                cnt++;
            }
            else if(distributeDay < remainDay){ // 현재 작업의 남은날이 이전 작업 배포날보다 더 크면 -> 이전 작업 배포
                answer.push(cnt);
                distributeDay = remainDay;
                cnt = 1;
            }
        }
    }
    
    // 마지막에 answer에 안 넣어지고 반복문이 끝났을 경우
    if(cnt>0) answer.push(cnt);
    
    return answer;
}