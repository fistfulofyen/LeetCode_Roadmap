#using dict
def topKFrequent(nums, k):
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = dic.get(nums[i],0) +1

    #.item return each item in dict in tuple (key,value)
    sorted_dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)
    out = []
    newdic = sorted_dic[:k]
    for key in newdic:
        out.append(key[0])
    return out
    
    
topKFrequent([4,1,-1,2,-1,2,3],2)