import sys
sys.stdin = open('input.txt', 'r')

def solution(n):
    s = 0
    for i in range(n+1):
        s += i
    arr = [[0] * n for _ in range(n)]
    dx, dy = [1, 0, -1], [0, 1, -1]
    x, y = 0, 0
    dr = 0
    for i in range(1, s+1):
        arr[x][y] = i
        while True:
            if i == s:
                break
            nx = x + dx[dr]
            ny = y + dy[dr]
            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
                x = nx
                y = ny
                break
            else:
                dr = (dr+1)%3
    ans = []
    for i in range(n):
        for j in range(i+1):
            ans.append(arr[i][j])
    return ans

n = int(input())
print(solution(n))