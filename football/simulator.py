import numpy as np
import pandas as pd


def GameSim(team1, team2,data, leagueHGS, leagueHGC, leagueAGS, leagueAGC):
    team1ATT = np.random.normal(data.loc[data['Team']==team1,'AvgHGS'])-leagueHGS
    team1DEF = np.random.normal(data.loc[data['Team']==team1,'AvgHGC'])-leagueHGC
    team2ATT = np.random.normal(data.loc[data['Team']==team2,'AvgAGS'])-leagueAGS
    team2DEF = np.random.normal(data.loc[data['Team']==team2,'AvgAGC'])-leagueAGC
    team1exp = leagueHGS + team1ATT + team2DEF
    team2exp = leagueAGS + team2ATT + team1DEF
    team1exp = round(team1exp[0])
    team2exp = round(team2exp[0])
    score = [team1exp, team2exp]
    return score


def sim(team1, team2):
    data = pd.read_csv('football/footballdata.csv')
    leagueHGS = sum(data['HGS']) / sum(data['HG'])
    leagueHGC = sum(data['HGC']) / sum(data['HG'])
    leagueAGS = sum(data['AGS']) / sum(data['AG'])
    leagueAGC = sum(data['AGC']) / sum(data['AG'])
    team1win = 0
    team2win = 0
    draw = 0
    for i in range(10000):
        gm = GameSim(team1, team2,data, leagueHGS, leagueHGC, leagueAGS, leagueAGC)
        if gm[0] > gm[1]:
            team1win += 1
        elif gm[0] < gm[1]:
            team2win += 1
        else:
            draw += 1
    team1win = (team1win / 10000) * 100
    team2win = (team2win / 10000) * 100
    draw = (draw/10000) * 100
    re = [team1win, team2win, draw]
    return re
