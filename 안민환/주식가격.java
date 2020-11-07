// 각 초의 가격에서 떨어지기까지의 시간을 구하는 것....
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        int nowIndex = 0; // 비교하는 배열의 index
        int notFallSec = 0; // 현재 index 값의 안 떨어진 시간
        
        /*
            0번째 index 값 -> 배열 뒤 index 값을 차례로 가져와서 비교해보고 떨어질 때까지 시간을 체크
            1번째 index 값
            2번째 index 값 ...
        */
        for(int i=0; i<prices.length; i++){
            if(nowIndex == i) continue; // 현재 값의 다음 index부터 시간을 재기 때문에 다음순으로 넘김.
            
            // 현재 비교하는 index의 값이 떨어졌는지 체크
            if(prices[nowIndex] > prices[i] || i == prices.length-1){ // 값이 떨어졌거나 마지막까지 안 떨어졌거나
                answer[nowIndex] = notFallSec + 1; // 현재 초까지 포함해서 정답 배열에 입력
                notFallSec = 0; // 초기화
                i = ++nowIndex; // 다음index값을 비교하기 위해 변경
            } else {
                notFallSec++;
            }
        }
        
        return answer;
    }
}