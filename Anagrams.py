def anagrams(s1,s2):
    return sorted(s1)==sorted(s2)

s1=(input())
s2=(input())
if anagrams(s1,s2):
    print("true")
else:
    print("false")
