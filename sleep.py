import os
import sys
import math
from random import randint

print('\n Starting sleeping routine...\n')

path = "./quran"
schedule_minutes = sys.argv[1] # 1st argument of py command
files = os.listdir(path) # get all files in audio dir
random_file = files[ randint( 0, len(files)-1 ) ] # get random file
try:
    os.system('cd ' + path + ' && "' + random_file + '"')
    print('\nQuran Started\n')
except:
    print('\nStarting Quran Faild\n')

if (schedule_minutes):
    try:
        schedule_time = math.floor( float( schedule_minutes ) *60 )
    except:
        schedule_time = 3600

try:
    os.system('Shutdown.exe -s -t ' + str(schedule_time) )
    print('Shutdown scheduled after: [' + str((int(schedule_time/60))) + ' minutes] \n')
except:
    print('Shutdown schedule faild')