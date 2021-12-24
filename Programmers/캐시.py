def solution(cacheSize, cities):
    cities = [c.upper() for c in cities]
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            if not city in cache:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1

    return answer




cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(2, cities))