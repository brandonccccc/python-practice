# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end :
        return None
    mid = (start + end) // 2
    
    #찾은 경우 중간값 인덱스 반환
    if array[mid] == target:
        return mid
    
    # 중간 점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 크면 오른쪽 확인
    if array[mid] < target:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열) 입력받기
n, target = list(map(int, input().split()))
#전체 원소 입력
array = list(map(int, input().split()))

#이진탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)