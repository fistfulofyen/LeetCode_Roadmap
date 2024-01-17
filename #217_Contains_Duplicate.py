list1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
list2 = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

def find_dup(list):
    if len(list) < 2:
        return False
    
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j] :
                return True
        
    return False

find_dup(list1)

def find_dup(list):
    if len(list) < 2:
        return False
    
    list.sort()
    for i in range(1,len(list)):
        if list[i] == list[i-1]:
            return True
    return False

find_dup(list2)

def find_dup(list):
    dic = {}
    for num in list:
        if num in dic and dic[num] >= 1:
            return True
        dic[num] = dic.get(num,0) +1
    
    return False


find_dup(list2)
