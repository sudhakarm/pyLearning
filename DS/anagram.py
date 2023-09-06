
def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    return print(sorted(s1) == sorted(s2))

anagram('god','dog')
anagram('ssss','s')
