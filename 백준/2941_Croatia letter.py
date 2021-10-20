word = str(input())
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alpha in croatian:
        word = word.replace(alpha, "*")

print(len(word))