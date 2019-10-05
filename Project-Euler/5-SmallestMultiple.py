import math
def smallestMultiples(value):
  primeArr = []
  primeFactor = {}

  def checkPrime(num):
    for i in range(len(primeArr)):
      if num % primeArr[i] == 0:
        return False
      if primeArr[i] >= math.sqrt(num):
        return True
    return True
  
  def brokenToPrimeFactor(num):
    idx = 0
    currPrimeFactor = {}
    
    while (num !=1):
      while (num % primeArr[idx] == 0 ):
        if primeArr[idx] in currPrimeFactor:
          currPrimeFactor[primeArr[idx]] +=1
        else:
          currPrimeFactor[primeArr[idx]] =1
        num = num / primeArr[idx]
      idx +=1

    for key, value in currPrimeFactor.items():
      if key not in primeFactor:
        primeFactor[key] = value
      else:
        primeFactor[key] = max(value, primeFactor[key])
      
  for i in range(2,value):
      if checkPrime(i):
        primeArr.append(i)
        primeFactor[i] = 0
      brokenToPrimeFactor(i)

  res = 1
  for value,occurence in primeFactor.items():
    res = res * (value**occurence)
  return res

print(smallestMultiples(20))