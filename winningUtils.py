#!/usr/bin/env python3

# sets up the initial object
def setUpPlayerObject(playersArray, numberOfWeeks, weeklyEntryCost):
    dictToReturn = {}
    defaultScore = numberOfWeeks * weeklyEntryCost * -1
    for player in playersArray:
        dictToReturn.update({player: defaultScore})
    return dictToReturn

def addWinningsData(initalWinningsData, weeklyWinnings, firstPlaceWinAmmount, secondPlaceWinAMount):
    finalWinnings = initalWinningsData
    for winnings in weeklyWinnings:
        first = winnings.get('first')
        second = winnings.get('second')

        firstOldPoints = finalWinnings.get(first.get('name'))
        firstNewPoints = firstOldPoints + firstPlaceWinAmmount
        finalWinnings.update({first.get('name'): firstNewPoints})

        secondOldPoints = finalWinnings.get(second.get('name'))
        secondNewPoints = secondOldPoints + secondPlaceWinAMount
        finalWinnings.update({second.get('name'): secondNewPoints})
    return finalWinnings
