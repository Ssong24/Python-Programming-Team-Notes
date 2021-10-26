import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선의 개수 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결된 노드 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(graph, start, distance):
    q = []  # 우선순위 큐를 위한 공간을 배열로 초기화
    heapq.heappush(q, (0,start))  # (거리, 출발노드)
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드라면 무시 (코드적 의미는 이전에 업데이트 거리가 더 작으면 그냥 패쓰)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들읋 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(graph, start, distance)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY", end=' ')
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i], end=' ')
