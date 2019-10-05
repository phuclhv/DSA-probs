
import math
def sumPrime(maxValue):
  primeArr = [1,2,3]
  
  def checkPrime(num):
    #print(primeArr)
    for i in range(1,len(primeArr)):
      if num % primeArr[i] == 0:
        return False
      if primeArr[i] >= math.sqrt(num):
        return True
    return True

  currNum = 4
  while currNum < maxValue:
    if checkPrime(currNum):
      primeArr.append(currNum)
      currNum += int(round(math.sqrt(currNum)))
    else:
      currNum += 1
  
  sumEven = 0
  idx = 0

  while idx < len(primeArr):
    sumEven += primeArr[idx]
    idx += 2

  return sumEven

print(sumPrime(100))
      
