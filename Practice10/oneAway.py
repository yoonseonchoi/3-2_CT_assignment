import sys

def oneAway(s1:str, s2:str) -> bool:
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if s1 == s2:
        return True
    if len(s1) - len(s2) > 1:
        return False
    elif len(s1) - len(s2) == 1:
        for i in range(len(s1)):
            if s1[:i] + s1[i+1:] == s2:
                return True
        return False
    else:
        diff = sum(1 for i in range(len(s1)) if s1[i] != s2[i])
        return diff < 2

if __name__ == '__main__':
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    print(oneAway(s1, s2))
