#!/usr/bin/env python3
from getData import getLeagueDetails, getAllPlayerDetails, getAllPlayerEventDetails, getAthleteNames, getPlayerNameArray
from weekCalculations import checkEachWeek, getGameWeeks
from fileIO import createOutPutDirectory, readFileAndConvertToJSON, writeJsonData, writeTextData
from analytics import generateAnalyticsOutputText
from winningUtils import setUpPlayerObject, addWinningsData

weeklyEntryCost = 200
firstPlaceWinAmmount = 1500
secondPlaceWinAMount = 700

def getweeklyWinnings(playerDetails):
    for player in playerDetails:
        checkEachWeek(player.get("name"), player.get("weeklyData").get("current"))
    return getGameWeeks()

def main():
    # 1) Fetch league details
    leagueDetails = getLeagueDetails(73611)

    # 2) Get details for each player
    playerDetails = getAllPlayerDetails(leagueDetails.get("members"))

    # 3) Get weekly winnings
    weeklyWinnings = getweeklyWinnings(playerDetails)

    # 4) Create output directory
    outputPath = createOutPutDirectory()

    # 5) Write Weekly Winnings Josn to output file
    writeJsonData(outputPath, weeklyWinnings, '/weeklyWinnings.json')

    # 6) Get the team of each player
    playerEventData = getAllPlayerEventDetails(leagueDetails.get("members"), len(weeklyWinnings))

    # 7) Get all playernames
    athleteNames = getAthleteNames()

    # 8) Create a readable txt file
    analysticsString = generateAnalyticsOutputText(leagueDetails, playerDetails, weeklyWinnings, playerEventData, athleteNames)
    writeTextData(outputPath, analysticsString)

    # 9) Calculate weekly winnings so far
    playersArray = getPlayerNameArray(leagueDetails.get("members"))
    numberOfWeeks = len(weeklyWinnings)
    initialPlayerWinningData = setUpPlayerObject(playersArray, numberOfWeeks, weeklyEntryCost)
    currentWinningData = addWinningsData(initialPlayerWinningData, weeklyWinnings, firstPlaceWinAmmount,secondPlaceWinAMount)
    writeJsonData(outputPath, currentWinningData, '/winningsSoFar.json')

if __name__ == "__main__":
    main()
