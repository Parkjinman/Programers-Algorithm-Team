/*
    N: stage 개수
    stages: 각 사용자별 현재 stage
    1 <= N <= 500
    1 <= stages.length <= 200000 (사용자 수)
    1 <= stages[i] <= N+1
    -> stages[i] == N+1 -> all clear
    -> 실패율 같으면 -> 작은 게 앞으로
    -> 도달한 사용자가 없는 stage -> 실패율 = 0
*/
import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        
        int clearNum = 0; // 해당 스테이지를 클리어한 사용자 수
        int arrivalNum = 0; // 해당 스테이지에 도달한 사용자 수
        double failPercent = 0;
        LinkedHashMap<Double, ArrayList> map = new LinkedHashMap<Double, ArrayList>(); // (실패율, 스테이지)
        
        // 1~N을 각 stages에서 조사한다.
        for(int num=1; num<=N; num++){
            clearNum = arrivalNum = 0; // 초기화
            for(int i=0; i<stages.length; i++){
                int userStage = stages[i]; // 해당 사용자의 stage
                if(userStage > num) { // 사용자의 현재 stage > 조사하는 스테이지 => 클리어한 것
                    clearNum++;
                    arrivalNum++;
                } else if (userStage == num){ // 클리어는 못했지만 도달은 한 것
                    arrivalNum++;
                }
            }
            // 실패율 계산
            failPercent = arrivalNum == 0 ? 0 : (double)(arrivalNum - clearNum) / arrivalNum;
            
            // map에 해당 스테이지를 key로, 실패율을 value로 저장
            if(map.containsKey(failPercent)){ // 해당 key가 있으면
                ArrayList arrList = (ArrayList)map.get(failPercent); // 기존 ArrayList값을 꺼내고
                arrList.add(num); // 그 ArrayList에 새 값을 추가시킴
            } else{
                ArrayList arrList = new ArrayList();
                arrList.add(num);
                map.put(failPercent, arrList); // 값을 ArrayList로 넣음
            }
        }
        
        // 실패율 정렬
        // 1. key(실패율)을 먼저 뽑아 내림차순 정렬
        Collection c = map.keySet();
        Iterator iter = c.iterator();
        ArrayList<Double> keyArr = new ArrayList<Double>();
        while(iter.hasNext()){
        	keyArr.add((double)iter.next());
        }
        Collections.sort(keyArr, Collections.reverseOrder());
        
        // 2. 정렬된 key를 다시 뽑아 key에 해당하는 value를 차례대로 넣음
        int idx = 0;
        iter = keyArr.iterator();
        while(iter.hasNext()){
            Object key = iter.next();
            Object value = map.get(key);
            if(value instanceof ArrayList){
                ArrayList sameFailStages = (ArrayList)value;
                int sameFailStagesSize = sameFailStages.size();
                for(int i=0; i<sameFailStagesSize; i++){
                    answer[idx++] = (int)sameFailStages.get(i);
                }
            } else {
                answer[idx++] = (int)iter.next();
            }
        }
        
        return answer;
    }
}