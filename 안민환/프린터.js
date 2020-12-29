// 프린터
function solution(priorities, location) {
    var answer = 0;
    var descArr = priorities.slice(); // 깊은 복사(참조가 아닌 내용 복사)
    descArr = descArr.sort(function(f,s) { // 우선순위가 큰 순서로 정렬된 배열 생성
        console.log('first:: ' + f +', second:: ' + s);
        return s-f;
    }); 
    
    // 1. 우선순위 배열을 한 바퀴 돌면서 [현재위치, 우선순위] 배열로 만듬
    for(var i in priorities){
        priorities[i] = [i, priorities[i]];
    }
    
    // 2. 루프를 돌면서 현재 최대값이면 출력, 아니면 맨 뒤로 넣음
    var nowLoc = 0;
    var max = descArr.shift();
    while(true){
        var docJ = priorities.shift(); // 현재 문서를 빼냄
        var docJLoc = docJ[0]; // 문서J의 원래위치
        var docJPri = docJ[1]; // 문서J의 우선순위
        if(max == docJPri){
            nowLoc++;
            if(docJLoc == location){ // 이 문서가 내가 요청한 위치의 문서이면
                answer = nowLoc;
                break;
            }
            max = descArr.shift(); // 가장 큰 숫자 재설정
        } else {
            priorities.push(docJ);
        }
    }
    
    return answer;
}