def funnyString(s):
    for a in range(len(s)//2):
        b=a+1
        z=len(s)-1-a
        y=len(s)-1-b
        if abs(ord(s[a])-ord(s[b]))!=abs(ord(s[z])-ord(s[y])):
            return "Not Funny"
    return "Funny"
