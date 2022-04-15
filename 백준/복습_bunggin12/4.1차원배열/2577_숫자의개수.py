a, b, c = int(input()), int(input()), int(input())
multi_abc = str(a*b*c)

for i in range(10):
    print(multi_abc.count(str(i)))
    
# count 함수는 int 값으로 할 수 없다. str 씌워야함