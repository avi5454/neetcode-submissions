class Solution:

    def encode(self, strs: List[str]) -> str:
        modified=[]
        for i in range(len(strs)):
            length=len(strs[i])
            modified.append(f"{length}#{strs[i]}")
        s="".join(modified)
        return s 

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            location=s.find("#",i)
            
            length=int(s[i:location])
            
            word_start=location+1
            
            word_end=word_start+length
            
            result.append(s[word_start:word_end])
            
            i=word_end
        
        return result