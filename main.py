#!/usr/bin/env python3
from getData import getLeagueDetails, getAllPlayerDetails
from weekCalculations import checkEachWeek, getGameWeeks
from fileIO import createOutPutDirectory, readFileAndConvertToJSON, writeJsonData, writeTextData
from analytics import generateAnalyticsOutputText

users={
    "Rayan": "Rayan.txt",
    "Shiv": "Shiv.txt",
    "Rishabh": "Rishabh.txt",
    "Sahib": "Sahib.txt",
    "Lakshya": "Lakshya.txt",
    "Shreyas": "Shreyas.txt",
}

# Update to conver to use playerDetails
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
    writeJsonData(outputPath, weeklyWinnings)

    # 6) Create a readable txt file
    analysticsString = generateAnalyticsOutputText(leagueDetails, playerDetails, weeklyWinnings)
    writeTextData(outputPath, analysticsString)
    
    

if __name__ == "__main__":
    main()
