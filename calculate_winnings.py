#!/usr/bin/env python3
from getData import getLeagueDetails, getPlayerNameArray
from fileIO import readFileAndConvertToJSON
from winningUtils import setUpPlayerObject, addWinningsData
import os

weeklyEntryCost = 200
firstPlaceWinAmmount = 1500
secondPlaceWinAMount = 700

def main():
    # 1) Fetch league details
    leagueDetails = getLeagueDetails(73611)

    # 2) Extract list of players
    playersArray = getPlayerNameArray(leagueDetails.get("members"))

    # 3) Read weekly winnings json
    working_directory = os.getcwd()
    file_path = os.path.join(working_directory, 'FinalWeeklyWinning/weeklyWinnings.json')
    finalWeeklyWinnings = readFileAndConvertToJSON(file_path)
    numberOfWeeks = len(finalWeeklyWinnings)

    # 4) create the object to return
    initialPlayerWinningData = setUpPlayerObject(playersArray, numberOfWeeks, weeklyEntryCost)


    # 5) Add winning data
    finalData = addWinningsData(initialPlayerWinningData, finalWeeklyWinnings, firstPlaceWinAmmount,secondPlaceWinAMount)
    

    print(finalData)

if __name__ == "__main__":
    main()
