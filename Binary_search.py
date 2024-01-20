import math


def binary_search(list,key,low,high):
    if high < low:
        return -1
    #find the mid and compare with key
    mid_index = (low + high) // 2
    if list[mid_index] == key:
        return mid_index
    elif key < list[mid_index]:
        return binary_search(list,key,low, mid_index -1)
    else:
        return binary_search(list,key,mid_index +1, high)
    

if __name__ == '__main__':
    key = 72
    my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(binary_search(my_list,key,0,len(my_list)-1))