def solution(id_list, report, k):
    answer = []
    
    singo_dict = dict()
    report_dict = dict()
    for r in report:
        a = r.split()[0]
        b = r.split()[1]
        if a in report_dict:
            if b in report_dict[a]:
                continue
            else:
                report_dict[a].add(b)
        else:
            b_set = set()
            b_set.add(b)
            report_dict[a] = b_set
        
        if b in singo_dict:
            singo_dict[b] += 1
        else:
            singo_dict[b] = 1
            
    for id_ in id_list:
        count = 0
        if id_ in report_dict:
            for b in report_dict[id_]:
                if b in singo_dict and singo_dict[b] >= k:
                    count += 1
        answer.append(count)
        
    
    return answer