# Example: 'programmerstringxxxprozmerqgram'
# Indices 0-9 form one 'programmer'
# Indices 13-24 form another 'programmer'
# There are 3 letters between them, so return 3.

def programmerString(s):
    str1 = 'programmer'
    str2 = 'programmer'
    L = len(s)
    i = 0
    j = L-1

    while str1 != '':   # from first to last
        c = s[i]
        if c in str1:
            str1 = str1.replace(c, '', 1)
        i = i+1
    i = i - 1   # the index is the last char of programmer

    while str2 != '':   # from last to first
        c = s[j]
        if c in str2:
            str2 = str2.replace(c, '', 1)
        j = j-1
    j = j + 1   # the index is the first char of programmer

    print(i)
    print(j)
    return j - i - 1


if __name__ == "__main__":
    s = 'programmerxxxprozmerqgram'
    result = programmerString(s)
    print(result)