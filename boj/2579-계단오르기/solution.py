stair_num = int(input())
stairs = []
for i in range(stair_num):
    stairs.append(int(input()))
# stairs = [10,20,15,25,10,20]
scores = [[],[]]
scores[0] = [None] * stair_num
scores[1] = [None] * stair_num
def topDown(i, count):
    # print(i, stairs[i])
    if i < 0:
        return 0
    else:
        num = stairs[i] 
        if count == 1:
            if scores[0][i-2] == None:
                scores[0][i-2] = topDown(i-2, 0)
                num += scores[0][i-2]
            else:
                num += scores[0][i-2]
            return num
        else:
            if scores[1][i-1] == None:
                scores[1][i-1] = topDown(i-1, count+1)
            if scores[0][i-2] == None:
                scores[0][i-2] = topDown(i-2, 0)
            num += max(scores[1][i-1], scores[0][i-2])
            return num
if len(stairs) == 1:
    print(stairs[0])
else:
    num = topDown(len(stairs)-1, 0)
    # print("scores",scores)
    print(num)
