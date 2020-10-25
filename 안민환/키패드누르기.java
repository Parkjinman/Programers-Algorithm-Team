/*
    1 <= numbers.length <= 1000
    0 <= numbers[i] <= 9
    
    문제 요약
    : 숫자배열 안의 값을 1개씩 뽑아 왼손으로 누르면 L, 오른손으로 누르면 R로 바꾸고 문자열로 만들어서 return
    1) 1,4,7이 나오면 L
    2) 3,6,9가 나오면 R
    3) 2,5,8,0은 이전에 누른 위치에서 가까운 손 (위치가 같으면 hander 체크)
*/
import java.util.HashMap;
class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        
        // 현재 왼손, 오른손 위치를 담을 변수
        int leftNum = 10; // * 대신 10
        int rightNum = 12; // # 대신 12
        
        // 패드숫자의 위치를 map에 저장
        /*
            map = {  1:00, 2:01, 3:02
                     4:10, 5:11, 6:12
                     7:20, 8:21, 9:22
                     10:30, 11:31, 12:32 }
        */
        HashMap map = new HashMap();
        for(int i=0; i<4; i++){
            for(int j=1; j<=3; j++){
                map.put(j+(i*3),(10*i)+(j-1));
            }
        }
        
        // 숫자 배열을 하나씩 꺼내서 적용
        for(int i=0; i<numbers.length; i++){
            // 현재 숫자
            int clickNum = numbers[i];
            if(clickNum == 0) clickNum = 11;
            
            if(clickNum % 3 == 1){ // 3으로 나눴을 때 나머지가 1이면 왼손
                leftNum = clickNum;
                answer += "L";
            }
            else if(clickNum % 3 == 0){ // 3으로 나눴을 때 나머지 0이면 오른손
                rightNum = clickNum;
                answer += "R";
            }
            else { // 2,5,8,0의 경우
                // 왼손, 오른손, 클릭부분 자판위치 구함
                int leftLoc = (int)map.get(leftNum);
                int rightLoc = (int)map.get(rightNum);
                int clickLoc = (int)map.get(clickNum);
                
                // 클릭 위치에서 왼,오른손과의 거리 구함
                int leftDist = Math.abs(clickLoc/10 - leftLoc/10) + Math.abs(clickLoc%10 - leftLoc%10);
                int rightDist = Math.abs(clickLoc/10 - rightLoc/10) + Math.abs(clickLoc%10 - rightLoc%10);
                
                // 두 거리를 비교
                if(leftDist < rightDist) {
                    leftNum = clickNum;
                    answer += "L";
                } else if(leftDist > rightDist) {
                    rightNum = clickNum;
                    answer += "R";
                } else {
                    if(hand.equals("left")){
                        leftNum = clickNum;
                        answer += "L";
                    } else {
                        rightNum = clickNum;
                        answer += "R";
                    }
                }
            }
        }
        
        return answer;
    }
}