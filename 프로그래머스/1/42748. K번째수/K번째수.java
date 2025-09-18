import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        
        ArrayList<Integer> numList = new ArrayList<Integer>();
        
        for (int cur=0; cur<commands.length; cur++) {
            int i = commands[cur][0];
            int j = commands[cur][1];
            int k = commands[cur][2];
            i--;
            
            int[] tmp = new int[j-i];
            
            for (int idx=i; idx<j; idx++) {
                tmp[idx-i] = array[idx];
            }
            
            Arrays.sort(tmp);
            
            // for (int t: tmp) {
            //     System.out.print(t+" ");
            // }
            
            for (int idx=0; idx<tmp.length; idx++) {
                if (idx+1==k) {
                    numList.add(tmp[idx]);
                    break;
                }
            }
            
        }
        
        // for (int num: numList) {
        //     System.out.println(num);
        // }
        
        answer = numList.stream().mapToInt(i->i).toArray();
        
        return answer;
    }
}