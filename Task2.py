def merge(n1,n2,m,n):
    n2.extend(n1[:m])
    print(sorted(n2))

merge([0], [1],0,1)

# Time -> O(n log n)

# Space -> O(1) as no new array was used... But yes, It takes 
# M number of spaces while extending the two arrays