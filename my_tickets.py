import random

def my_ticket():
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
    for i in lastSet:
        lastDic[i] = '{}次'.format(lastList.count(i))
    sortedCount = sorted(countDic.items(), key=lambda x: x[1], reverse=True)
    sortedLast = sorted(lastDic.items(), key=lambda x: x[1], reverse=True)
    result = []
    f2 = open('./myTicket.txt', 'a')
    f2.writelines('\n')
    for i, j in sortedCount[:6:]:
        result.append(str(i).zfill(2))
        result = sorted(result)
    result.append(str(sortedLast[0][0]).zfill(2))
    f2.write(','.join(result))
    f2.close()

if __name__ == '__main__':
    t = 0
    while t < 20:
        my_ticket()
        t += 1