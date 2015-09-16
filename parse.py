import csv
import math
import itertools

def nameTeams(data,i):
  for row in data:
    if (row[i] == "ANA"):
      row[i] = "ANAHEIM"
    elif (row[i] == "ARI"):
      row[i] = "ARIZONA"
    elif (row[i] == "BOS"):
      row[i] = "BOSTON"
    elif (row[i] == "BUF"):
      row[i] = "BUFFALO"
    elif (row[i] == "CGY"):
      row[i] = "CALGARY"
    elif (row[i] == "CAR"):
      row[i] = "CAROLINA"
    elif (row[i] == "CHI"):
      row[i] = "CHICAGO"
    elif (row[i] == "COL"):
      row[i] = "COLORADO"
    elif (row[i] == "CBJ"):
      row[i] = "COLUMBUS"
    elif (row[i] == "DAL"):
      row[i] = "DALLAS"
    elif (row[i] == "DET"):
      row[i] = "DETROIT"
    elif (row[i] == "EDM"):
      row[i] = "EDMONTON"
    elif (row[i] == "FLA"):
      row[i] = "FLORIDA"
    elif (row[i] == "LAK"):
      row[i] = "LOS ANGELES"
    elif (row[i] == "MIN"):
      row[i] = "MINNESOTA"
    elif (row[i] == "MTL"):
      row[i] = "MONTREAL"
    elif (row[i] == "NSH"):
      row[i] = "NASHVILLE"
    elif (row[i] == "NJD"):
      row[i] = "NEW JERSEY"
    elif (row[i] == "NYI"):
      row[i] = "NY ISLANDERS"
    elif (row[i] == "NYR"):
      row[i] = "NY RANGERS"
    elif (row[i] == "OTT"):
      row[i] = "OTTAWA"
    elif (row[i] == "PHI"):
      row[i] = "PHILADELPHIA"
    elif (row[i] == "PIT"):
      row[i] = "PITTSBURGH"
    elif (row[i] == "SJS"):
      row[i] = "SAN JOSE"
    elif (row[i] == "STL"):
      row[i] = "ST LOUIS"
    elif (row[i] == "TBL"):
      row[i] = "TAMPA BAY"
    elif (row[i] == "TOR"):
      row[i] = "TORONTO"
    elif (row[i] == "VAN"):
      row[i] = "VANCOUVER"
    elif (row[i] == "WSH"):
      row[i] = "WASHINGTON"
    elif (row[i] == "WPG"):
      row[i] = "WINNIPEG"  
  return data

def addPrices(data, data4):
  for row in data:
    for player in data4:
      name = player[2].split()
      if (len(row) == 21):  
        name2 = row[16].split()
        if (name[0] in name2[0] and name[1] in name2[1] or name2[0] in name[0] and name2[1] in name[1]):
          row.append(player[4])
          row[6] = player[5]
      else:
        name2 = row[11].split()
        if (name[0] in name2[0] and name[1] in name2[1] or name2[0] in name[0] and name2[1] in name[1]):
          row.append(player[4])
          row[13] = float(player[0])
    if (len(row) != 22 and len(row) != 19):
      row.append("not in Fanduel!")
  return data
  
def calcFantasyGoalies(data2):
  for row in data2:
        score = 0
        score = int(row[8]) * 3
        score = score + int(row[2]) * -1
        score = score + int(row[6]) * .2
        score = score + int(row[14]) * 2
        row[13] = score
  return data2
  
def calcFantasyPlayers(data):
  for row in data:
        score = 0
        score = int(row[2]) * 3
        score = score + int(row[10]) * 2
        score = score + int(row[19])
        score = score + int(row[15]) * .25
        score = score + int(row[17]) * .5
        score = score + int(row[8]) * .4
        score = score / int(row[3])
        row[18] = score
  return data
  
