#!/usr/bin/env python3

from athleteClass import Athlete

# Creats a set of all atheletes in all teams
def createAthleteCollection(playerEventData, athleteNames):
    athleteDict = {}
    # loop through each player, get their atheletes, and update the dict
    for player in playerEventData:
        playerName = player.get("name")
        # go through each pick and add them to the dict
        for athlete in player.get("picks"):
            athleteId = athlete.get("element")
            isCaptain = athlete.get("is_captain")
            # check if they exist in the dict, if not add them
            if(athleteId not in athleteDict):
                athleteName = athleteNames.get(athleteId)
                ath = Athlete(athleteId, athleteName)
                athleteDict[athleteId] = ath
            # add current person as the user to the class
            currentAthlete = athleteDict.get(athleteId)
            currentAthlete.addToTeam(playerName)
            if(isCaptain):
                currentAthlete.addToTeamAsCaptain(playerName)
    return athleteDict
