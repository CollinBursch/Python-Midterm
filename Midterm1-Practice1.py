"""
Steps to creating a new virtual environment:

Create a virtual environment: 
py -3 -m venv .venv (.venv is the name of the virtual environment and can be changed

Set yes when asked to use this as a workplace env

Activate the virtual environment: 
.\.venv\Scripts\activate

Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope Process

Create New file
.gitignore

In git ignore type .venv/ (save)

Install library: 
pip install matplotlib   


"""

import csv

'''
Make a class called NBAPlayer
- This class should have three attributes: First Name, Last Name, and points
- This class should have one method for calculating the players score tier, using this table below
( Tier1: 25,000-30,000 | Tier2: 30,000-35,000 | Tier3: 35,000-40,000 | Failure: other )
'''


class NBAPlayer: # created the NBA player class

    def __init__(self, F_Name, L_Name, Points): # initialized the attributes 
        self.__F_Name = F_Name
        self.__L_Name = L_Name
        self.__Points = Points

    def get_F_Name(self):
        return self.__F_Name

    def get_L_Name(self):
        return self.__L_Name
    
    def get_Points(self):
        return self.__Points

    def score_tier(self): 
        if self.__Points >= 25000 and self.__Points < 29999:
            return 'Tier1'
        elif self.__Points >= 30000 and self.__Points < 34999:
            return 'Tier2'
        elif self.__Points >= 35000 and self.__Points < 39999:
            return 'Tier3'
        else: 
            return 'Failure'

x = NBAPlayer('Collin', 'Bursch', 35678)



''' 
Parse the top 10 NBA players file using csv reader
- Make a dictionary holding objects of the nba players 
(use the player full names as keys)
- Make another dictionary holding the different
 tiers of scoring,  (use the player full names as keys)
( Tier1: 25,000-30,000 Tier2: 30,000-35,000 | Tier3: 35,000-40,000 | Failures: other)
'''

infile = open('Top Basketball Players.txt', 'r')
csv_reader = csv.reader(infile)

nba_players = {}
score = {'Tier1': [], 'Tier2': [], 'Tier3': [], 'Failures': []}


for line in csv_reader:
    nba_players[line[0]] = NBAPlayer(line[0].split()[0], line[0].split()[1], int(line[1]))
    score[ nba_players.get(line[0]).score_tier() ].append(line[0].split()[0])

print(score)

    






'''
Parse the top 10 NBA players file using plain input file reader
- Make a dictionary holding objects of the nba players (use the player full names as keys)
- Make another dictionary holding the different tiers of scoring,  (use the player full names as keys)
( Tier1: 25,000-30,000 Tier2: 30,000-35,000 | Tier3: 35,000-40,000 | Failures: other)
'''

def main():
    players_infile = open('Top Basketball Players.txt', 'r')





