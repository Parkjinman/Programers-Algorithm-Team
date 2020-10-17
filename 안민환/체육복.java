// 체육복
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        
        // 여벌 있음 + 도난된 학생 제외
        for(int i=0; i<lost.length; i++){
            for(int j=0; j<reserve.length; j++){
                if(reserve[j] == lost[i]) {
                    reserve[j] = -1;
                    lost[i] = -1;
                    break;
                }
            }
        }
        
        // 빌려주기 작업
        for(int i=0; i<lost.length; i++){
            for(int j=0; j<reserve.length; j++){
                if(reserve[j]-lost[i] == 1 || reserve[j]-lost[i] == -1){
                    lost[i] = -1;
                    reserve[j] = -1;
                    break;
                }
            }
            if(lost[i] != -1) n -= 1; 
        }
        
        return n;
    }
}