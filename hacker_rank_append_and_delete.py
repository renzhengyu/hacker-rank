def appendAndDelete(s, t, k):
    common_length = 0
    for i in range(min(len(s),len(t))):
        if s[i]==t[i]:
            common_length += 1
        else:
            break
    
    if len(s)+len(t)-2*common_length>k:
        return "No"
    elif (len(s)+len(t)-2*common_length)%2==k%2:
        return "Yes"
    elif len(s)+len(t)<k:
        return "Yes"
    else:
        return "No"
