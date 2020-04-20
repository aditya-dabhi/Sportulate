import numpy as np
import pandas as pd


def GameSim(team1, team2, data, league_avg, league_avg_given):
    team1runs = np.random.normal(data.loc[data['teams']==team1,'avg_runs'],scale=10)-league_avg
    team1runs_given = np.random.normal(data.loc[data['teams']==team1,'avg_runs_given'],scale=10)-league_avg_given
    team2runs = np.random.normal(data.loc[data['teams']==team2,'avg_runs'],scale=10)-league_avg
    team2runs_given = np.random.normal(data.loc[data['teams']==team2,'avg_runs_given'],scale=10)-league_avg_given
    team1exp = league_avg + team1runs + team2runs_given
    team2exp = league_avg + team2runs + team1runs_given
    score = [team1exp, team2exp]
    return score


def sim(team1, team2):
    data = pd.read_csv('cricket/cricdata.csv')
    league_avg = sum(data['runs']) / sum(data['Games'])
    league_avg_given = sum(data['runs_given']) / sum(data['Games'])
    team1win = 0
    team2win = 0
    for i in range(10000):
        gm = GameSim(team1, team2, data, league_avg, league_avg_given)
        if gm[0] > gm[1]:
            team1win += 1
        elif gm[0] < gm[1]:
            team2win += 1
    team1win = (team1win/10000)*100
    team2win = (team2win/10000)*100
    re = [team1win, team2win]
    return re
