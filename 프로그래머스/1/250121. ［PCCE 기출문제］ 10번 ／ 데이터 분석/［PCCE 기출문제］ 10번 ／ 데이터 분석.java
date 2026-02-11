import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int[][] answer = {};
        List<int[]> lst = new ArrayList<>();

        int extIdx = findIdx(ext);
        int sortIdx = findIdx(sort_by);
        
        for (int[] cur: data) {
            if (cur[extIdx] < val_ext) {
                lst.add(cur);
            }
        }
        /*
        for (int[] cur: lst) {
            System.out.println(Arrays.toString(cur));
        }
        */
        lst.sort((a,b)-> a[sortIdx]-b[sortIdx]);
        
        return lst.toArray(new int[lst.size()][]);
    }
    
    int findIdx(String st) {
        int idx = -1;
        switch(st) {
                case "code" -> idx = 0;
                case "date" -> idx = 1;
                case "maximum" -> idx = 2;
                case "remain" -> idx = 3;
        }
        return idx;
    }
}