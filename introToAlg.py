import time
import random
def merge(left,right,increase):
    left_len = len(left)
    right_len = len(right)
    print 'left:',left,'right:',right
    l = r = 0
    result = []
    while l < left_len  and r < right_len :
        if increase:
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        else:
            if left[l] > right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
    if l >= left_len and r < right_len :
        result.extend(right[r:])

    else:
        if r >= right_len and l <= left_len:
            result.extend(left[l:])
    print result
    return result

def merge_sort(list,increase):
    length = len(list)
    #print length
    if length <= 1:
        return list
    else:
        r = int(length / 2)
        left = list[:r]
        right = list[r:]
        #print left
        #print right
        #recursively solve the subproblum
        left = merge_sort(left,increase)
        right = merge_sort(right,increase)
        #combine the subproblum into large one
        return merge(left,right,increase)



def heap_sort(list):
    for i in range(len(list)):
        list[i:] = build_maximum_heap(list[i:])
       # print list
    return list

def build_maximum_heap(list):
    length = len(list)
    for i in range(int(length-1) / 2,-1,-1):
        left = 2 * i +1
        right = 2 * i +2
        if(left < length):
            if(list[i] < list[left]):
                list[i] ,list[left] = list[left] , list[i]
        if(right < length):
            if(list[i] < list[right]):
                list[i] ,list[right] = list[right] , list[i]
    return list
#def insert__maximum_heap(node,heap):

if __name__ == '__main__':

    a = []
    for i in range(8):
        a.append(random.randrange(1,100))
    print a
    print heap_sort(a)
