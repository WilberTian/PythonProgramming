li = [4,7,2,9,3,5,8,1]

#insert_sort
def insert_sort(li):
    length = len(li)
    for i in range(1, length):
        j = i
        while j > 0 and li[j-1] > li[j]:
            li[j-1], li[j] = li[j], li[j-1]
            j -= 1
    return li

print insert_sort(li)    


#shell_sort
def shell_sort(li):
    length = len(li)
    inc = 2
    group = length/inc
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < length:
                k = j - group
                while k > 0 and li[k] > li[k + group]:
                    li[k+group], li[k] = li[k], li[k+group]
                    k -= group
                j += group
        group /= inc
    return li
    
print shell_sort(li)    

#selection_sort
def selection_sort(li):
    length = len(li)
    for i in range(0, length):
        min = i
        for j in range(i, length):
            if li[min] > li[j]:
                min = j
        li[i], li[min] = li[min], li[i]
    return li
    
print selection_sort(li)

#bubble_sort
def bubble_sort(li):
    length = len(li)
    for i in range(0, length):
        swap = False
        for j in range(i + 1, length):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
                swap = True
        if not swap:
            break
    return li
    
print bubble_sort(li)    


#quick_sort
def quick_sort(li):
    if len(li) < 2:
        return li
    key = li[0]
    return quick_sort([x for x in li[1:] if x < key]) +[key] + quick_sort([x for x in li[1:] if x > key])
    
print quick_sort(li)    
    
    
def quick_sort(li, left, right):
    if left >= right:
        return li
    key = li[left]
    low = left
    high = right
    while left < right:
        while left < right and li[right] >= key:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= key:
            left += 1
        li[right] = li[left]
    li[right] = key
    quick_sort(li, low, left - 1)
    quick_sort(li, left + 1, high)
    return li    
    
print quick_sort(li, 0, len(li)-1)       
    
    
#heap_sort
'''
iParent     = floor((i-1) / 2)
iLeftChild  = 2*i + 1
iRightChild = 2*i + 2
'''
def heap_sort(li):
    def ajust_heap(start, end):
        root = start
        lChild = 2*root + 1
        rChild = 2*root + 2
        
        if root < end/2:
            if lChild < end and li[lChild] > li[root]:
                root = lChild
            if rChild < end and li[rChild] > li[root]:
                root = rChild
            if root != start:
                li[start], li[root] = li[root], li[start]
                ajust_heap(root, end)
        pass
    
    def build_heap():
        for i in range(0, (len(li)/2), -1):
            adjust_heap(i, len(li))
            

    build_heap()
    for i in range(0, len(li), -1):
        li[0], li[i] = li[i], li[0]
        adjust_heap(li, 0, i)
    
    return li
    
print heap_sort(li)            
    
    
#merge_sort
def merge_sort(li):
    if len(li) < 2:
        return li
        
    def merge(left, right):
        i, j = 0, 0
        temp = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
        temp += left[i:]
        temp += right[j:]
        return temp
        
    idx = len(li)/2
    left = merge_sort(li[:idx])
    right = merge_sort(li[idx:])
    return merge(left, right)

print merge_sort(li)    
    
    
#radix_sort
import math
def radix_sort(li, radix=10):
    """li为整数列表， radix为基数"""
    K = int(math.ceil(math.log(max(li), radix))) # 用K位数可表示任意整数
    bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
    for i in range(1, K+1): # K次循环
        for val in li:
            bucket[val%(radix**i)/(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
        del li[:]
        for each in bucket:
            li.extend(each) # 桶合并
        bucket = [[] for i in range(radix)]
    return li
    
print radix_sort(li)
  
    