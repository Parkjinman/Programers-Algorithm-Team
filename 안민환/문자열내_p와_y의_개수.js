/*
  문자열에서 p의 개수와 y의 개수 비교
  - 대소문자 구분 X
  - 각 개수가 같으면 true, 다르면 false
*/
function solution(s){
    s = s.toLowerCase();
    var pCnt = 0;
    var yCnt = 0;
    for(var i=0; i<s.length; i++){
        if('p' == s.charAt(i)) pCnt++;
        else if('y' == s.charAt(i)) yCnt++;
    }

    return pCnt == yCnt;
}