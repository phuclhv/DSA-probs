
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
def primeFactor(value):
  primeArr = []
  primeFactor = []
  def checkPrime(num):
    for i in range(len(primeArr)):
      if num % primeArr[i] == 0:
        return False
      if primeArr[i] >= math.sqrt(num):
        return True
    return True

  currNum = 2
  while value != 1:
    if checkPrime(currNum):
      primeArr.append(currNum)
      print(primeArr)
      currNum += int(round(math.sqrt(currNum)))
      while (value % currNum == 0):
        primeFactor.append(currNum)
        value = int(value/currNum)
        print(value)
    else:
      currNum += 1
  
  return primeFactor

print(primeFactor(600851475143))
      
