# https://neetcode.io/problems/string-encode-and-decode

class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s #str해줘야한다. 자체 형변환 안됨
        return res

    def decode(self, s):
        res = []
        i = 0      
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
