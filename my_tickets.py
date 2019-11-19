import random

i = 0
total = range(1, 34)
countList = []
lastList = []
while i < 100000:
    result = random.sample(total, 6)
    countList += result
    lastList.append(random.randint(1, 16))
    i += 1
countSet = set(countList)
lastSet = set(lastList)
countDic = {}
lastDic = {}
for i in countSet:
    countDic[i] = '{}次'.format(countList.count(i))
print(countDic)
for i in lastSet:
    lastDic[i] = '{}次'.format(lastList.count(i))
sortedCount = sorted(countDic.items(), key=lambda x: x[1], reverse=True)
sortedLast = sorted(lastDic.items(), key=lambda x: x[1], reverse=True)
result = []
for i, j in (sortedCount[:6:] + sortedLast[:1:]):
    result.append(i)
print(result)