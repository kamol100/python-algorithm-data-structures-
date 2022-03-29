
def climbingTheLeaderBoard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    result = []
    score = len(ranked)
    i = 0
    print(ranked)
    for play in player:
        #print(ranked[i], play,score)
        while i < score and ranked[i] <= play:
            i += 1
        result.append(score - i + 1)
    return result


ranked = [100,100,50,40,40,20,10]
player = [5,25,50,120]
print(climbingTheLeaderBoard(ranked, player))