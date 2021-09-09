def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        for j in range(i, len(prices)):
            if prices[i] > prices[j] or j == len(prices) - 1:
                answer.append(j - i)
                break
    return answer


