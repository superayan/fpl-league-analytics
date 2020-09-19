#!/usr/bin/env python3
import json

## Array contains highest and second highest data
# Private
gameWeeks= []

## gets the total point of your week
# Private
def getTotalPoints(week):
    rawPoints = week.get('points')
    transferCost = week.get('event_transfers_cost')
    return rawPoints - transferCost

## sets up the new week
# Private
def setUpNewWeek(name, totalPoints):
    gameWeeks.append({
        "first": {
            "points": totalPoints,
            "name": name,
        },
        "second": {
            "points": -100,
            "name": "",
        },
    })

## Takes in the position, weekNuumber, user name and total points
## Sets for the weekNumber index of gameWeeks and it's given position
## The name and totalPoints
# Private
def setUserPointsAndName(weekNumber, position, name, totalPoints):
    gameWeeks[weekNumber][position]["points"] = totalPoints
    gameWeeks[weekNumber][position]["name"] = name

# Takes the weeknumber, the total points and the name
# Checks if the person got first or second positio that week
# Private
def addToGameWeeks(weekNumber, name, totalPoints):
    if (len(gameWeeks) < (weekNumber + 1)):
        setUpNewWeek(name, totalPoints)
    else:
        currentWeekFirstPoints = gameWeeks[weekNumber].get("first").get("points")
        currentWeekFirstName = gameWeeks[weekNumber].get("first").get("name")
        currentWeekSecondPoints = gameWeeks[weekNumber].get("second").get("points")
        #print("for week " + str(weekNumber) + " first place has " + str(currentWeekFirstPoints)  + " second place has " + str(currentWeekFirstPoints))
        # case 1: if points are greater that first and second place
        # Put current user as first place and previous first place user as second place
        if (totalPoints >= currentWeekFirstPoints) and (totalPoints > currentWeekSecondPoints):
            setUserPointsAndName(weekNumber, "second", currentWeekFirstName, currentWeekFirstPoints)
            setUserPointsAndName(weekNumber, "first", name, totalPoints)
        elif (totalPoints < currentWeekFirstPoints) and (totalPoints > currentWeekSecondPoints):
            # case 2: more than second place, less than first place
            # update second place with current user and their points
            setUserPointsAndName(weekNumber, "second", name, totalPoints)
            # print('updating second place for gameweek ' + str(weekNumber))


def checkEachWeek(name, weeks):
    for i in range(len(weeks)):
        totalPoints = getTotalPoints(weeks[i])
        #print('Total points for week ' + str(i + 1) + ' for ' + name + ' is ' + str(totalPoints))
        addToGameWeeks(i, name, totalPoints)

def getGameWeeks():
    return gameWeeks
    



    
