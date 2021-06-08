#!/usr/bin/env python3
from teamCalculations import createAthleteCollection

# Private
def formatLeagueDetailsString(leagueDetails):
    name = "League Name: " + leagueDetails.get("name") + "\n"
    rank = "League Rank: " + str(leagueDetails.get("rank")) + "\n"
    return (name + rank + "\n")
# Private
def getTopAthletes(teamCollection):
    top5Array = []
    top2CaptainArray = []
    # loop through the athletes
    for athleteId in teamCollection.keys():
        athlete = teamCollection.get(athleteId)

        for index in range(5):
            if(index > len(top5Array)):
                break
            if(index == len(top5Array)):
                top5Array.insert(index, athlete)
                break
            top = top5Array[index]
            if(len(athlete.partOfTeams) > len(top.partOfTeams)):
                top5Array.insert(index, athlete)
                break
        for index in range(2):
            if(index > len(top2CaptainArray)):
                break
            if(index == len(top2CaptainArray)):
                top2CaptainArray.insert(index, athlete)
                break
            top = top2CaptainArray[index]
            if(len(athlete.captaineByTeams) > len(top.captaineByTeams)):
                top2CaptainArray.insert(index, athlete)
                break
    return {
        "topAthletes": top5Array[0:5],
        "topCaptains": top2CaptainArray[0:2]
    }


# Takes all the athlets and calculates the
# 1) Most common 5 athletes
# 2) Most captained 2 athletes
# Privates
def doAthelteAnalytics(teamCollection):
    toppers = getTopAthletes(teamCollection)
    toReturn = "The 5 most common players are: \n"
    for a in toppers.get("topAthletes"):
        toReturn += "\t" + str(a.name) + ": " + a.getTeamsIAmAPartOf() + "\n\n"
    toReturn += "The 2 most common captains are: \n"
    for b in toppers.get("topCaptains"):
        toReturn += "\t" + str(b.name) + ": " + b.getTeamsIAmACaptainOf() + "\n\n"

    return toReturn



# Gets the highest and lowest points, the average and if more than 1 transfer
#private
def doWeekAnalytics(playerDetails):
    latestWeek = len(playerDetails[0].get("weeklyData").get("current")) - 1
    totalNumberOfPlaters = len(playerDetails)
    lowestPoints = {"name": "", "points": 10000}
    highestTeamValue = {"name": "", "value": 0, "isTied": False}
    totalPoints = 0
    transferPerformed = []

    #loop through each player
    for player in playerDetails:
        weekData =  player.get("weeklyData").get("current")[latestWeek]
        currentPoints = weekData.get("points")
        bankValue = weekData.get("value")
        if(currentPoints < lowestPoints.get("points")):
            lowestPoints["name"] = player.get("name")
            lowestPoints["points"] = currentPoints
        totalPoints += currentPoints
        if(bankValue == highestTeamValue.get("value")):
            highestTeamValue["isTied"] = True
        elif(bankValue > highestTeamValue.get("value")):
            highestTeamValue["name"] = player.get("name")
            highestTeamValue["value"] = bankValue
            highestTeamValue["isTied"] = False

    average = totalPoints/totalNumberOfPlaters
    toReturn = "Lowest points: " + lowestPoints.get("name") + ", " + str(lowestPoints.get("points")) + "\n\n"
    toReturn += "Average points: " + str(average) + "\n\n"
    toReturn += "Highest Valued Team: " + highestTeamValue.get("name") + ", £" + str(highestTeamValue.get("value")/10) + "\n\n"

    return toReturn



def formatLatestWeekString(weeklyWinnings, playerDetails, teamCollection):
    toReturn = ""
    latestWeek = len(weeklyWinnings)
    toReturn += "Current Week: " + str(latestWeek) + ":\n\n"
    if latestWeek > 0:
        latestWinners = weeklyWinnings[latestWeek - 1]
        first = latestWinners.get("first")
        second = latestWinners.get("second")
        firstPlaceString = "First Place is " + first.get("name") + " with points: " + str(first.get("points")) + "\n\n"
        secondPlaceString = "Second Place is " + second.get("name") + " with points: " + str(second.get("points")) + "\n\n"
        toReturn = toReturn + firstPlaceString + secondPlaceString
    toReturn += doWeekAnalytics(playerDetails)
    toReturn += doAthelteAnalytics(teamCollection)
    return toReturn + "\n"

# Performs analytics on the league data, and returns a string to be output
def generateAnalyticsOutputText(leagueDetails, playerDetails, weeklyWinnings, playerEventData, athleteNames):
    teamCollection = createAthleteCollection(playerEventData, athleteNames)
    toReturn = ""
    toReturn += formatLeagueDetailsString(leagueDetails)
    toReturn += formatLatestWeekString(weeklyWinnings, playerDetails, teamCollection)
    return toReturn
