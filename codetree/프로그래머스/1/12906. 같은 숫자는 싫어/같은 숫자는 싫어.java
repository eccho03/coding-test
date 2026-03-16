import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        int N = arr.length;
        
        ArrayList<Integer> numList = new ArrayList<Integer>();
        numList.add(arr[0]);
        for (int i=1; i<N; i++) {
            if (arr[i]==arr[i-1]) continue;
            numList.add(arr[i]);
        }
        
        // for (int num: numList){
        //     System.out.println(num);
        // }
        
        // list to array
        return numList.stream().mapToInt(i->i).toArray();
    }
}