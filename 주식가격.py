def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices) - 1): 
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]: #가격이 떨어짐
                answer[i] += 1
                break
            else: #가격이 오름
                answer[i] += 1
            
    return answer

print(solution([1, 2, 3, 2, 3]))