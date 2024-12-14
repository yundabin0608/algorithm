import sys
input = sys.stdin.readline

# N*N 격자에 서로 다른 높이를 가진 리브로수 
# 영양제 위치는 최초 좌하단 4칸, 이동 가능한데 8방향 이동
# 이동시 좌표는 모든 행, 열이 끝과 끝으로 연결되어있음

# 빡구횬

# 특수 영양제 이동 후 투입 -> 성장 ( 대각선 인접 방향에 리브로수 수만큼 + 높이)
# 투입된 부분 영양제 사라지지만 체크해두기
# 전체에서 높이 2이상 리브로수들은 높으 -2 하고 특영제 올려두기

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx, dy = [1, 1, 0, -1, -1, -1, 0, 1], [0, -1, -1, -1, 0, 1, 1, 1]
trees = [list(map(int, input().split())) for _ in range(n)]
supplements = deque([[0,n-1], [0, n-2], [1, n-1], [1, n-2]])
sup_count = 4

for _ in range(m):
    d, p = map(int, input().split())
    visited = [[False]*n for _ in range(n)]

    # 영양제 이동 + 영양제 투입
    for i in range(sup_count):
        x, y = supplements.popleft()
        newX, newY = (x+(dx[d-1]*p))%n, (y+(dy[d-1]*p))%n
        trees[newY][newX] += 1
        supplements.append([newX, newY])

    # 영양제 추가 성장 (인접 대각선 좌표넘어가는건 안따짐 -> 높이 1이상인것 갯수)
    while supplements:
        x, y = supplements.popleft() 
        visited[y][x] = True
        for i in [1, 3, 5, 7]:
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and trees[ny][nx]: 
                trees[y][x] += 1
    sup_count = 0

    # 전체돌며 높이 2 이상 리브로수는 -2 하고 영양제 표기 
    # 영양제 줬던 곳은 주면 안됨!
    for y in range(n):
        for x in range(n):
            if trees[y][x] < 2 or visited[y][x]: continue
            trees[y][x] -= 2
            sup_count += 1
            supplements.append([x, y])
print(sum(sum(trees, [])))