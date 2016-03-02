def partial_match_table(pattern):
    pattern_len = len(pattern)
    table = [0] * pattern_len
    
    k = 0
    for q in range(1, pattern_len):
        while k > 0 and pattern[k] != pattern[q]:
            k = table[k - 1]
        if pattern[k] == pattern[q]:
            k = k + 1
        table[q] = k
    return table

def kmp(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    table = partial_match_table(pattern)
    print table
    q = 0
    for i in range(text_len):
        while q > 0 and pattern[q] != text[i]:
            q = table[q - 1]
        if pattern[q] == text[i]:
            # 移动位数 = 已匹配的字符数 - 对应的部分匹配值
            q = q + 1
        if q == pattern_len:
            return i - pattern_len + 1
    return -1
    
    
print kmp("abcabcabdabba", "abcabd")    
'''
How to get the partial match table of "abcabd"?

a   
[], []  ->  0


ab
["a"], ["b"]    ->  0


abc
["a", "ab"], ["bc", "c"]    ->  0


abca
["a", "ab", "abc"], ["bca", "ca", "a"]    ->  1


abcab
["a", "ab", "abc", "abca"], ["bcab", "cab", "ab", "b"]    ->  2


abcabd
["a", "ab", "abc", "abca", "abcab"], ["bcabd", "cabd", "abd", "bd", "d"]    ->  0
'''    


