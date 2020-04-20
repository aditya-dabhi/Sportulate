import numpy as np
import pandas as pd


def GameSim(team1, team2, data, oeravg, deravg, tempoavg):
    team1odiff = np.random.normal(data.loc[data['Team'] == team1, 'OER'], scale=5) - oeravg
    team1ddiff = np.random.normal(data.loc[data['Team'] == team1, 'DER'], scale=5) - deravg
    team2odiff = np.random.normal(data.loc[data['Team'] == team2, 'OER'], scale=5) - oeravg
    team2ddiff = np.random.normal(data.loc[data['Team'] == team2, 'DER'], scale=5) - deravg
    team1expeff = (oeravg + team1odiff + team2ddiff) * (1.01)
    team2expeff = (oeravg + team2odiff + team1ddiff) * (0.99)
    matchtempo = (data.loc[data['Team']==team1,'Tempo']-tempoavg).to_numpy() + (data.loc[data['Team']==team1,'Tempo']-tempoavg).to_numpy() + tempoavg
    team1score = (team1expeff / 100) * matchtempo
    team2score = (team2expeff / 100) * matchtempo
    score = [team1score, team2score]
    return score


def sim(team1, team2):
    data = pd.read_csv('basketball/bbdata.csv')
    oeravg = data.loc[:, 'OER'].mean(axis=0)
    deravg = data.loc[:, 'DER'].mean(axis=0)
    tempoavg = data.loc[:, 'Tempo'].mean(axis=0)
    team1win = 0
    team2win = 0
    matchcount = 0
    for i in range(5000):
        gm = GameSim(team1, team2, data, oeravg, deravg, tempoavg)
        if gm[0] > gm[1]:
            team1win += 1
        elif gm[0] < gm[1]:
            team2win += 1
        else:
            matchcount -= 1
        matchcount += 1
    team1win = (team1win/matchcount)*100
    team2win = (team2win/matchcount)*100
    re = [team1win, team2win]
    return re
