def hackerrankInString(s):
    t = 'hackerrank'
    tp = 0
    sp = 0

    while tp<10 and sp<len(s):
        if t[tp]==s[sp]:
            tp += 1
        sp += 1
    return 'YES' if tp==10 else "NO"


