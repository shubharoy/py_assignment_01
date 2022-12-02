### -----------Assignment-1 : Problem 03 ----------###
# When there will be 100, program will add previous number with 100 and add new number to the list

givenList = [1, 100, 2, 3, 100, 4, 5, 6, 100]

newItemList = []
print("\nGiven List", givenList)
print("\n")
for val in range(len(givenList)):
    if givenList[val] == 100:        
        newItem = 100 + givenList[val-1]
        newItemList.append(newItem)
    else:
        newItemList.append(givenList[val])
print("New Item List", newItemList)