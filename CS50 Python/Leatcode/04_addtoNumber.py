# l1 = [1,2,3]
# l2 = [5,6,7]

# # l3 = l1[::-1]
# # l4 = l2[::-1]

# # s=[str(i) for i in l3]

# s= "".join(l1)
# print(s)




def addToNumber(l1,l2):
    l3 = l1[::-1]
    l4 = l2[::-1]
    temp1 = [str(i) for i in l3] 
    temp2 = [str(j) for j in l4]
    temp1 = "".join(temp1)
    temp2 = "".join(temp2)
    return [int(temp1) + int(temp2)]
print(addToNumber([2,4,3],[5,6,4]))