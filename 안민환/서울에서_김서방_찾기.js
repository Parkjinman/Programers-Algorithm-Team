function solution(seoul) {
    var x = -1;
    seoul.find(function(name){ // find 함수는 배열을 순회하면서 찾는 게 있으면 순회 중단, 해당 값을 return.
        x++;
        return name == 'Kim';
    });
    return '김서방은 '+x+'에 있다';
}