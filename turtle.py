def rev (s):
    return s[::-1].replace('(',')')
s=input()
print(s+rev(s))