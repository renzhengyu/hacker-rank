import math
def encryption(s):
    t=math.sqrt(len(s))
    col = math.ceil(t)
    a = []
    p = 0
    for r in range(col):
        t=[]
        for c in range(col):
            t.append(s[p] if p<len(s) else "X")
            p+=1
        a.append(t)
    result = ""
    for c in range(col):
        for r in range(col):
            if a[r][c]!="X":
                result+=a[r][c]
        result+=" "
    return result
