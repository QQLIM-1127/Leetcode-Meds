class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L=0
        dict={}
        n=len(fruits)
        res=0
        number=0
        for i in range(n):
            if fruits[i] not in dict:
                dict[fruits[i]]=1
                number+=1
            else:
                dict[fruits[i]]+=1
            if number>2:
                while number>2:
                    dict[fruits[L]]-=1
                    if dict[fruits[L]]==0:
                        dict.pop(fruits[L])
                        number-=1
                    L+=1
            res=max(res,i-L+1)
        return res