def calcFantasyTeams(data, data2, data3):
  data.sort(key=lambda x: x[5])
  data2.sort(key=lambda x: x[9])
  data3.sort(key=lambda x: x[9])
  team = data[0][5]
  i = 0
  j = 0
  for row in data3:
    switch = False
    total = 0
    while (switch == False):
      if (data[i][5] != team or i+1 == len(data)):
        switch = True
      else:
        total = total + data[i][18]
        i = i+1
    while (switch == True):
      if (data2[j][9] != team or j+1 == len(data2)):
        row[21] = total
        team = data2[j][9]
        switch = False
      else:
        total = total + data2[j][13]
        j = j+1
  return data3
  
def calcFantasyAllowedTeams(data3):
  for row in data3:
    row.append(float(0))
  data3.sort(key=lambda x: x[9])
  for team in data3:
    team[25] = float(team[6]*3)
    team[25] = float(team[25]+((float(team[18])*3)/float(team[3])))
    team[25] = float(team[25]+(float(team[23])*.4))
  return data3
  
def notPlaying(teams, data3):
  today = []
  for team in data3:
    playing = False
    for match in teams:
      if (team[9] == match[0]):
        playing = True
    if (playing == False):
      today.append(False)
    else:
      today.append(True)
  index = 0
  for team in today:
    if (team == False):
      del data3[index]
    else:
      index = index + 1
  return data3

def fantasyRank(teams, data3):      
  data3.sort(key=lambda x: x[21], reverse = True)
  rank = 1
  print("Top Ranked Teams by Fantasy Point Totals: ")
  for team in data3:
    print(team[9], team[21])
  return teams
  
def winRank(teams, data3):
  home = 2
  for team in data3:
    for match in teams:
      if (match[0] == team[9]):
        if (home % 2 == 0):
          team[8] = float(float(team[13]) / float(team[3]))
        else:
          team[8] = float(float(team[22]) / float(team[3]))
      home = home + 1
    home = 2    
    
  data3.sort(key=lambda x: x[8], reverse = True)
  rank = 1
  print("Top Ranked Teams by Win Totals: ")
  for team in data3:
    print(team[9], team[8])
    for ranking in teams:
      if (ranking[0] == team[9]):
        ranking[1] = float(rank)
        rank = rank+1
  return teams
  
def goalsRank(teams, data3):
  print("Team scoring predictions: ") 
  for team in data3:
    home = 0
    prev = "nobody"
    for ranking in teams:
      if (ranking[0] == team[9]):
        if (home % 2 == 1):
          for opponent in data3:
            if (opponent[9] == prev):
              team[12] = float((float(team[12]) + float(opponent[18]))/2)
              opponent[12] = float((float(opponent[12]) + float(team[18]))/2)
              print("H:" + opponent[9] + " = " + str(opponent[12]) + " vs. V:" + team[9] + " = " + str(team[12]))
      home = home + 1
      prev = ranking[0]
  data3.sort(key=lambda x: x[12], reverse = True)
  print(" ")
  print("Ranking by number of predicted goals: ")
  rank = 1
  for team in data3:
    print(team[9], team[12])
    for ranking in teams:
      if (ranking[0] == team[9]):
        ranking[1] = float((rank + float(ranking[1])) / 2)
        rank = rank+1
  return teams   
  
