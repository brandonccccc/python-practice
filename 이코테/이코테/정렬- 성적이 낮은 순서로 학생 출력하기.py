N = int(input())
array = []
for i in range(N):
    input_data = input().split()
    # 이름은 문자열, 점수는 정수형으로 변환. 튜플로 저장
    array.append((input_data[0], int(input_data[1]))) 
# key를 이용하여 점수 기준으로 정렬    
array = sorted(array, key=lambda x: x[1])
    
for x in array:
    print(x[0], end = ' ')