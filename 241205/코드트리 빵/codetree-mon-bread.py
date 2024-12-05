import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, -1, 1, 0], [-1, 0, 0 ,1]
n, m = map(int, input().split())
board, baseCamp, people = [[0]*n for _ in range(n)], [], {}
time, arrive = 0, 0

for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(n):
        if tmp[x] == 1 : baseCamp.append([x, y])

for idx in range(m):
    y, x = map(int, input().split())
    people[idx+1] = [[], [x-1, y-1], False]

def bfs(startX, startY, endX, endY):
    visited = [[0]*n for _ in range(n)]
    q = deque([[startX, startY, 0]])
    visited[startY][startX] = 1

    while q:
        x, y, dist = q.popleft()
        if [x, y] == [endX, endY]:
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([nx, ny, dist + 1])
    return float('inf')

while arrive < m:
    time += 1
    # 1번 -> 최단거리로 1칸만 움직이기 = 이동 순간마다 최단 거리 구해야할 듯
    for idx in people.keys():
        if people[idx][0] == [] or people[idx][2]: 
            continue
        min_dist, result = float('inf'), []
        for i in range(4):
            nowX, nowY = people[idx][0][0] + dx[i], people[idx][0][1] + dy[i]
            if 0<=nowX<n and 0<=nowY<n:
                dist = bfs(nowX, nowY, people[idx][1][0], people[idx][1][1])
                if dist < min_dist:
                    min_dist = dist
                    result = [nowX, nowY]
        
        people[idx][0] = result

        if people[idx][0] == people[idx][1]:
            people[idx][2] = True
            arrive += 1

    # 2번 사람 도착한 편의점은 비활성화
    for idx in people.keys():
        if people[idx][2]:
            board[people[idx][1][1]][people[idx][1][0]] = 1

    # 3번 -> 베이스캠프 배정
    if time <= m:
        dist = people[time][1]
        min_dist, result = float('inf'), []
        for idx, bc in enumerate(baseCamp):
            dist_to_camp = bfs(bc[0], bc[1], dist[0], dist[1])
            if dist_to_camp < min_dist:
                min_dist = dist_to_camp
                result = bc
        
        people[time][0] = result
        baseCamp.remove(result)
        board[result[1]][result[0]] = 1

print(time)

# 메모리초과..
# sort 때문인거 같아서 없애봄..