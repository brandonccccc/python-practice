v = int(input())
vote = input()
if vote.count("A") > vote.count("B"):
    print("A")
elif vote.count("A") < vote.count("B"):
    print("B")
else:
    print("Tie")