def shootingRank(teams, data3):
  print("Team shooting predictions: ")

  for team in data3:
    home = 0
    prev = "nobody"
    for ranking in teams:
      if (ranking[0] == team[9]):
        if (home % 2 == 1):
          for opponent in data3:
            if (opponent[9] == prev):
              team[20] = float((float(team[20]) + float(opponent[23]))/2)
              opponent[20] = float((float(opponent[20]) + float(team[23]))/2)
              print("H:" + opponent[9] + " = " + str(opponent[20]) + " vs. V:" + team[9] + " = " + str(team[20]))
              if (team[20] > opponent[20]):
                opponent[5] = opponent[11]
              elif (team[20] < opponent[20]) :
                team[5] = team[11]
      home = home + 1
      prev = ranking[0]
  data3.sort(key=lambda x: x[5], reverse = True)
  print(" ")
  print("Percentage of wins by shot or out-shot: ")
  for team in data3:
    print(team[9], team[5])
  
  for team in data3:
    home = 0
    prev = "nobody"
    for ranking in teams:
      if (ranking[0] == team[9]):
        if (home % 2 == 1):
          for opponent in data3:
            if (opponent[9] == prev):
              if (abs(float(team[20])-float(opponent[20])) >= 2.0):
                if (team[20] > opponent[20]):
                  team[5] = float(abs(float(team[5])*float((float(team[20])-float(opponent[20]))/2)))
                  opponent[5] = float(opponent[5])
                else:
                  opponent[5] = float(abs(float(opponent[5])*float((float(opponent[20])-float(team[20]))/2)))
                  team[5] = float(team[5])
              else:
                team[5] = float(team[5])
                opponent[5] = float(opponent[5])
      home = home + 1
      prev = ranking[0]  
  
  data3.sort(key=lambda x: x[5], reverse = True)
  print(" ")
  print("Weighted rank by shooting and percentage of wins: ")
  rank = 1
  for team in data3:
    print(team[9], team[5])
    for ranking in teams:
      if (ranking[0] == team[9]):
        ranking[1] = float((rank + float(ranking[1])*2) / 3)
        rank = rank+1
        
  return teams   
  
def matchupRank(teams, data3):
  i = 0
  matchups = []
  while (i < (len(teams)/2)):
    team = []
    adv = "nobody"
    if (teams[i*2][1] < teams[(i*2)+1][1]):
      team.append(teams[i*2][0])
      team.append(teams[(i*2)+1][0])
      adv = "Advantage: "+teams[i*2][0]
    else:
      team.append(teams[(i*2)+1][0])
      team.append(teams[i*2][0])
      adv = "Advantage: "+teams[(i*2)+1][0]
    team.append(float(abs(teams[i*2][1] - teams[(i*2)+1][1])))
    team.append(adv)
    matchups.append(team)
    i = i + 1
  return matchups
  
def findGoalie(matchups, data2, data3):
  goalies = []
  for matchup in matchups:
    for goalie in data2:
      tender = []
      if (goalie[9] == matchup[0] and goalie[4] > 8):
        tender.append(goalie)
        tender.append(matchup[1])
        goalies.append(tender)
  
  goalies.sort(key=lambda x: x[0][12], reverse=True)
  data3.sort(key=lambda x: x[12])
  rank = 1
  for team in data3:
    grank = 1
    for goalie in goalies:
      if (team[9] == goalie[1]):
        goalie[1] = float((rank + rank + grank) / 2)
        rank = rank + 1
      grank = grank + 1
  goalies.sort(key=lambda x: x[1])
  return goalies
  
def findPlayers(matchups, data, data3, type):
  players = []
  for matchup in matchups:
    for player in data:
      match = []
      if ((player[6] == type) and (player[5] == matchup[0] or player[5] == matchup[1])):
        match.append(player)
        match.append(matchup[1])
        players.append(match)
  
  players.sort(key=lambda x: x[0][18], reverse=True)
  data3.sort(key=lambda x: x[25], reverse=True)
  rank = 1
  for team in data3:
    prank = 1
    for player in players:
      if (team[9] == player[1]):
        player[1] = float((rank + prank) / 2)
        rank = rank + 1
      prank = prank + 1
  players.sort(key=lambda x: x[1])
  data3.sort(key=lambda x: x[21])
  rank = 1
  for team in data3:
    for player in players:
      if (team[9] == player[1]):
        player[1] = float((float(player[1])*2 + rank) / 3)
        rank = rank + 1
  players.sort(key=lambda x: x[1])
  data3.sort(key=lambda x: x[12], reverse=True)
  rank = 1
  for team in data3:
    for player in players:
      if (team[9] == player[1]):
        player[1] = float((float(player[1])*3 + rank + rank) / 5)
        rank = rank + 1
  players.sort(key=lambda x: x[1])
  
  return players
  
