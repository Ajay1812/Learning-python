def isMatch(str):
    if first.startswith(match_str) and second.startswith(match_str) and third.startswith(match_str):
        match = True
    else:
        match = False
    return match

words = ["dog","racecar","car"]
# test = ["dog","racecar","car"]
def longestCommonPrefix(words):
    first = words[0] 

    index = 1
    for _ in first:
        match_str = first[:index]
        
        match_result = isMatch(match_str)
        if match_result:
            index = index + 1
        else:
            if index != 1:
                return first[:index -1]
            else:
                return ""
















# count = 1
# while True:
    
#     # match = 0
#     chosen=words[0][:count]
#     for word in words:
#         if word.startswith(chosen):
#             match = True
#         else:
#             match = False 
#     if match:
#         count = count + 1
#     else:
#         print(words[0][:count-1])
#         break


    

# chosen=words[0][:1]
# print(words[0].startswith("f"))




        








# def longestCommonPrefix(l):
    


# print(longestCommonPrefix(["flower","flow","flight"]))