def count_freq(string):
    string=string.lower()
    freq={}
    for char in string:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq

string=input()
freq=count_freq(string)
for char,count in freq.items():
    print(f"{char} : {count}")
