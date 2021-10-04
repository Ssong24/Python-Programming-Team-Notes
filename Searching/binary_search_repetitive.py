# 반복문을 이용한 이진탐색 소스코드
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    # 중간점 값부터 체크
    if array[mid] == target:
      return mid
    
    # target이 중간점 값보다 작은 경우, 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    # target이 중간점 값보다 큰 경우, 오른쪽 확인
    else:
      start = mid + 1

  return None

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
