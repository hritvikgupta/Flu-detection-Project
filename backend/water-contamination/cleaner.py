import os
import re

dir = 'inmaps/'
listing = os.listdir( dir )

s = listing[0]
reg = r"(.*)_(\d*).png"

features = set()
files = []


for s in listing:
  match = re.match( reg, s )
  if match:
    feat = match.group( 1 )
    year = match.group( 2 )
    if feat not in features:
      features.add( feat )
    files.append( [ s, feat, year ] )

# print( features )
for f in features:
  os.makedirs( f'maps/{f}' )
  
#move files 
for f in files:
  print( f"Renamed {f[0]} to maps/{f[1]}/{f[2]}.png" )
  try:
    os.rename( f'inmaps/{f[0]}', f'maps/{f[1]}/{f[2]}.png')
  except OSError as e:
    print( e )

