import java.util.*;

class Solution {
    static class Word {
        char ch;
        String string;
        
        Word(char ch, String string) {
            this.ch = ch;
            this.string = string;
        }
    }
    
    public String[] solution(String[] strings, int n) {
        ArrayList<Word> lst = new ArrayList<>();
        
        for (String string: strings) {
            lst.add(new Word(string.charAt(n), string));
        }
        
        Collections.sort(lst, new Comparator<Word>(){
            @Override
            public int compare(Word w1, Word w2) {
                int word_compare = w1.ch-w2.ch;
                if (word_compare!=0) return word_compare;
                return w1.string.compareTo(w2.string);
            }
        });
        
        return lst.stream().map(w->w.string).toArray(String[]::new);
    }
}