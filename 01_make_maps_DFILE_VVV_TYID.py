#!/usr/bin/env python3
#
# 01_make_maps_DFILE_VVV_TYID

import sys
import subprocess
import pandas as pd

nargv = len(sys.argv)
if nargv == 4:
  dfile=sys.argv[1]
  var=sys.argv[2]
  tyid=sys.argv[3]
  if (var == "LHF"):
   lev="(0,400,40)"
elif nargv == 5:
  dfile=sys.argv[1]
  var=sys.argv[2]
  tyid=sys.argv[3]
  lev=sys.argv[4] 
else:
  print("input error")

print(tyid)

# get best track data
command='./Best_Track/best_track.py DATA:time,lon,lat,p,ws ' +  tyid + ' > ty1013.txt'
subprocess.getoutput(command)

# read date,clon,clat
df = pd.read_table('./ty1013.txt', header=None, sep=' ',skipinitialspace=True, skiprows=[0],names=['time','lon','lat','p','wind'])
print(df)

# define date_time as a new column (For ferret time format)
df['date_time'] = pd.to_datetime(df['time'], format='%y%m%d%H')
df['date_time_ferret'] = df['date_time'].dt.strftime("%d-%b-%Y %H:%M:%S")

# cal longitude and latitude
df['longitude'] = df['lon']/10
df['latitude'] = df['lat']/10

# print Best track data for TYID
target=['date_time_ferret','longitude','latitude']
print(df[target])

# Loop and make figures
n=0
for date in df['date_time_ferret']:
 print (n,date,df.iloc[n]['longitude'],df.iloc[n]['latitude'])
 longitude = df.iloc[n]['longitude']
 latitude = df.iloc[n]['latitude']
 task='./make_jnl.csh ' + dfile + ' ' + var + ' ' + str(n).zfill(3) + ' ' + date + ' ' + str(longitude) + ' ' + str(latitude) + ' "' + lev + '" ' + tyid
 print(task)
 res=subprocess.getoutput(task)
 print(res)
 command='ferret -nojnl -gif < ferret_go.jnl'
 res=subprocess.getoutput(command)
 print(res)
 n += 1
 

