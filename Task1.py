# def findKthLargest(nums):
#         res=0
#         for i in range(k):
#             res = max(nums)
#             nums.remove(res)
#         return res

# print()

def merge(l1,l2):
    i,j,combined=0,0,[]

    while i<len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            combined.append(l1[i])
            i+=1
        else:
            combined.append(l2[j])
            j+=1

    while i < len(l1):
        combined.append(l1[i])
        i+=1
    while j < len(l2):
        combined.append(l2[j])
        j+=1
    return combined

def merge_sort(l):
    if len(l)==1:
        return l
    mid = len(l)//2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    return merge(left,right)

def kth_element(l,k):
    arr = merge_sort(l)
    return arr[-k]


# Time ->O(n log n)
# space -> O(n)