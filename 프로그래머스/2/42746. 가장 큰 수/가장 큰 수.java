import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuilder answer = new StringBuilder();
        String[] arr = new String[numbers.length];
        
        for (int i=0; i<numbers.length; i++) {
            arr[i]=String.valueOf(numbers[i]);
        }
        
        Arrays.sort(arr, (a, b) -> (b+a).compareTo(a+b));
        
        // System.out.println(Arrays.toString(arr));
        
        for (String num: arr) {
            answer.append(num);
        }
        
        if (arr[0].equals("0")) return "0";
        
        return answer.toString();
    }
}