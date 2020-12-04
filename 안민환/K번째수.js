// https://programmers.co.kr/learn/courses/30/lessons/42748
function solution(array, commands) {
    var answer = [];
    
    if(array.length > 100 || array.length < 1) return;
    if(commands.length > 50 || commands.length < 1) return;
    
    // 명령어를 1개씩 꺼냄
    for(var i in commands){
        var command = commands[i];
        // 0: slice start, 1: slice end, 2: num
        var newArr = array.slice(command[0]-1, command[1]);
        
        // sort는 문자 기준 정렬이라 100 미만 숫자 앞에 0을 붙여줌.
        for(var j=0; j<newArr.length; j++){
            var num = newArr[j];
            if(num >= 10 && num < 100) {
                num = '0' + num;
            } else if(num < 10){
                num = '00' + num;
            }
            newArr[j] = num;
        }
        
        newArr.sort();
        
        var kNum = Number(newArr[command[2]-1]);
        answer.push(kNum);
    }
    
    return answer;
}