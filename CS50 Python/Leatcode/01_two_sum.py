# ----------------------------------------------------------------------

# def twosum(num, target):
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             if (i!=j and num[i] + num[j] == target):
#                 return [i,j]
#     return []
            
# print(twosum([3,2,4], 6))

# -----------------------------------------------------------------------
# Using Hashmap

def twosum(num, target):
    prevMap = {} # val: index
    for i,n in enumerate(num):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
    return

print(twosum([3,2,4], 6))