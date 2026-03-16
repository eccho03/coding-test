class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;
        for (int h=n; h>=0; h--) {
            int cnt_up = 0;
            int cnt_down = 0;
            for (int j=0; j<n; j++) {
                if (citations[j]>=h) {
                    cnt_up++;
                }
                if (citations[j]<h) {
                    cnt_down++;
                }
            }
            //System.out.println(cnt_up + " " + cnt_down);
            if (cnt_up>=h && cnt_down<=h) {
                return h;
                //System.out.println(cnt_up + " " + cnt_down);
            }
        }
        
        return answer;
    }
}