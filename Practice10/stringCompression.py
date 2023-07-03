def stringCompression(s:str) -> str:
    output = ''
    cnt = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            output = output + s[i-1] + str(cnt)
            cnt = 1
    output = output + s[-1] + str(cnt)
    return output

if __name__ == '__main__':
    s = 'aabcccccaaa'
    print(stringCompression(s))
