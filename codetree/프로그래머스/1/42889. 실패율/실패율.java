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
        int[] answer = new int[N];
        List<Stage> ratio = new ArrayList<>();
        
        for (int i=1; i<=N; i++) {
            int completed=0;
            int doing=0;
            for (int j=0; j<stages.length; j++) {
                if (stages[j]>=i) completed++;
                if (stages[j]==i) doing++;
            }
            if (completed==0) ratio.add(new Stage(0, i));
            else ratio.add(new Stage((float)doing/completed, i));
        }
        
        ratio.sort((a, b) -> {
            if (a.ratio==b.ratio) return a.stage-b.stage;
            return Float.compare(b.ratio, a.ratio);
        });
        
        for (int i=0; i<N; i++) {
            answer[i]=ratio.get(i).stage;
        }
        
        return answer;
    }
}