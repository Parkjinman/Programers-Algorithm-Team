function solution(answers) {
    var answer = [];
    var cntObj = {cnt1:0, cnt2:0, cnt3:0};
    var supo1Arr = [1,2,3,4,5];
    var supo2Arr = [2,1,2,3,2,4,2,5];
    var supo3Arr = [3,3,1,1,2,2,4,4,5,5];
    var idx1 = 0, idx2 = 0, idx3 = 0;
    
    // 3명의 정답 횟수 구하기
    for(var i in answers){
        if(answers[i] == supo1Arr[idx1]){
            cntObj.cnt1 = cntObj.cnt1 + 1;
        }
        if(answers[i] == supo2Arr[idx2]){
            cntObj.cnt2 = cntObj.cnt2 + 1;
        }
        if(answers[i] == supo3Arr[idx3]){
            cntObj.cnt3  = cntObj.cnt3 + 1;
        }
        idx1++; idx2++; idx3++;
        if(idx1 % 5 == 0) idx1 = 0;
        if(idx2 % 8 == 0) idx2 = 0;
        if(idx3 % 10 == 0) idx3 = 0;
    }
    
    // 정답 횟수 max값 구함
    var max = 0;
    var keys = Object.keys(cntObj);
    for(var j in keys){
        var cnt = cntObj[keys[j]];
        if(cnt > max){
            max = cnt;
        }
    }
    
    // max값과 같은 key를 가장 많은 정답자 배열에 넣음
    for(var k in keys){
        var cnt = cntObj[keys[k]];
        if(max == cnt){
            answer.push(Number(k)+1);
        }
    }
    
    // 정답 배열 오름차순 정렬
    if(answer.length > 1) answer.sort();
    
    return answer;
}