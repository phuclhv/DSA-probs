
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
def primeFactor(value):
  primeArr = [2]
  def checkPrime(num):
    for i in range(len(primeArr)):
      if num % primeArr[i] == 0:
        return False
      if primeArr[i] >= math.sqrt(num):
        return True
    return True

  currNum = 3
  res = value
  while value != 1:
    if checkPrime(currNum):
      primeArr.append(currNum)
      while (value % currNum == 0):
        value = value // currNum
        res = currNum
    currNum += 2
  return res

print(primeFactor(600851475143))
      
