# 재귀 함수로 구현한 이진탐색
def binary_search(array, target, start, end):
  """
  array: 오름차순으로 정렬된 배열
  target: 찾아야할 원소
  start: 배열의 특정범위에서 첫 원소의 Index
  end: 배열의 특정범위에서 끝 원소의 Index
  """
  if start > end:
    return None
  mid = (start + end) // 2

  # 중간값 부터 체크
  if array[mid] == target:
    return mid
  # 중간점 값보다 target이 작은 경우, 왼쪽 확인
  if array[mid] > target:
    return binary_search(array, target, start, mid-1)
  # 중간점 값보다 target이 큰 경우, 오른쪽 확인
  if array[mid] < target:
    return binary_search(array, target, mid +1, end)
  
# n(원소의 개수)과 target(찾고자 하는 원소)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result is None:
  print("원소가 존재하지 않습니다.")
else:
  print('target 원소의 index: ', result)
