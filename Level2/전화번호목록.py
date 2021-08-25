phone_book = ["119", "97674223", "1195524421"]
def solution(phone_book): #다시 풀어보기
    answer = True
    phone_book.sort()
    temp_str = []
    temp1 = len(phone_book[0])
    
    for i in range(0, len(phone_book)):
        if temp1 >= len(phone_book[i]):
            temp1 = len(phone_book[i])
    '''
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if j == i:
                pass
            else:
                if phone_book[i][:temp1] == phone_book[j][:temp1]:
                    answer = False
                    break
    '''
    
    for i in range(0, len(phone_book)):
        temp_str.append(phone_book[i][:temp1])
    for i in range(0, len(temp_str)):
        if temp_str.count(temp_str[i]) >= 2:
            return False
    
     
    return answer
solution(phone_book)