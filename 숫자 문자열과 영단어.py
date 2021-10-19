def solution(s):
    answer = ''
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    tmp = ''
    
    for v in s:
        if v.isdigit():
            answer += v
            continue
        else:
            tmp += v
            if tmp in words:
                answer += str(words.index(tmp))
                tmp = ''
            
    return int(answer)


print(solution("2three45sixseven"))