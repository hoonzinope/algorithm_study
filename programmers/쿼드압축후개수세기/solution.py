def slice_arr(arr, upDown, direction):
    temp_arr = []
    slice_num = len(arr)//2
    if upDown == "up":
        for sub in arr[:slice_num]:
            sub_arr = []
            if direction == "left":
                for num in sub[:slice_num]:
                    sub_arr.append(num)
                temp_arr.append(sub_arr)
            else:
                for num in sub[slice_num:]:
                    sub_arr.append(num)
                temp_arr.append(sub_arr)
    else:
        for sub in arr[slice_num:]:
            sub_arr = []
            if direction == "left":
                for num in sub[:slice_num]:
                    sub_arr.append(num)
                temp_arr.append(sub_arr)
            else:
                for num in sub[slice_num:]:
                    sub_arr.append(num)
                temp_arr.append(sub_arr)
    return temp_arr

def dfs(arr):
    count_dic = {}
    if len(arr) == 1:
        count_dic[arr[0][0]] = 1
        return count_dic
    else:
        temp_arr = slice_arr(arr, "up","left")
        quater_1 = dfs(temp_arr)
        
        temp_arr = slice_arr(arr, "up", "right")
        quater_2 = dfs(temp_arr)
        
        temp_arr = slice_arr(arr, "down", "left")
        quater_3 = dfs(temp_arr)
        
        temp_arr = slice_arr(arr, "down", "right")
        quater_4 = dfs(temp_arr)
        
        for key in quater_1.keys():
            if key in count_dic:
                count_dic[key] += quater_1[key]
            else:
                count_dic[key] = quater_1[key]
                
        for key in quater_2.keys():
            if key in count_dic:
                count_dic[key] += quater_2[key]
            else:
                count_dic[key] = quater_2[key]
                
        for key in quater_3.keys():
            if key in count_dic:
                count_dic[key] += quater_3[key]
            else:
                count_dic[key] = quater_3[key]
                
        for key in quater_4.keys():
            if key in count_dic:
                count_dic[key] += quater_4[key]
            else:
                count_dic[key] = quater_4[key]
        
        key_list = list(count_dic.keys())
        if len(key_list) == 1 and count_dic[key_list[0]] == 4:
            count_dic[key_list[0]] = 1
                
        return count_dic
        

def solution(arr):
    answer = []
    
    count_dic = dfs(arr)
    if 0 in count_dic:
        answer.append(count_dic[0])
    else:
        answer.append(0)
        
    if 1 in count_dic:
        answer.append(count_dic[1])
    else:
        answer.append(0)
    
    return answer