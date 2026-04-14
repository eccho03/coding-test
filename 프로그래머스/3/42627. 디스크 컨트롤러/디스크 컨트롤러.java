import java.util.*;

class Solution {
    class Node {
        int num;
        int s;
        int l;
        
        Node(int num, int s, int l) {
            this.num = num;
            this.s = s;
            this.l = l;
        }
    }
    
    public int solution(int[][] jobs) {
        int answer = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>(
            (a, b) -> {
                if (a.l!=b.l) return a.l-b.l;
                if (a.s!=b.s) return a.s-b.s;
                return a.num-b.num;
            }
        );
        
        Arrays.sort(jobs, (a, b)-> a[0]-b[0]);
        
        int time = 0;
        int idx=0;
        int count = 0;
        
        while(count<jobs.length) {
            // 현재 시간까지 들어온 작업 추가
            while(idx<jobs.length && jobs[idx][0]<=time) {
                pq.offer(new Node(idx, jobs[idx][0], jobs[idx][1]));
                idx++;
            }
            
            // 실행 가능한 작업 있음
            if (!pq.isEmpty()) {
                Node cur_job = pq.poll();
                time += cur_job.l;
                answer += time - cur_job.s;
                count++;
            }
            else {
                time = jobs[idx][0];
            }
        }
        
        
        return answer/jobs.length;
    }
}