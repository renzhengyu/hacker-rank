def pangrams(s):
    s=s.lower()
    t=[False]*26
    for c in s:
        if c!=' ':
            t[ord(c)-97]=True
    return "pangram" if all(t) else "not pangram"


print(pangrams("We promptly judged antique ivory buckles for the next prize"))