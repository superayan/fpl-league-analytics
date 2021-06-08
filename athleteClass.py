#!/usr/bin/env python3

# This is the athelte class
# The class contains data about who has the athelete, how many people have captained him

class Athlete:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.partOfTeams = []
        self.captaineByTeams = []

    #overloading operators
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    # methods to add data
    def addToTeam(self, teamOwner):
        self.partOfTeams.append(teamOwner)

    def addToTeamAsCaptain(self, teamOwner):
        self.captaineByTeams.append(teamOwner)

    def getTeamsIAmAPartOf(self):
        toReturn = ""
        for team in self.partOfTeams:
            toReturn += team
            toReturn += ", "
        return toReturn

    def getTeamsIAmACaptainOf(self):
        toReturn = ""
        for team in self.captaineByTeams:
            toReturn += team
            toReturn += ", "
        return toReturn
