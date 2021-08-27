participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
participant.sort()
completion.sort()
print(participant)
print(completion)
i = 0
for a in participant:
    if i < len(completion) and a == completion[i]:
        i += 1
    else:
        answer = a
        break
print(answer)


"""
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]"""