def solution(weights, head2head):
    answer = [i+1 for i in range(len(weights))]
    win_rate, win_count = [] , []
    
    for weight, score in zip(weights,head2head): 
        res = winning(weight, weights, score)
        win_rate.append(res[0])
        win_count.append(res[1])
    
    answer = sorted(zip(answer, win_rate, win_count, weights), key = lambda x: (-x[1], -x[2], -x[3]))
    
    return [i[0] for i in answer]

def winning(my_weight, weights, arr):
    
    win, lose, count = 0, 0, 0,
    
    for i in range(len(arr)):
        if arr[i] == 'W':
            win += 1
            if my_weight < weights[i]: #나보다 무거운 선수를 이겼을 경우
                count += 1
            
        elif arr[i] == 'L':
            lose += 1
    
    if win + lose == 0: #전적 없음
        return (0, count)
    else:
        return (win / (win+lose), count)

print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]))