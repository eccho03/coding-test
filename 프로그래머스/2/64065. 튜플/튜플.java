import java.util.*;

class Solution {
    public int[] solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        
        String new_s = s.substring(0, s.length()-1);
        
        ArrayList<Integer> tmp = new ArrayList<>();
        String num="";
        boolean flag = true;
        
        for (int i=0; i<new_s.length(); i++) {
            
            char ch = new_s.charAt(i);
            if (flag && ch!='{' && ch!='}'&&ch!=',') {
                num+=ch;
                if (!Character.isDigit(new_s.charAt(i+1))) {             
                    tmp.add(Integer.parseInt(num));
                    num="";
                }
            }
            else if (ch=='{') flag = true;
            else if (ch=='}') {
                flag = false;
                arr.add(tmp);
                tmp = new ArrayList<>();
            }
            else continue;
        }
        // System.out.println(arr);
        
        Collections.sort(arr, new Comparator<>(){
            @Override
            public int compare(ArrayList<Integer> arr1, ArrayList<Integer> arr2) {
                return arr1.size()-arr2.size();
            }
        });
        
        // System.out.println(arr);
        for (ArrayList<Integer> cur_arr: arr) {
            for (int cur_num: cur_arr) {
                if (!answer.contains(cur_num)) {
                    answer.add(cur_num);
                    break;
                }
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}