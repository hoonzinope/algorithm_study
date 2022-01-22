def timeCal(start, end):
    start_time = int(start.split(":")[0])
    start_min = int(start.split(":")[1])
    
    end_time = int(end.split(":")[0])
    end_min = int(end.split(":")[1])
    
    total_min = 0
    if end_min < start_min:
        end_time -= 1
        end_min+=60
        
        total_min += (end_time - start_time) * 60
        total_min += (end_min - start_min)
    else:
        total_min += (end_time - start_time) * 60
        total_min += (end_min - start_min)

    return total_min

def solution(fees, records):
    import math
    answer = []

    total_time_dict = {}
    record_dict = {}

    for record in records:
        time, carNum, InOut = record.split()
        if InOut == "IN":
            record_dict[carNum] = time
        else:
            start_time = record_dict[carNum]
            if carNum in total_time_dict:
                total_time_dict[carNum] += timeCal(start=start_time, end=time)
            else:
                total_time_dict[carNum] = timeCal(start=start_time, end=time)
            record_dict[carNum] = ""
    
    for carNum in record_dict:
        if record_dict[carNum] != "":
            start_time = record_dict[carNum]
            if carNum in total_time_dict:
                total_time_dict[carNum] += timeCal(start=start_time, end="23:59")
            else:
                total_time_dict[carNum] = timeCal(start=start_time, end="23:59")

    base_min, base_fee, unit_time, unit_fee = fees
    result = []
    for carNum in total_time_dict:
        fee = 0
        if total_time_dict[carNum] <= base_min:
            fee = base_fee
        else:
            fee = base_fee
            fee += math.ceil((total_time_dict[carNum] - base_min) / unit_time) * unit_fee

        result.append([carNum, fee])
    
    result = list(sorted(result, key= lambda x : x[0]))

    for carNum, fee in result:
        answer.append(fee)

    return answer