def createLineups(goalies,defensemen,centers,lwings,rwings, matchups):
  
  lineup = []
  lineup2 = []
  lineup3 = []
  lineup4 = []
  lineup5 = []
  lineup6 = []
  lineups = []
  i = 0
  while (i < 9):
    lineup.append(" ")
    lineup2.append(" ")
    lineup3.append(" ")
    lineup4.append(" ")
    lineup5.append(" ")
    lineup6.append(" ")
    i = i + 1
  
  lineup[0] = goalies[0]
  lineup4[0] = goalies[0]
  
  best = 10000
  best2 = 10000
  best3 = 10000
  best4 = 0
  best5 = 0
  best6 = 0
  i = 0
  del goalies[5:len(goalies)]
  del centers[13:len(centers)]
  del defensemen[13:len(defensemen)]
  del lwings[13:len(lwings)]
  del rwings[13:len(rwings)]
  
  for goalie in goalies:
    if (goalie[0][18] != "not in Fanduel!"):
      goalie[0][18] = goalie[0][18].replace("$","")
      goalie[0][18] = goalie[0][18].replace(",","")
      goalie[0][18] = float(goalie[0][18])
    else:
      goalie[0][18] = float(60000)
  
  for player in centers:
    if (player[0][21] != "not in Fanduel!"):
        player[0][21] = player[0][21].replace("$","")
        player[0][21] = player[0][21].replace(",","")
        player[0][21] = float(player[0][21])
    else:
      player[0][21] = float(60000)
      
  for player in lwings:
    if (player[0][21] != "not in Fanduel!"):
        player[0][21] = player[0][21].replace("$","")
        player[0][21] = player[0][21].replace(",","")
        player[0][21] = float(player[0][21])
    else:
      player[0][21] = float(60000)
  
  for player in rwings:
    if (player[0][21] != "not in Fanduel!"):
        player[0][21] = player[0][21].replace("$","")
        player[0][21] = player[0][21].replace(",","")
        player[0][21] = float(player[0][21])
    else:
      player[0][21] = float(60000)
  
  for player in defensemen:
    if (player[0][21] != "not in Fanduel!"):
        player[0][21] = player[0][21].replace("$","")
        player[0][21] = player[0][21].replace(",","")
        player[0][21] = float(player[0][21])
    else:
      player[0][21] = float(60000)
       
  percentage = 0
  gi = -1
  for goalie in goalies:
    gi = gi + 1
    percentage = gi*20
    print str(percentage) + "% complete"
    for dset in itertools.combinations(defensemen,2):
      for cset in itertools.combinations(centers,2):
        for lset in itertools.combinations(lwings,2):
          for rset in itertools.combinations(rwings,2):
            salary = float(float(goalie[0][18]) + float(dset[0][0][21]) + float(dset[1][0][21]) + float(cset[0][0][21]) + float(cset[1][0][21]) + float(lset[0][0][21]) + float(lset[1][0][21]) + float(rset[0][0][21]) + float(rset[1][0][21]))
            ptotal = float(float(goalie[0][13]) + dset[0][0][18] + dset[1][0][18] + cset[0][0][18] + cset[1][0][18] + lset[0][0][18] + lset[1][0][18] + rset[0][0][18] + rset[1][0][18])
            rtotal = float(float(goalie[1]) + dset[0][1] + dset[1][1] + cset[0][1] + cset[1][1] + lset[0][1] + lset[1][1] + rset[0][1] + rset[1][1])
            if (salary < float(55000) and salary > float(52500)):
              temp = []
              temp.append(dset[0])
              temp.append(dset[1])
              temp.append(cset[0])
              temp.append(cset[1])
              temp.append(lset[0])
              temp.append(lset[1])
              temp.append(rset[0])
              temp.append(rset[1])
              twoteams = False
              for player in itertools.combinations(temp,3):
                for matchup in matchups: 
                  if (player[0][0][5] == matchup[0] or player[0][0][5] == matchup[1]):
                    if (player[1][0][5] == matchup[0] or player[1][0][5] == matchup[1]):
                      if (player[2][0][5] == matchup[0] or player[2][0][5] == matchup[1]):
                        twoteams = True
              
              if (twoteams == False):
                if (rtotal < best):
                  best = rtotal
                  print "found rank lineup!"
                  if (goalie[0][11] != lineup[0][0][11]):
                    lineup3 = lineup[:]
                  else:
                    lineup2 = lineup[:]
                  lineup[0] = goalie
                  lineup[1] = dset[0]
                  lineup[2] = dset[1]
                  lineup[3] = cset[0]
                  lineup[4] = cset[1]
                  lineup[5] = lset[0]
                  lineup[6] = lset[1]
                  lineup[7] = rset[0]
                  lineup[8] = rset[1]
                elif (rtotal < best2):
                  best2 = rtotal
                  lineup2[0] = goalie
                  lineup2[1] = dset[0]
                  lineup2[2] = dset[1]
                  lineup2[3] = cset[0]
                  lineup2[4] = cset[1]
                  lineup2[5] = lset[0]
                  lineup2[6] = lset[1]
                  lineup2[7] = rset[0]
                  lineup2[8] = rset[1]
                elif (rtotal < best3 and goalie[0][11] != lineup[0][0][11] and goalie[0][11] != lineup2[0][0][11]):
                  best3 = rtotal
                  lineup3[0] = goalie
                  lineup3[1] = dset[0]
                  lineup3[2] = dset[1]
                  lineup3[3] = cset[0]
                  lineup3[4] = cset[1]
                  lineup3[5] = lset[0]
                  lineup3[6] = lset[1]
                  lineup3[7] = rset[0]
                  lineup3[8] = rset[1]
                elif (ptotal > best4):
                  print "found point lineup!"
                  best4 = rtotal
                  if (goalie[0][11] != lineup[0][0][11]):
                    lineup6 = lineup4[:]
                  else:
                    lineup5 = lineup4[:]
                  lineup4[0] = goalie
                  lineup4[1] = dset[0]
                  lineup4[2] = dset[1]
                  lineup4[3] = cset[0]
                  lineup4[4] = cset[1]
                  lineup4[5] = lset[0]
                  lineup4[6] = lset[1]
                  lineup4[7] = rset[0]
                  lineup4[8] = rset[1]
                elif (ptotal > best5):
                  best5 = rtotal
                  lineup5[0] = goalie
                  lineup5[1] = dset[0]
                  lineup5[2] = dset[1]
                  lineup5[3] = cset[0]
                  lineup5[4] = cset[1]
                  lineup5[5] = lset[0]
                  lineup5[6] = lset[1]
                  lineup5[7] = rset[0]
                  lineup5[8] = rset[1]
                elif (ptotal > best6 and goalie[0][11] != lineup4[0][0][11] and goalie[0][11] != lineup5[0][0][11]):
                  best5 = rtotal
                  lineup6[0] = goalie
                  lineup6[1] = dset[0]
                  lineup6[2] = dset[1]
                  lineup6[3] = cset[0]
                  lineup6[4] = cset[1]
                  lineup6[5] = lset[0]
                  lineup6[6] = lset[1]
                  lineup6[7] = rset[0]
                  lineup6[8] = rset[1]
                  
  lineups.append(lineup)
  lineups.append(lineup2)
  lineups.append(lineup3)
  lineups.append(lineup4)
  lineups.append(lineup5)
  lineups.append(lineup6)
  return lineups
  
  
