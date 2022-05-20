def drawStars(n, x):
    table = []
    if n == 3:
        return x
    else:
        for i in x:
            table.append(i*3)
        for i in x: 
            # 중간에 x, 즉 n-1 에서 찍은 별 리스트의 길이를 곱하면 빈 공간의 길이가 딱 나온다. 
            # 왜냐하면 딱 n//3의 길이로 리스트가 구성되기 때문이다.
            table.append(i+' '*len(x)+i)
        for i in x:
            table.append(i*3)
        return drawStars(n//3, table)
    
n = int(input())
table_3 = ['***', '* *', '***']
table_n = drawStars(n, table_3)
for i in table_n:
    print(i)
    
# 이 문제는 여러가지 답이 있었지만 재귀적으로 푼 답을 찾아보았다.
# 처음에는 위 답이 맘에 들지 않았지만...
# for 문을 이용해서 어떤 특정 상황에는 별을 찍지 않는 방법은
# 재귀적으로 푼 문제가 아니라고 생각했고 돌고 돌아 다시 위 답을보니
# 위 답이 재귀적으로 푼 문제더라... 
