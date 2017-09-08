import math
import time
from datetime import datetime
import ephem

degrees_per_radian = 180.0 / math.pi

home = ephem.Observer()
#Seattle, WA (USA) - Phinney Ridge @ 63rd and Linden
home.lon = '-122.349'   # +E
home.lat = '47.67459'      # +N
home.elevation = 66 # meters

# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
    '1 25544U 98067A   17200.50869150  .00016717  00000-0  10270-3 0  9001',
    '2 25544  51.6400 237.2171 0006024  49.2680 310.8995 15.54194842 26772'
)

while True:
    home.date = datetime.utcnow()
    #home.date = '2017/7/21 01:14:40'
    print(home.date)
    iss.compute(home)
    #print('\n iss: altitude %4.1f deg, azimuth %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
    print('\n',iss.alt,iss.az, iss.eclipsed, iss.elevation/1000)
    print(home.date)
    time.sleep(1.0)
