import math

def solution(str1, str2):
    str1_arr, str2_arr = [], []
    inter, union = 0, 0

    #공백, 숫자, 특수문자 제거 & 소문자로 변환
    for i in range(len(str1)-1):
        tmp = str1[i:i+2].lower()
        if tmp.isalpha():
            str1_arr.append(tmp)
        
    for j in range(len(str2)-1):
        tmp = str2[j:j+2].lower()
        if tmp.isalpha():
            str2_arr.append(tmp)

    #다중집합 교집합
    str2_copy = str2_arr.copy()
    for s in str1_arr:
        if s in str2_copy:
            inter += 1
            str2_copy.remove(s)
    
    #다중집합 합집합
    union = len(str1_arr) + len(str2_arr) - inter
    
    if union == 0: return 65536
    res = math.trunc((inter/union) * 65536)
    
    return res

print(solution("FRANCE","french"))