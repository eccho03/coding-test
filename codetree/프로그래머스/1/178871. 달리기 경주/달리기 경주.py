def solution(players, callings):
    answer = []
    
    ranking = {player: idx for idx, player in enumerate(players) }
    
    for target in callings:
        idx = ranking[target]
        front = players[idx-1]
        players[idx-1], players[idx] = players[idx], players[idx-1]
        ranking[target]-=1
        ranking[front]+=1
        
    return players