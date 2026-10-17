class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        elements=[]
        while k>0:
            elements.append(max(dict.items(),key=lambda item:item[1])[0])
            dict.pop(max(dict.items(),key=lambda item:item[1])[0])
            k-=1
        return elements