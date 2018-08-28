"""

Scratch - learning how to format data types from PyEphem

November 2017

"""



#Packages

import math
import time
from datetime import datetime
import requests
import arrow
import ephem



#Home location - Seattle, WA (USA) - Phinney Ridge @ 63rd and Linden

home = ephem.Observer()
home.lon = '-122.349'   # +E
home.lat = '47.67459'      # +N
home.elevation = 66 # meters
home.horizon = '-0:34'  #US Naval Observatory refraction correction of 34 degrees below horizon
home.date = datetime.utcnow()
local_date = ephem.localtime(home.date)



arw = arrow.utcnow()

#print(arrow.get('home.date').format('YY'))

print(home.date)


date_string = '{:%m/%d/%Y}'.format(local_date)

date_string = '{:%m/%d/%Y %H:%M:%s}'.format(local_date)
print(date_string)

print(local_date.strftime('%m-%d-%Y'))


