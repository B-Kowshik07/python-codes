def non_repeat_char(string):
    freq={}
    for char in string:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1

    for char in string:
        if freq[char]==1:
            return char
    return None

string=input()
print(non_repeat_char(string))