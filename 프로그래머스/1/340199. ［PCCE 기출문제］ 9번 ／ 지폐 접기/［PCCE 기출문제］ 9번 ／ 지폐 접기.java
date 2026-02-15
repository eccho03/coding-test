class Solution {
    static int[] putHalf(int[] bill) {
        if (bill[0]<bill[1]) bill[1]/=2;
        else bill[0]/=2;
        return bill;
    }
    static boolean isPut(int[] wallet, int[] bill) {
        if (wallet[0]>=bill[0] && wallet[1]>=bill[1]) return true;
        if (wallet[0]>=bill[1] && wallet[1]>=bill[0]) return true;
        return false;
    }
    
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        // 항상 길이가 긴 쪽을 반으로 접어야함
        // 버림
        
        while(true) {
            if (isPut(wallet, bill)) break;
            bill = putHalf(bill);
            // System.out.println(wallet[0] +" " +wallet[1]+" " +bill[0]+" " +bill[1]);
            answer++;
        }
        return answer;
    }
}