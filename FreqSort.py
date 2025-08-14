class Solution:
    def frequencySort(self, s: str) -> str:
        dict={}
        n=len(s)
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        bucket=[[] for i in range(n)]
        for key in dict:
            bucket[dict[key]-1].append(key*dict[key])
        s=[]
        for i in range(n-1,-1,-1):
            s.extend(bucket[i])
        return "".join(s)