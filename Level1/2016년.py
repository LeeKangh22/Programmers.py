def solution(a, b):
    date = 0
    if a == 1:
        date = 0
    elif a == 2:
        date = 31
    elif a == 3:
        date = 60
    elif a == 4:
        date = 91
    elif a == 5:
        date = 121
    elif a == 6:
        date = 152
    elif a == 7:
        date = 182
    elif a == 8:
        date = 213
    elif a == 9:
        date = 244
    elif a == 10:
        date = 274
    elif a == 11:
        date = 305
    elif a == 12:
        date = 335
    date += b 
    result = date % 7
    print(date)
    print(result)
    if result == 1:
        return "FRI"
    elif result == 2:
        return "SAT"
    elif result == 3:
        return "SUN"
    elif result == 4:
        return "MON"
    elif result == 5:
        return "TUE"
    elif result == 6:
        return "WED"
    elif result == 0:
        return "THU"
    
solution(1,1)
