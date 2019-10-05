def largestPal(value):
  maxMul = -float("inf")
  for i in range(value, 100, -1):
    for j in range (i, 100, -1):
      mulNum = i * j 
      if mulNum > maxMul:
        mulStr =str(mulNum)
        if mulStr == mulStr[::-1]:
          maxMul = mulNum
  return maxMul

print(largestPal(999))

