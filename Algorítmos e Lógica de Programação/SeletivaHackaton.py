
def sortByOne(n):
  return str(n).count('1')

def hack(n, k):
  numList = []
  for x in range(2**n):
    numList.append(bin(x))
  orderedList = sorted(numList, key=sortByOne, reverse=True)
  print(orderedList)
  return orderedList[k-1]

print(hack(22, 33))