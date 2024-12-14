import sys
input = sys.stdin.readline

# n 정수가 주어지고 그 사이사이 덧뺄곱 연산자 배치 -> 순차 계산할 것이고 가능 식의 최대, 최솟값 출력하기
# 가능한 덧 뺄 곱 수가 공백을 두고 주어짐

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul = map(int, input().split())

answer = [float('inf'), -float('inf')]
def dfs(idx, result, add, sub, mul):
    if idx == n : 
        answer[0] = min(answer[0], result)
        answer[1] = max(answer[1], result)
        return
    
    if add : dfs(idx+1, result+nums[idx], add-1, sub, mul)
    if sub : dfs(idx+1, result-nums[idx], add, sub-1, mul)
    if mul : dfs(idx+1, result*nums[idx], add, sub, mul-1)

dfs(1, nums[0], add, sub, mul)
print(*answer)