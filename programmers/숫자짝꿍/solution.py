def solution(X, Y):
    answer = ''
    
    x_dict = {}
    for x in X:
        if x in x_dict:
            x_dict[x] += 1
        else:
            x_dict[x] = 1
    
    y_dict = {}
    for y in Y:
        if y in y_dict:
            y_dict[y] += 1
        else:
            y_dict[y] = 1
            
    for i in range(9, -1, -1):
        x = str(i)
        if x in x_dict and x in y_dict:
            if x_dict[x] > y_dict[x]:
                answer += x * y_dict[x]
            else:
                answer += x * x_dict[x]
                
    if answer == "":
        answer = "-1"
    elif [x for x in answer].count("0") == len([x for x in answer]):
        answer = "0"
    return answer