def main():
  data = []
  data2 = []
  data3 = []
  data4 = []
  with open('C:\\Users\\Kevin\\Documents\\Python\\NHL\\tutorial\\players.csv', 'rb') as csvfile:
    with open('C:\\Users\\Kevin\\Documents\\Python\\NHL\\tutorial\\goalies.csv', 'rb') as csvfile2:
      with open('C:\\Users\\Kevin\\Documents\\Python\\NHL\\tutorial\\teams.csv', 'rb') as csvfile3:
        with open('C:\\Users\\Kevin\\Documents\\Python\\NHL\\tutorial\\fanduel.csv', 'rb') as csvfile4:
          parser = csv.reader(csvfile)
          parser2 = csv.reader(csvfile2)
          parser3 = csv.reader(csvfile3)
          parser4 = csv.reader(csvfile4)
          first = True
          for row in parser:
            if (first == True):
              first = False	
            else:
              data.append(row)
          first = True
          for row in parser2:
           if (first == True):
             first = False	
           else:
             data2.append(row)
          first = True
          for row in parser3:
            if (first == True or row[0] == ""):
              first = False	
            else:
              data3.append(row)
          first = True
          for row in parser4:
           if (first == True):
             first = False	
           else:
             data4.append(row)
          data = nameTeams(data,5)
          data2 = nameTeams(data2,9)
          data = calcFantasyPlayers(data)
          data2 = calcFantasyGoalies(data2)
          data3 = calcFantasyTeams(data, data2, data3)
          data3 = calcFantasyAllowedTeams(data3)
          data = addPrices(data, data4)
          data2 = addPrices(data2, data4)
  teams = []
  team = []
  print "DATA IS PREPARED"
  print "PLEASE INPUT GAMES (FORMAT: Home Team [Enter] Away Team [Enter] STOP [Enter]"
  game = raw_input()
  while (game != "STOP"):
    team = []
    team.append(game)
    team.append(float(0))
    teams.append(team)
    team = []
    team.append(raw_input())
    team.append(float(0))
    teams.append(team)
    game = raw_input()
  data3 = notPlaying(teams, data3)
  print " "
  print " "
  teams = fantasyRank(teams, data3)
  print "---------------"
  teams = winRank(teams, data3)
  print "---------------"
  teams = goalsRank(teams, data3)
  print "---------------"
  teams = shootingRank(teams,data3)
  print "---------------"
  matchups = []
  matchups = matchupRank(teams, data3)
  teams.sort(key=lambda x: x[1])
  print " "
  print "The ranking of teams for today is: "
  for team in teams:
    print team[0], team[1]
  matchups.sort(key=lambda x: x[2], reverse = True)
  print " "
  print "The best match-ups today are: "
  for matchup in matchups:
    print matchup
  goalies = []
  goalies = findGoalie(matchups, data2, data3)
  defensemen = []
  centers = []
  lwings = []
  rwings = []
  defensemen = findPlayers(matchups, data, data3, "D")
  centers = findPlayers(matchups, data, data3, "C")
  lwings = findPlayers(matchups, data, data3, "LW")
  rwings = findPlayers(matchups, data, data3, "RW")
  print " "
  print "Top 10 goalies today are: "
  i = 0
  while (i < 10 and i < len(goalies)):
    print goalies[i][0][11], goalies[i][1], goalies[i][0][9], goalies[i][0][18]
    i = i + 1
  print " "
  print "Top 15 defensemen today are: "
  i = 0
  while (i < 15 and i < len(defensemen)):
    print defensemen[i][0][16], defensemen[i][1], defensemen[i][0][5], defensemen[i][0][21]
    i = i + 1
  print " "
  print "Top 15 centers today are: "
  i = 0
  while (i < 15 and i < len(centers)):
    print centers[i][0][16], centers[i][1], centers[i][0][5], centers[i][0][21]
    i = i + 1
  print " "
  print "Top 15 left wings today are: "
  i = 0
  while (i < 15 and i < len(lwings)):
    print lwings[i][0][16], lwings[i][1], lwings[i][0][5], lwings[i][0][21]
    i = i + 1
  print " "
  print "Top 15 right wings today are: "
  i = 0
  while (i < 15 and i < len(rwings)):
    print rwings[i][0][16], rwings[i][1], rwings[i][0][5], rwings[i][0][21]
    i = i + 1
  print " "

  lineups = []
  lineups = createLineups(goalies,defensemen,centers,lwings,rwings, matchups)          
  
  totsal = []
  totpts = []
  totrnk = []
  tmpsal = 0
  tmppts = 0
  tmprnk = 0
  i = 0
  
  for lineupa in lineups:
    tmpsal = (lineupa[0][0][18] + lineupa[1][0][21] + lineupa[2][0][21] + lineupa[3][0][21] + lineupa[4][0][21] + lineupa[5][0][21] + lineupa[6][0][21] + lineupa[7][0][21] + lineupa[8][0][21])
    tmppts = (lineupa[0][0][13] + lineupa[1][0][18] + lineupa[2][0][18] + lineupa[3][0][18] + lineupa[4][0][18] + lineupa[5][0][18] + lineupa[6][0][18] + lineupa[7][0][18] + lineupa[8][0][18])
    tmprnk = (lineupa[0][1] + lineupa[1][1] + lineupa[2][1] + lineupa[3][1] + lineupa[4][1] + lineupa[5][1] + lineupa[6][1] + lineupa[7][1] + lineupa[8][1])
    totsal.append(tmpsal)
    totpts.append(tmppts)
    totrnk.append(tmprnk)
  
  for lineupa in lineups:
    for player in lineupa:
      for goalie in goalies:
        if player[0][11] == goalie[0][11]:
          player = goalie
      for dman in defensemen:
        if player[0][16] == dman[0][16]:
          player = dman
      for lwing in lwings:
        if player[0][16] == lwing[0][16]:
          player = lwing
      for rwing in rwings:
        if player[0][16] == rwing[0][16]:
          player = rwing
      for center in centers:
        if player[0][16] == center[0][16]:
          player = center
  
  lineup = lineups[0]
  lineup2 = lineups[1]
  lineup3 = lineups[2]
  lineup4 = lineups[3]
  lineup5 = lineups[4]
  lineup6 = lineups[5]
  
  print "Top rank lineup today... Salary = " + str(totsal[0]) + " Points = " + str(totpts[0]) + " Rank = " + str(totrnk[0])
  print lineup[0][0][11], lineup[0][0][9], lineup[0][1], lineup[0][0][13], lineup[0][0][18]
  for player in lineup:
    if player != lineup[0]:
      print player[0][16], player[0][5], player[1], player[0][18], player[0][21]
  print " "
  print "Next best rank lineup today is... Salary = " + str(totsal[1]) + " Points = " + str(totpts[1]) + " Rank = " + str(totrnk[1])
  print lineup2[0][0][11], lineup2[0][0][9], lineup2[0][1], lineup2[0][0][13], lineup2[0][0][18]
  for player in lineup2:
    if player != lineup2[0]:
      print player[0][16], player[0][5], player[1], player[0][18], player[0][21]
  print " "
  print "Alternate goalie rank lineup today is... Salary = " + str(totsal[2]) + " Points = " + str(totpts[2]) + " Rank = " + str(totrnk[2])
  print lineup3[0][0][11], lineup3[0][0][9], lineup3[0][1], lineup3[0][0][13], lineup3[0][0][18]
  for player in lineup3:
    if player != lineup3[0]:
      print player[0][16], player[0][5], player[1], player[0][18], player[0][21]
  print " "
  print "Top point lineup today is... Salary = " + str(totsal[3]) + " Points = " + str(totpts[3]) + " Rank = " + str(totrnk[3])
  print lineup4[0][0][11], lineup4[0][0][9], lineup4[0][1], lineup4[0][0][13], lineup4[0][0][18]
  for player in lineup4:
    if player != lineup4[0]:
      print player[0][16], player[0][5], player[1], player[0][18], player[0][21]
  print " "
  print "Next best point lineup today is... Salary = " + str(totsal[4]) + " Points = " + str(totpts[4]) + " Rank = " + str(totrnk[4])
  print lineup5[0][0][11], lineup5[0][0][9], lineup5[0][1], lineup5[0][0][13], lineup5[0][0][18]
  for player in lineup5:
    if player != lineup5[0]:
      print player[0][16], player[0][5], player[1], player[0][18], player[0][21]
  print " "
  print "Alternate goalie point lineup today is... Salary = " + str(totsal[5]) + " Points = " + str(totpts[5]) + " Rank = " + str(totrnk[5])
  print lineup6[0][0][11], lineup6[0][0][9], lineup6[0][1], lineup6[0][0][13], lineup6[0][0][18]
  for player in lineup6:
    if player != lineup6[0]:
      print player[0][16], player[0][5], player[1], player[0][18], player[0][21]
  print " "

  
if __name__ == "__main__":
  main()
      
	