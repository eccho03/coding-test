import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        ArrayList<String> answer = new ArrayList<>();
        
        int[][] new_arr1 = new int[n][n];
        int[][] new_arr2 = new int[n][n];
        int[][] answer_arr = new int[n][n];
        
        for (int i=0; i<n; i++) {
            String binary = Integer.toBinaryString(arr1[i]);
            while (binary.length() < n) {
                binary = "0" + binary;
            }
            // System.out.println(binary);
            
            for (int j=0; j<n; j++) {
                new_arr1[i][j] = binary.charAt(j)-'0';
            }
        }
        
        for (int i=0; i<n; i++) {
            String binary = Integer.toBinaryString(arr2[i]);
            while (binary.length() < n) {
                binary = "0" + binary;
            }
            // System.out.println(binary);
            
            for (int j=0; j<n; j++) {
                new_arr2[i][j] = binary.charAt(j)-'0';
            }
        }
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (new_arr1[i][j]==1 || new_arr2[i][j]==1) {
                    answer_arr[i][j]=1;
                }
                else {
                    answer_arr[i][j]=0;
                }
            }
            //System.out.println();
        }
        
        for (int i=0; i<n; i++) {
            StringBuilder tmp = new StringBuilder();
            for (int j=0; j<n; j++) {
                if (answer_arr[i][j]==1) tmp.append("#");
                else tmp.append(" ");
            }
            answer.add(tmp.toString());
        }
        
        return answer.toArray(new String[0]);
    }
}