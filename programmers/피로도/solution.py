def func(start, k, dungeons, step):
    dungeon = dungeons[start]
    if dungeon[0] > k:
        return step
    else:
        k -= dungeon[1]
        step += 1
        
        index = dungeons.index(dungeon)
        temp_dungeons = dungeons[:index]+dungeons[index+1:]
        if len(temp_dungeons) == 0:
            return step
        else:
            return max([func(i, k, temp_dungeons, step) for i in range(len(temp_dungeons))])

def solution(k, dungeons):
    answer = 0
    
    # dungeons = sorted(dungeons, key=lambda x : (x[0]-x[1], -x[0]), reverse = True)
    # print(dungeons)
    # for dungeon in dungeons:
    #     if dungeon[0] <= k:
    #         k -= dungeon[1]
    #         answer+=1
    answer = max([func(i, k, dungeons, 0) for i in range(len(dungeons))])
    print(answer)
    return answer