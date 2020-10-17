import java.util.Arrays;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        
        // 오름차순 정렬
        Arrays.sort(d);
        
        // 앞순부터 예산에서 차감 -> 예산 초과시 break
        for(int i=0; i<d.length; i++){
            budget -= d[i];
            if(budget < 0){
                answer = i;
                break;
            } 
            else if(i == d.length-1) answer = d.length;
        }
        
        return answer;
    }
}