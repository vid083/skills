def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
recursion(6)

OUTPUT: 
Recursion Example Results
1
3
6
10
15
21