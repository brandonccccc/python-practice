import operator
n = int(input())
books = {}
for i in range(n):
    name = input()
    if name not in books:
        books[name] = 1
    else:
        books[name] += 1
    
books = dict(sorted(books.items()))
books = sorted(books.items(), key = operator.itemgetter(1), reverse=True)

print(books[0][0])