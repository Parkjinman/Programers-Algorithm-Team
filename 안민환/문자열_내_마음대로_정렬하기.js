/*
    문제 요약: 문자열들의 n번째 문자순으로 정렬하시오.
    -  1 <= strings.length <= 50
    - 문자는 소문자로만
    - 문자 길이는 1이상 100이하, n보다 큼
    - n번째 문자가 같으면 해당 문자열을 사전순으로
*/
function solution(strings, n) {
    var answer = [];
    var nIndexArr = [];
    // 문자열을 1개씩 꺼내 n번째 문자를 가져와서 해당 문자열 맨 앞에 붙임
    for(var i=0; i<strings.length; i++){
        nIndexArr[i] = strings[i].substr(n,1);
        strings[i] = nIndexArr[i] + strings[i];
    }
    
    // 변경된 문자열 배열을 정렬
    strings.sort();
    
    // 맨 앞에 붙였던 문자들을 빼줌
    for(var j=0; j<strings.length; j++){
        answer[j] = strings[j].substring(1,strings[j].length);
    }
    
    return answer;
}