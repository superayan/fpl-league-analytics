#!/usr/bin/env python3
import json
import urllib.request

# Private
def formatLeagueData(leagueData):
    name = leagueData.get("league").get("name")
    rank = leagueData.get("league").get("rank")
    members = leagueData.get("standings").get("results")
    return {
        "name": name,
        "rank": rank,
        "members": members,
    }

# Fetches data from the given url and converts the data into json
# Private
def fetchRequest(url):
    request = urllib.request.urlopen(url)
    data = request.read()
    print("Successfuly fetched data")
    return json.loads(data.decode('utf-8'))

# Takes in a player id, and returns player data
# Private
def fetchPlayerData(playerId):
    print("Attempting to fetch data for plyaer: " + str(playerId))
    plyaerUrl = "https://fantasy.premierleague.com/api/entry/%s/history/" % playerId
    return fetchRequest(plyaerUrl)

# Takes in player details, gets their weekly data and creates a user object
# Private
def getPlayerData(playerDetails):
    name = playerDetails.get("player_name")
    playerId = playerDetails.get("entry")
    playerData = fetchPlayerData(playerId)
    return {
        "name": name,
        "id": playerId,
        "weeklyData": playerData,
    }
    
# Takes in a array of player details and fetches their weekly data
def getAllPlayerDetails(playerArray):
    arrayToReturn = []
    for player in playerArray:
        arrayToReturn.append(getPlayerData(player))
    return arrayToReturn
    


# Takes in the league id, and returns league name, rank, and members
def getLeagueDetails(leagueId):
    print("Attempting to fetch data for league: " + str(leagueId))
    leagueUrl = "https://fantasy.premierleague.com/api/leagues-classic/%s/standings" % leagueId
    return formatLeagueData(fetchRequest(leagueUrl))



