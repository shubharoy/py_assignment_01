### -----------Assignment-1 : Problem 04 : Remove 20 from the list----------###
givenList = [5,20,15,20,25,50,20]
newList = []
for i in range(len(givenList)):
    if givenList[i] != 20:
        newList.append(givenList[i])
print(newList)