import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        int sum = 0;
        int time = 0;
        
        for (int i=0; i<bridge_length; i++) {
            queue.add(0);
        }
        
        int idx = 0;
        
        while (idx<truck_weights.length) {
            time++;
            sum -= queue.poll();
            
            if (truck_weights[idx]+sum<=weight) {
                queue.add(truck_weights[idx]);
                sum += truck_weights[idx];
                idx++;
            }
            else {
                queue.add(0);
            }
        }
        
        time+=bridge_length;
        
        return time;
    }
}