def max_repeating_subsrting(s):
    start=max_len=0
    curr_index={}

    for end in range(len(s)):
        if s[end] in curr_index and curr_index[s[end]]>=start:
            start=curr_index[s[end]]+1

        curr_index[s[end]]=end
        max_len=max(max_len,end-start+1)

    return max_len

s=input()
print(max_repeating_subsrting(s))



