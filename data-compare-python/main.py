# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:13:34 2020

@author: sriram1204
"""

import pandas as pd

df1 = pd.read_excel('IAM.xlsx')
df2 = pd.read_excel('BCA.xlsx')


newDf = pd.merge(df1,df2,on=['Date','HomeTeam','AwayTeam'],how='inner')

sameDf = newDf[((newDf["Tottal Home goals_x"] == newDf["Tottal Home goals_y"]) &
               (newDf["Tottal Away Goals _x"] == newDf["Tottal Away Goals _y"]) &
               (newDf["Half Time Home Goals_x"] == newDf["Half Time Home Goals_y"]) &
               (newDf["Half Time Away Goals_x"] == newDf["Half Time Away Goals_y"]) &
               (newDf["HOME TRIES _x"] == newDf["HOME TRIES _y"]) &
               (newDf["DRAW TRIES _x"] == newDf["DRAW TRIES _y"]) &
               (newDf["AWAY TRIES _x"] == newDf["AWAY TRIES _y"]))]

invSameDf = newDf[~((newDf["Tottal Home goals_x"] == newDf["Tottal Home goals_y"]) &
               (newDf["Tottal Away Goals _x"] == newDf["Tottal Away Goals _y"]) &
               (newDf["Half Time Home Goals_x"] == newDf["Half Time Home Goals_y"]) &
               (newDf["Half Time Away Goals_x"] == newDf["Half Time Away Goals_y"]) &
               (newDf["HOME TRIES _x"] == newDf["HOME TRIES _y"]) &
               (newDf["DRAW TRIES _x"] == newDf["DRAW TRIES _y"]) &
               (newDf["AWAY TRIES _x"] == newDf["AWAY TRIES _y"]))]

#Finding the missing rows
df1 = df1.fillna(0)
df2 = df2.fillna(0)

DummyRows = df1[df1['Date'] == 0]
DummyRows2 = df2[df2['Date'] == 0]

invSameDf = pd.concat([invSameDf,DummyRows,DummyRows2])

sameDf.to_excel("CommonRowsBetweenFiles.xlsx",index=False)
invSameDf.to_excel("DifferentRowsBetweenFiles.xlsx",index=False)