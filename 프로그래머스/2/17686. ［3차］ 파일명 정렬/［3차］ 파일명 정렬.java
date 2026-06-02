import java.util.*;

class Solution {
    static class File {
        String file;
        String head;
        int number;
        String tail;
        
        File(String file, String head, int number, String tail) {
            this.file = file;
            this.head = head;
            this.number = number;
            this.tail = tail;
        }
    }
    
    
    public String[] solution(String[] files) {
        String[] answer = new String[files.length];
        ArrayList<File> new_files = new ArrayList<>();
        
        for (int i=0; i<files.length; i++) {
            StringBuilder head = new StringBuilder();
            StringBuilder number = new StringBuilder();
            StringBuilder tail = new StringBuilder();
            boolean number_start = false;
            boolean tail_start = false;
            
            for (int j=0; j<files[i].length(); j++) {
                char c = files[i].charAt(j);
                if (!number_start) {
                    if (Character.isDigit(c)) {
                        number_start = true;
                        number.append(c);
                    }
                    else {
                        head.append(c);
                    }
                }
                else if (!tail_start) {
                    if (Character.isDigit(c)) {
                        number.append(c);
                    }
                    else {
                        tail_start = true;
                        tail.append(c);
                    }
                }
                
            }
            
            //System.out.println("head: "+head.toString());
            //System.out.println("number: "+number.toString());
            //System.out.println("tail: "+tail.toString());
            //System.out.println("----------------------------");
            
            
            String HEAD = head.toString().toLowerCase();
            int NUMBER = Integer.parseInt(number.toString());
            String TAIL = tail.toString();
            
            new_files.add(new File(files[i], HEAD, NUMBER, TAIL));
        }
        
        Collections.sort(new_files, new Comparator<File>(){
            @Override
            public int compare(File f1, File f2) {
                int head_compare = f1.head.compareTo(f2.head);          
                if (head_compare!=0) return head_compare;
                
                return Integer.compare(f1.number, f2.number);
            }
        });
        
        for (int i=0; i<files.length; i++) {
            answer[i] = new_files.get(i).file;
        }
        
        return answer;
    }
}