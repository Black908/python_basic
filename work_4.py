import random

# ran = random.randint(1, 999999)
# print(ran)

countDic = {}
for x in range(0, 999):
    ran = random.randint(1, 999999)
    if str(ran)[-1] == "1":
        if 1 in countDic:
            countDic[1] += 1
        else:
            countDic[1] = 1
    elif str(ran)[-1] == "2":
        if 2 in countDic:
            countDic[2] += 1
        else:
            countDic[2] = 1
    elif str(ran)[-1] == "3":
        if 3 in countDic:
            countDic[3] += 1
        else:
            countDic[3] = 1
    elif str(ran)[-1] == "4":
        if 4 in countDic:
            countDic[4] += 1
        else:
            countDic[4] = 1
    elif str(ran)[-1] == "5":
        if 5 in countDic:
            countDic[5] += 1
        else:
            countDic[5] = 1
    elif str(ran)[-1] == "6":
        if 6 in countDic:
            countDic[6] += 1
        else:
            countDic[6] = 1
    elif str(ran)[-1] == "7":
        if 7 in countDic:
            countDic[7] += 1
        else:
            countDic[7] = 1
    elif str(ran)[-1] == "8":
        if 8 in countDic:
            countDic[8] += 1
        else:
            countDic[8] = 1
    elif str(ran)[-1] == "9":
        if 9 in countDic:
            countDic[9] += 1
        else:
            countDic[9] = 1

print(countDic)
