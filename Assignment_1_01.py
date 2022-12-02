
### -----------Assignment-1 : Problem 01 ----------###
print("Enter maximum 5 Interger Item. Pointer input will be turn into integer value")
print("\n")
totalSumItem = []
firstItemList = []
secondItemList = []
for firstVal in range(5):
    countFirst = firstVal + 1
    firstInput = int(float(input("Enter First List Item : ")))
    #firstInput = int(firstRawInput)
    firstItemList.append(firstInput)
    if countFirst == 5:
        break
print("\n")
for secondVal in range(5):
    countSecond = secondVal + 1
    secondInput = int(input("Enter Second List Item : "))
    secondItemList.append(secondInput)
    if countSecond == 5:
        break
print("\n")
for sumVal in range(5):
    totalSum = firstItemList[sumVal] + secondItemList[sumVal]
    totalSumItem.append(totalSum)

print(totalSumItem)



