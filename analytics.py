#!/usr/bin/env python3

# Private
def formatLeagueDetailsString(leagueDetails):
    name = "League Name: " + leagueDetails.get("name") + "\n"
    rank = "League Rank: " + str(leagueDetails.get("rank")) + "\n"
    return (name + rank + "\n")


# Gets the highest and lowest points, the average and if more than 1 transfer
#private
def doWeekAnalytics(playerDetails):
    latestWeek = len(playerDetails[0].get("weeklyData").get("current")) - 1
    totalNumberOfPlaters = len(playerDetails)
    lowestPoints = {"name": "", "points": 10000}
    totalPoints = 0
    transferPerformed = []

    #loop through each player
    for player in playerDetails:
        weekData =  player.get("weeklyData").get("current")[latestWeek]
        currentPoints = weekData.get("points")
        if(currentPoints < lowestPoints.get("points")):
            lowestPoints["name"] = player.get("name")
            lowestPoints["points"] = currentPoints
        totalPoints += currentPoints

    average = totalPoints/totalNumberOfPlaters
    toReturn = "Lowest points: " + lowestPoints.get("name") + ", " + str(lowestPoints.get("points")) + "\n"
    toReturn += "Average points: " + str(average)
    
    return toReturn
        
    
    
def formatLatestWeekString(weeklyWinnings, playerDetails):
    toReturn = ""
    latestWeek = len(weeklyWinnings)
    toReturn += "Current Week: " + str(latestWeek) + ":\n\n"
    if latestWeek > 0:
        latestWinners = weeklyWinnings[latestWeek - 1]
        first = latestWinners.get("first")
        second = latestWinners.get("second")
        firstPlaceString = "First Place is " + first.get("name") + " with points: " + str(first.get("points")) + "\n"
        secondPlaceString = "Second Place is " + second.get("name") + " with points: " + str(second.get("points")) + "\n"
        toReturn = toReturn + firstPlaceString + secondPlaceString
    toReturn += doWeekAnalytics(playerDetails)
    return toReturn + "\n"
    
# Performs analytics on the league data, and returns a string to be output
def generateAnalyticsOutputText(leagueDetails, playerDetails, weeklyWinnings):
    toReturn = ""
    toReturn += formatLeagueDetailsString(leagueDetails)
    toReturn += formatLatestWeekString(weeklyWinnings, playerDetails)
    return toReturn
