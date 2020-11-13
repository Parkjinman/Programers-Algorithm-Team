/*
  문자열 내에 여는 괄호가 다 닫히면 true 안 닫히면 false
  - 닫는 괄호가 앞에, 여는괄호가 뒤에 나올 경우 여는괄호개수 = 닫는괄호개수 여도 false가 나올 수 있음
*/
function solution(s){
    var stack = [];
    var pushCnt = 0;
    var popCnt = 0;
    for(var i=0; i<s.length;i++){
        if('(' == s.charAt(i)) { // 여는 괄호일 경우 stack에 push
            pushCnt++;
            stack.push('(');
        } else if(')'== s.charAt(i)) { // 닫는 괄호일 경우 stack에서 pop
            popCnt++;
            if(stack.length != 0) stack.pop(); // 배열에 아무것도 없을 경우 다음 문자로 넘어감
        }
    }

    // 여는 괄호가 다 소진돼야 하므로 stack에 아무것도 없어야 됨
    // 여는 괄호만 다 닫으면 되는 줄 알았는데 '('개수와 ')'개수가 같아야 하는듯
    return stack.length == 0 && pushCnt == popCnt;
}