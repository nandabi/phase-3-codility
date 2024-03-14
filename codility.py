  # In this scenario we are finding a matching character in a strings list
  # List of strings given "s",,,comparing each S[i] and S[j]
  # If matching character is found in both strings then matching character along with the indices of the strings is added to the result
  # First result is returned if no matching character are fund then  no list is returned or an empty list is returned 
  
  
   def solution(S):
    result=[ ]
  # Iterate each string in S    
    for i in range(len(S)):
        for j in range(i+1, len(S)):
        # Iterate characters in the strings
    for k in range(len(S[i])):
        
    if S[i][k] == S[j][k]:
        # Add indices to results
        result.append([i, j, k]) 
        # Return first matching indices
        return result[0]
  # Return empty list if no matching characters are found 
    return []

print(solution(["abc","bca","dbe"]))  # Expected: [0, 2, 1]
print(solution(["zzzz","ferz","zdsr","fgtd"]))  # Expected: [0, 1, 3]
print(solution(["gr","sd","rg"]))  # Expected: []
print(solution(["bdafg","ceagi"]))  # Expected: [0, 1, 2]