import java.util.*;

class Solution {
    
    static class Stage {
        float ratio;
        int stage;

        Stage(float ratio, int stage) {
            this.ratio = ratio;
            this.stage = stage;
        }
    }
    
    public int[] solution(int N, int[] stages) {
        List<Stage> ratio = new ArrayList<>();
        int [] answer = new int[N];
        
        for (int i=1; i<=N; i++) {
            int all_cnt=0;
            int ing_cnt=0;
            for (int j=0; j<stages.length; j++){
                if (stages[j]>=i) {
                    all_cnt++;
                }
                if (stages[j]==i) {
                    ing_cnt++;
                }
            }
            // System.out.println(all_cnt+" "+ing_cnt);
            float failRatio = (all_cnt == 0) ? 0 : (float) ing_cnt / all_cnt;
            ratio.add(new Stage(failRatio, i));
            
        }
        
        Collections.sort(ratio, (a, b)-> {
            if (a.ratio==b.ratio) return a.stage-b.stage;
            return Float.compare(b.ratio, a.ratio);
        });
            
        for (int i=0; i<N; i++) {
            answer[i] = ratio.get(i).stage;
        }
        
        return answer;
    }
}