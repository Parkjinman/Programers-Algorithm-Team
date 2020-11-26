function solution(n, words) {
    var answer = [0,0];
    
    var num = 1; // 현재 누구 차례
    var order = 1; // 몇 번째 턴인지
    var passArr = []; // 통과된 단어 목록
    
    for(var i in words){
        var word = words[i];
        
        if(i!=0){ // 첫번째는 그냥 넘김
            
            // 중복 단어라면
            if(passArr.indexOf(word) > -1){
                answer = [num, order];
                break;
            }

            var prevLastChar = words[i-1].slice(-1); // 현재 단어의 마지막 값
            var thisFirstChar = word.slice(0,1); // 다음 단어의 첫번째 값

            if(prevLastChar != thisFirstChar){ // 끝말잇기가 안 됐다면
                answer = [num, order];
                break;
            }
        }
        
        // 여기 오면 pass된 것.
        passArr.push(word);
        num++;
        if(num > n) { // 다음 사람이 없으면
            num = 1; // 처음 사람으로 돌아옴
            order++; // 턴이 넘어감
        }
    }
    

    return answer;
}