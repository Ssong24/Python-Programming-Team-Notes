# 무한 수 초기화
INF = int(1e9)

# 노드 개수,간선 개수 입력받기
n,m = 4, 7  # map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용: 0 
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 간선 정보 입력 받고 초기화
# for _ in range(m):
#     # A에서 B로 가는 비용은 C라고 설정
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
graph[1][2] = 4
graph[1][4] = 6
graph[2][1] = 3
graph[2][3] = 7
graph[3][1] = 5
graph[3][4] = 4
graph[4][3] = 2

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      if a != k and b != k and a != b:
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    answer = graph[a][b]
    if answer == INF:
      print("INF", end=' ')
    else:
      print(answer, end=' ')
  print()
  
"""출력예시:
0 4  8 6
3 0  7 9
5 9  0 4
7 11 2 0"""
