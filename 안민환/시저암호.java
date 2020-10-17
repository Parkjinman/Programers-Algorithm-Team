// 시저 암호
class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        char[] charArr = new char[s.length()];
        for(int i=0; i<s.length(); i++){
            int asciiValue = (int)s.charAt(i);
            
            if (asciiValue == 32) charArr[i] = ' '; // 공백
            else if(asciiValue >= 65 && asciiValue <= 90) {
                charArr[i] = (char)((asciiValue + n > 90) ? asciiValue - 26 + n : asciiValue + n); //대문자 처리
            }
            else if(asciiValue >= 97 && asciiValue <=122) {
                charArr[i] = (char)((asciiValue + n > 122) ? asciiValue - 26 + n : asciiValue + n); //소문자 처리
            }
        }
        answer = new String(charArr);
        return answer;
    }
}