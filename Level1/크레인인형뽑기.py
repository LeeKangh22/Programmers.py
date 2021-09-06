board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	

def solution(board, moves):
    answer = 0
    temp = []
    for i in range(0, len(moves)):
        k = 0
        for j in range(0, len(board)):
            if board[k][moves[i] - 1] == 0:
                k += 1
            else:
                temp.append(board[k][moves[i] - 1])
                board[k][moves[i] - 1] = 0
                break
        if len(temp) >= 2 and temp[-1] == temp[-2]:
            temp.pop()
            temp.pop()
            answer += 2    
    return answer
print(solution(board,moves))