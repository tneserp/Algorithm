from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input().strip())

ability = [list(map(int, input().split())) for _ in range(N)]

person = [i for i in range(N)]
ans = float("inf")
for team in combinations(person, N // 2):

    team1 = 0
    team2 = 0

    for i, j in combinations(team, 2):
        team1 += ability[i][j] + ability[j][i]

    for i, j in combinations(set(person) - set(team), 2):
        team2 += ability[i][j] + ability[j][i]

    ans = min(ans, abs(team1 - team2))

print(ans)
