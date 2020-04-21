import numpy as np
import pandas as pd


def GameSim(team1, team2, data, league_avg, league_avg_given):
    team1runs = np.random.normal(data.loc[data['teams']==team1,'avg_runs'],scale=10)-league_avg
    team1runs_given = np.random.normal(data.loc[data['teams']==team1,'avg_runs_given'],scale=10)-league_avg_given
    team2runs = np.random.normal(data.loc[data['teams']==team2,'avg_runs'],scale=10)-league_avg
    team2runs_given = np.random.normal(data.loc[data['teams']==team2,'avg_runs_given'],scale=10)-league_avg_given
    team1exp = (league_avg + team1runs + team2runs_given)*(1.01)
    team2exp = (league_avg + team2runs + team1runs_given)*(0.99)
    score = [team1exp, team2exp]
    return score


def sim(team1, team2):
    data = pd.read_csv('cricket/cricdata.csv')
    league_avg = sum(data['runs']) / sum(data['Games'])
    league_avg_given = sum(data['runs_given']) / sum(data['Games'])
    team1win = 0
    team2win = 0
    for i in range(1000):
        gm = GameSim(team1, team2, data, league_avg, league_avg_given)
        if gm[0] > gm[1]:
            team1win += 1
        elif gm[0] < gm[1]:
            team2win += 1
    team1win = round((team1win/1000)*100, 2)
    team2win = round((team2win/1000)*100, 2)
    re = [team1win, team2win]
    return re
