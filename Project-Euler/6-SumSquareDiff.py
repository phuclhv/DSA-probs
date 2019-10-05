def sumSquareDiff(value):
  res = 0
  for i in range(value):
    for j in range(i+1,value):
      print(i,j)
      res += 2 * (i+1) * (j+1)
  return res

print(sumSquareDiff(100))


