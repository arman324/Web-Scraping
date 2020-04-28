#
#  webScraping.py
#  Created by Arman Riasi on 3/1/20.
#  Copyright © 2020 Arman Riasi. All rights reserved.
#
import requests
from bs4 import BeautifulSoup
import re
from time import gmtime, strftime
import time
from time import sleep
import os

exactTime = 0
def exactTimeFunc(exactTime):
    exactTime = time.strftime("%I:%M", time.gmtime())
    amOrPm = time.strftime("%p", time.gmtime())
    if amOrPm == 'PM':
        tmp = int(exactTime[:2]) + 12
        tmp = str(tmp)
        exactTime = exactTime.replace(exactTime[:2],tmp)
        exactTime += ' GMT'
    print('\n\n\n\n\n\n\t\t\t\ttime => %s '%exactTime)
    print('\n')
    return exactTime

result = requests.get('https://www.goal.com/en/live-scores')

soup = BeautifulSoup(result.text,'html.parser')

leagueName = soup.find_all('span',attrs={'class':'competition-name'})
matchTeamList = soup.find_all('span',attrs={'class':'match-row__team-name'})
matchTime = soup.find_all('span',attrs={'class':'match-row__state'})
matchDate = soup.find_all('span',attrs={'class':'match-row__date'})
everyMatch = soup.find_all('div',attrs={'class':'match-row__data'})

matchGoal = []
leagueTitle = []
firstTeam = []
secondTeam = []
date_= []
time_ = []
GMTtime = []

def matchsFunc():
    for matchs in everyMatch:
        matchGoal.append(re.findall(r'^.*(\d+   -   \d+).*',matchs.text))

count = 0;
def teamsFunc(count):
    for teams in matchTeamList:
        if count%2 == 0:
            firstTeam.append(teams.text)
        else:
            secondTeam.append(teams.text)
        count+=1
    return count

def dateFunc():
    for date in matchDate:
        date_.append(date.text)

def GMTtimeFunc():
    for i in range(0,len(date_)):
        temp = date_[i]
        temp = temp[12:21]
        GMTtime.append(temp)

def timeFunc():
    for time in matchTime:
        time_.append(time.text)


def findMatchTimeFunc(time_,hour,minute,cnt,totalMatch):
    for cnt in range (0,totalMatch):
        hourMatch = GMTtime[cnt][:2]
        minuteMatch = GMTtime[cnt][3:5]
        if hour < hourMatch:
            time_ = time_[:cnt]+[GMTtime[cnt]]+time_[cnt:]
        if hour == hourMatch:
            if minute < minuteMatch:
                time_ = time_[:cnt]+[GMTtime[cnt]]+time_[cnt:]

    return time_

def leagueFunc():
    for league in leagueName:
         leagueTitle.append(league.text)

######print("Which league do you want? ")
matchGoal_ = []
def goalFunc():
    for goal in matchGoal:
        goal = str(goal)
        matchGoal_.append(goal[2:11])

def changeDateFunc():
    for changeDate in range(0,len(date_)):
        tmp = date_[changeDate]
        date_[changeDate] = tmp[:10]


#while True:
exactTime = exactTimeFunc(exactTime)
cnt = 0
totalMatch = len(everyMatch)
hour = exactTime[:2]
minute = exactTime[3:5]
matchsFunc()
count = teamsFunc(count)
dateFunc()
GMTtimeFunc()
timeFunc()
time_ = findMatchTimeFunc(time_,hour,minute,cnt,totalMatch)
leagueFunc()
goalFunc()
changeDateFunc()

for j in range(0,totalMatch):
    if firstTeam[j] == 'Tottenham Hotspur' or firstTeam[j] == 'Internazionale' or firstTeam[j] == 'Real Madrid' or firstTeam[j] == 'Barcelona' or firstTeam[j] == 'Liverpool' or firstTeam[j] == 'PSG' or firstTeam[j] == 'Arsenal' or firstTeam[j] == 'Manchester City' or firstTeam[j] == 'Chelsea' or firstTeam[j] == 'Manchester United' or firstTeam[j] == 'Bayern München' or firstTeam[j] == 'Juventus':
        print('%s%s%s%s\t\t%s*(important)*'%(date_[j].ljust(15,' '),time_[j].ljust(10,' '),firstTeam[j].ljust(27,' '),
        matchGoal_[j],secondTeam[j].ljust(25,' ')))
        continue
    if secondTeam[j] == 'Tottenham Hotspur' or secondTeam[j] == 'Internazionale' or secondTeam[j] == 'Real Madrid' or secondTeam[j] == 'Barcelona' or secondTeam[j] == 'Liverpool' or secondTeam[j] == 'PSG' or secondTeam[j] == 'Arsenal' or secondTeam[j] == 'Manchester City' or secondTeam[j] == 'Chelsea' or secondTeam[j] == 'Manchester United' or secondTeam[j] == 'Bayern München' or secondTeam[j] == 'Juventus':
        print('%s%s%s%s\t\t%s*(important)*'%(date_[j].ljust(15,' '),time_[j].ljust(10,' '),firstTeam[j].ljust(27,' '),
        matchGoal_[j],secondTeam[j].ljust(25,' ')))
        continue
    else:
        print('%s%s%s%s\t\t%s'%(date_[j].ljust(15,' '),time_[j].ljust(10,' '),firstTeam[j].ljust(27,' '),
        matchGoal_[j],secondTeam[j]))
        continue

print('\n\n\n\n\n\n\n\n')
    #time.sleep(60)
    #os.system('clear')  # For Linux/OS X
