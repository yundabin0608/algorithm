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
    q = deque([[startX, startY, 1]])
    visited[startY][startX] = 1

    while q:
        x, y, dist = q.popleft()

        if [x, y] == [endX, endY]: return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] == 1
                q.append([nx, ny, dist + 1])
    return float('inf')


while arrive < m:
    time += 1
    # 1번 -> 최단거리로 1칸만 움직이기 = 이동 순간마다 최단 거리 구해야할 듯
    for idx in people.keys():
        if people[idx][0] == [] or people[idx][2]: continue
        # 4방향으로 이동했을 경우 이때마다의 최단 거리 구하기
        result = []
        for i in range(4):
            nowX, nowY = people[idx][0][0] + dx[i], people[idx][0][1] + dy[i]
            if 0<=nowX<n and 0<=nowY<n:
                result.append([bfs(nowX, nowY, people[idx][1][0], people[idx][1][1]), i, [nowX, nowY]])
        result.sort()
        people[idx][0] = result[0][2]

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
        result = []
        for idx, bc in enumerate(baseCamp):
            result.append([bfs(bc[0], bc[1], dist[0], dist[1]) ,idx,bc])
        # 최단거리로 편의점들의 최단거리 > 우선 bc 순 정렬 후 택
        result.sort()
        people[time][0] = result[0][2]
        baseCamp.remove(result[0][2])
        board[result[0][2][1]][result[0][2][0]] = 1

print(time)