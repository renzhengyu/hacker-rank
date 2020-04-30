def stones(n, a, b):
    if a==b:
        return [(n-1)*a]
    else:
        low = a if a<b else b
        delta = abs(a-b)
        hi = low+delta
        result = []
        i = (n-1)*low
        while i<=(n-1)*hi:
            result.append(i)
            i += delta
        return result


print(stones(73,25,25))