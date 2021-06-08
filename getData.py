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

# Priavte
def formatLeaguePlayers(leagueElemets):
    toReturn = {}
    for el in leagueElemets:
        id = el.get("id")
        name = el.get("first_name") + " " + el.get("second_name")
        toReturn[id] = name
    return toReturn

# Fetches data from the given url and converts the data into json
# Private
def fetchRequest(url):
    request = urllib.request.urlopen(url)
    data = request.read()
    print("Successfuly fetched data")
    return json.loads(data.decode('utf-8'))

# Takes in a player id and event id, and returns data for the current game week, including playes in their team
# Private
def fetchPlayerEventData(playerId, eventId):
    print("Attempting to fetch event data for " + str(playerId))
    playerEventUrl = "https://fantasy.premierleague.com/api/entry/%s/event/%s/picks/" % (playerId, eventId)
    return fetchRequest(playerEventUrl)

# Takes in a player id, and returns player data
# Private
def fetchPlayerData(playerId):
    print("Attempting to fetch data for plyaer: " + str(playerId))
    plyaerUrl = "https://fantasy.premierleague.com/api/entry/%s/history/" % playerId
    return fetchRequest(plyaerUrl)


# Takes in player details, gets their current team and creates a user object
# Private
def getPlayerEventData(playerDetails, eventId):
    name = playerDetails.get("player_name")
    playerId = playerDetails.get("entry")
    playerData = fetchPlayerEventData(playerId, eventId)
    return {
        "name": name,
        "id": playerId,
        "picks": playerData.get("picks"),
    }

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


# PUBLIC METHODS

# Takes in a array of player details and fetches their team for the given event
def getAllPlayerEventDetails(playerArray, eventId):
    arrayToReturn = []
    for player in playerArray:
        arrayToReturn.append(getPlayerEventData(player, eventId))
    return arrayToReturn

# Takes in a array of player details and fetches their weekly data
def getAllPlayerDetails(playerArray):
    arrayToReturn = []
    for player in playerArray:
        arrayToReturn.append(getPlayerData(player))
    return arrayToReturn

# Returns an object containg player ids as the key and their names as the value
def getAthleteNames():
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    data = fetchRequest(url)
    return formatLeaguePlayers(data.get("elements"))

# Takes in the league id, and returns league name, rank, and members
def getLeagueDetails(leagueId):
    print("Attempting to fetch data for league: " + str(leagueId))
    leagueUrl = "https://fantasy.premierleague.com/api/leagues-classic/%s/standings" % leagueId
    return formatLeagueData(fetchRequest(leagueUrl))

# Takes in the array of players and returns their names
def getPlayerNameArray(playerArray):
    arrayToReturn = []
    for player in playerArray:
        arrayToReturn.append(player.get("player_name"))
    return arrayToReturn
