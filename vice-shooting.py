#!/usr/bin/python

import math, sys
import numpy as np
from scipy.optimize import curve_fit
import sys
import pandas as pd

#sys.stdout.flush()
allthis = pd.read_csv('Vice-shooting-stat.csv',skipinitialspace=True,usecols =[1,2,3,4,5,6,9,10,11,12,14]).fillna("NAN")
psvarray = allthis.values


#print(len(np.unique(psvarray[:,0])),len(np.unique(psvarray[:,0])))
ids, indices, counts = np.unique(psvarray[:,3], return_index=True, return_counts=True)
ids2, indices2, counts2 = np.unique(psvarray[:,5], return_index=True, return_counts=True)
ids3, indices3, counts3 = np.unique(psvarray[:,9], return_index=True, return_counts=True)
ids4, indices4, counts4 = np.unique(psvarray[:,10], return_index=True, return_counts=True)

print('The total # of subjects involved in the shootings is', np.sum(psvarray[:,0]))

#compute the number of fatal to non-fatal shootings
ids5, indices5, counts5 = np.unique(psvarray[:,1], return_index=True, return_counts=True)
len_fatality = len(ids5)
print(psvarray[:,1])
print('The ratio of fatal to non-fatal shootings is',)
for i in range(len_fatality):
	print(ids5[i], counts5[i])

#compute the number of fatal to non-fatal shootings per armed and unarmed subjects
ids6, indices6, counts6 = np.unique(psvarray[:,2], return_index=True, return_counts=True)  
print(ids6)
nf_counts_NN = 0; nf_counts_NY =0; nf_counts_FN = 0; nf_counts_FY = 0
for i in range(len(ids6)):
	aa = np.where(psvarray[:,2] == ids6[i])
	bb = (np.asarray(aa)).flatten()
	for j in range(counts6[i]):
		if psvarray[bb[j],1].strip() == 'N'and ids6[i].strip() == 'Y':
			nf_counts_NY += 1
		if psvarray[bb[j],1].strip() == 'F' and ids6[i].strip() == 'N':
			nf_counts_FN += 1
		if psvarray[bb[j],1].strip() == 'N' and ids6[i].strip() == 'N':
			nf_counts_NN += 1
		if psvarray[bb[j],1].strip() == 'F' and ids6[i].strip() == 'Y':
			nf_counts_FY += 1


print('The number of fatalities when subjects was not armed is :', nf_counts_FN)
print('The number of fatalities when subjects were armed is :', nf_counts_FY)
print('The number of non-fatalities when subjects were armed is :', nf_counts_NY) 
print('The number of non-fatalities when subjects were not armed :', nf_counts_NN)

#compute the number of fatalities by city
all_cities = len(ids4)
c_nf_counts_NN = np.zeros(all_cities); c_nf_counts_NY = np.zeros(all_cities); c_nf_counts_FN = np.zeros(all_cities); c_nf_counts_FY = np.zeros(all_cities)
for i in range(len(ids4)):
	aa = np.where(psvarray[:,10] == ids4[i])
	bb = (np.asarray(aa).flatten())
	for j in range(counts4[i]):
		if psvarray[bb[j],1].strip() == 'N'and psvarray[bb[j],2].strip() == 'Y':
			c_nf_counts_NY[i] += 1
		if psvarray[bb[j],1].strip() == 'F' and psvarray[bb[j],2].strip() == 'N':
			c_nf_counts_FN[i] += 1
		if psvarray[bb[j],1].strip() == 'N' and psvarray[bb[j],2].strip() == 'N':
			c_nf_counts_NN[i] += 1
		if psvarray[bb[j],1].strip() == 'F' and psvarray[bb[j],2].strip() == 'Y':
			c_nf_counts_FY[i] += 1

for i in range(len(ids4)):
	print('The number of fatalities when subjects was not armed in :', ids4[i], 'is', c_nf_counts_FN[i])
	print('The number of fatalities when subjects were armed in :',ids4[i], 'is', c_nf_counts_FY[i])
	print('The number of non-fatalities when subjects were armed is :',ids4[i], c_nf_counts_NY[i]) 
	print('The number of non-fatalities when subjects were not armed :', ids4[i], c_nf_counts_NN[i])

np.savetxt('fatalities_by_cities.csv', np.transpose([c_nf_counts_FN, c_nf_counts_FY, c_nf_counts_NY, c_nf_counts_NN]), delimiter=",") 
np.savetxt('list_cities.txt', np.transpose([ids4]), fmt="%s") 


#compute the number of fatalities by city
all_races = len(ids)
print(ids, indices)
r_nf_counts_NN = np.zeros(all_races); r_nf_counts_NY = np.zeros(all_races); r_nf_counts_FN = np.zeros(all_races); r_nf_counts_FY = np.zeros(all_races)
for i in range(len(ids)):
	aa = np.where(psvarray[:,3] == ids[i])
	bb = (np.asarray(aa).flatten())
	for j in range(counts[i]):
		if psvarray[bb[j],1].strip() == 'N'and psvarray[bb[j],2].strip() == 'Y':
			r_nf_counts_NY[i] += 1
		if psvarray[bb[j],1].strip() == 'F' and psvarray[bb[j],2].strip() == 'N':
			r_nf_counts_FN[i] += 1
		if psvarray[bb[j],1].strip() == 'N' and psvarray[bb[j],2].strip() == 'N':
			r_nf_counts_NN[i] += 1
		if psvarray[bb[j],1].strip() == 'F' and psvarray[bb[j],2].strip() == 'Y':
			r_nf_counts_FY[i] += 1

np.savetxt('fatalities_by_race.csv', np.transpose([r_nf_counts_FN, r_nf_counts_FY, r_nf_counts_NY, r_nf_counts_NN]), delimiter=",")
np.savetxt('list_races.txt',np.transpose([ids]),fmt="%s")

for i in range(len(ids)):
	print('The number of fatalities when subjects was not armed and the race is:', ids[i], 'is', r_nf_counts_FN[i])
	print('The number of fatalities when subjects were armed and the race is :',ids[i], 'is', r_nf_counts_FY[i])
	print('The number of non-fatalities when subjects were armed and the race is :',ids[i], r_nf_counts_NY[i]) 
	print('The number of non-fatalities when subjects were not armed and the race is:', ids[i], r_nf_counts_NN[i])
