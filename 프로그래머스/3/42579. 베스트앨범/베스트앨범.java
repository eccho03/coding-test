import java.util.*;

class Solution {
    static class Song {
        int id;
        int play;
        
        Song (int id, int play) {
            this.id=id;
            this.play=play;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        Map<String, Integer> total_lst = new HashMap<>();
        Map<String, List<Song>> song_lst = new HashMap<>();

        for (int i=0; i<genres.length; i++) {
            total_lst.put(genres[i], total_lst.getOrDefault(genres[i], 0)+plays[i]);
            song_lst.putIfAbsent(genres[i], new ArrayList());
            song_lst.get(genres[i]).add(new Song(i, plays[i]));
        }
        
        //System.out.println(total_lst);
        //System.out.println(song_lst);
        
        List<String> total_order = new ArrayList<>(total_lst.keySet());
        total_order.sort((a,b)->total_lst.get(b)-total_lst.get(a));
        
        for (String genre: song_lst.keySet()) {
            List<Song> songs = song_lst.get(genre);
            
            songs.sort((a, b)-> {
                if (a.play!=b.play) return b.play-a.play;
                else return a.id-b.id;
            });
        }
        
        for (String genre: total_order) {
            List<Song> songs = song_lst.get(genre);
            answer.add(songs.get(0).id);
            if (songs.size()>1) answer.add(songs.get(1).id);            
        }

        return answer.stream().mapToInt(i->i).toArray();
    }
}