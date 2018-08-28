'''

December 2017

This script computes the RA and Dec for the Apollo 12 3rd stage booster.  Discovered by an amateaur astronomer in 2002.
Read this:  https://en.wikipedia.org/wiki/J002E3


'''


#Packages
import math
from datetime import datetime
import ephem


#Define a home location for the observer - in this case, Seattle, WA (USA)
home = ephem.Observer()
home.lon = '-122.349'   # +E
home.lat = '47.67459'      # +N
home.elevation = 66 # meters
home.horizon = '-0:34'  #US Naval Observatory refraction correction of 34 degrees below horizon
home.date = datetime.utcnow()

# Create a body by defining orbital elements for object for an elliptical orbit
apollo = ephem.EllipticalBody()

'''
Definition of EllipticalBody elements

_inc — Inclination (°)
_Om — Longitude of ascending node (°)
_om — Argument of perihelion (°)
_a — Mean distance from sun (AU)
_M — Mean anomaly from the perihelion (°)
_epoch_M — Date for measurement _M
_size — Angular size (arcseconds at 1 AU)
_e — Eccentricity
_epoch — Epoch for _inc, _Om, and _om
_H, _G — Parameters for the H/G magnitude model
_g, _k — Parameters for the g/k magnitude model
'''

#Set attributed for EllipticalBody using last known orbital elements

'''
Elements obtained JPL HORIZONS application - https://ssd.jpl.nasa.gov/horizons.cgi#results 
Search for NEOCP J002E3.  

See page 27 of ftp://ssd.jpl.nasa.gov/pub/ssd/Horizons_doc.pdf for definitions

'''

apollo._epoch = 2452713.5
apollo._inc = .05170235166773032
apollo._Om = 154.3675607263368
apollo._e = .04355885465851009
apollo._om = 344.9535405547711
apollo._a = .9898454790953145 / (1 - apollo._e)
apollo._H = 26.432 # Absolute magnitude parameter (asteroid)
apollo._G = 0.15 # Magnitude slope parameter; can be < 0 (asteroid)



#Compute RA and Dec
apollo.compute('2017/12/31 00:15:00')


print("{}".format(apollo.earth_distance))


print("{}, {}".format(apollo.ra, apollo.dec))

#unfinished - for remaining portion of script, iterate through date to calculate RA, DEC for a given time range.









