# sorted 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

result1 = sorted(array) # 오름차순
result2 = sorted(array, reverse=True) #내림차순

print(result1)
print(result2)

# ------------------------------ #
# sort 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

array.sort()  # 오름차순
print(array)

array.sort(reverse=True)  # 내림차순
print(array)

# ------------------------------ #
# key를 활용한 소스코드
array=[('이순신', 2), ('홍길동', 5), ('신사임당', 3)]

def setting(data):
  return data[1]

result1 = sorted(array, key=setting)
result2 = sorted(array, reverse=True, key=setting)

print(result1)
print(result2)
