# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:06:01 2020

@author: ricar
"""

import math
import numpy as np
import time
import matplotlib.pyplot as plt

def distance(x1, x2, y1, y2, z1, z2):
    d = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)+pow(z2-z1,2))
    return d
    
class people:
    def __init__(self, row, column, height):
        self.row = row
        self.column = column
        self.height = height

np.random.seed(int(time.time()))
np.set_printoptions(precision=3)
votersList = []
candidatesList = []
distanceVoter= []

nVoter = int(input("Enter voting population: "))
nCandidates = int(input("Enter the number of candidates: "))

voteCount = np.zeros(nCandidates)

for i in range (nVoter):
    votersList.append(people(np.random.randint(-100,101),np.random.randint(-100,101),np.random.randint(-100,101)))
    distanceVoter.append(distance(votersList[i].row, 0, votersList[i].column, 0, votersList[i].height, 0))

for j in range (nCandidates):
    candidatesList.append(people(np.random.randint(-100,101),np.random.randint(-100,101),np.random.randint(-100,101)))

for k in range(nVoter):
    d = []
    for l in range(nCandidates):
        d.append(distance(votersList[k].row, candidatesList[l].row, votersList[k].column, candidatesList[l].column, votersList[l].height, candidatesList[l].height))
    for m in range(nCandidates):
        if d[m] == max(d):
            voteCount[m] += 1

for n in range(nCandidates):
    print(voteCount[n]/nVoter)
    
for o in range(nCandidates):
    print(distance(candidatesList[o].row, 0, candidatesList[o].column, 0, candidatesList[o].height, 0))
    
plt.hist(distanceVoter, bins=20)
plt.show()