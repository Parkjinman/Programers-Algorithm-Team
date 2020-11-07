//.2016년 a월 b일은 무슨 요일
function solution(a, b) {
    var monthToDayArr = [31,29,31,30,31,30,31,31,30,31,30,31]; // 각 달의 일수
    var dayOfWeek = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    
    var days = 0;
    for(var i=0;i<a-1;i++){ // 해당 달의 전 달까지의 일 수를 더함
        days += monthToDayArr[i];
    }
    days += b; // 해당 달의 오늘까지의 일 수를 더함
    
    
    
    return dayOfWeek[(days+4) % 7]; // 금요일 부터라 +4 해줌(ex- 1월 1일 -> days = 1 -> dayOfWeek[5])
}