class Solution:

    def encode(self, strs: list[str]) -> str:
        ret = ""
    
        for iString in strs:
            length = len(iString)
            encoded = str(length) + "#" + iString
            ret += encoded

        return ret
            
        

    def decode(self, s: str) -> list[str]:
        length = ""
        ret = []

        i = 0
        while i < len(s):
            if s[i] != '#':
                length += s[i]
                i+=1
            else:
                length = int(length)
                out = s[i + 1:i+length+1]
                ret.append(out)
                i = i + length + 1
                length = ""

        return ret