// 10진법 -> 3진법 -> 10진법
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        
        String base3 = ""; // 3진법 문자열
        int remainder = 0; // 나머지 변수
        // 3진법 역순 구하는 공식: 3으로 나눈 나머지 + 또 3으로 나눈 나머지 + ... + 마지막 나눈 몫
        while(n >= 3){
            remainder = n % 3;
            base3 += remainder;
            n /= 3;
        }
        base3 += n; // 마지막 나눈 몫을 맨 뒤에 붙임.
        
        // 3진법 -> 10진법 계산
        char[] charArr = base3.toCharArray();
        for(int i=0; i<charArr.length; i++){
            int base3Num = Integer.parseInt((String.valueOf(charArr[i])));
            answer += Math.pow(3, (charArr.length-1-i)) * base3Num;
        }
        
        return answer;
    }
}