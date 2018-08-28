'''

November 2017

This script computes International Space Station (ISS) passes for a given location on Earth.  It generates a years worth of passes,
which is inaccurate because of station maneuvering and orbital drag effects.  However, the goal is to produce a data set
for creating a visualization.


'''


#Packages
import math
from datetime import datetime
import ephem


#Set file path for exporting ISS pass data to file
new_path = '/users/pnaranjo/pycharmprojects/untitled/iss-seattle-passes.csv'
new_file = open(new_path,'w')


#Define TLE orbital elements for ISS
iss = ephem.readtle("ISS (ZARYA)",
  "1 25544U 98067A   17313.54901810  .00016717  00000-0  10270-3 0  9011",
  "2 25544  51.6425  33.6740 0004009 104.3632 255.7966 15.54120801  4359")


#Define a home location for the observer - in this case, Seattle, WA (USA)
home = ephem.Observer()
home.lon = '-122.349'   # +E
home.lat = '47.67459'      # +N
home.elevation = 66 # meters
home.horizon = '-0:34'  #US Naval Observatory refraction correction of 34 degrees below horizon
home.date = datetime.utcnow()


#Function to format pass date/times from UTC to local and more suitable format for export
def convert_to_localdate(pass_date):
     local_date = ephem.localtime(pass_date)
     local_date_string = '{:%m/%d/%Y %H:%M:%S}'.format(local_date)
     return local_date_string

#Export - write column headers
print("{}, {}, {}, {}, {}, {}".format("Rise time (local)","Max alt time (local)","Set time (local)","Duration","Naked eye visible (T/F)","Sun alt for observer (deg)\n"))
new_file.write("{}, {}, {}, {}, {}, {}".format("Rise time (local)","Max alt time (local)","Set time (local)","Duration","Naked eye visible (T/F)","Sun alt for observer (deg)\n"))

#Iterate through spacecraft passes over observer home location
#IMPORTANT:  Set range for how many passes to calculate.  PyEphem will be unable to compute passes for date too many weeks in the future from the epoch
for i in range(5000):
    iss.compute(home)
    np = home.next_pass(iss)
    next_pass_times = np[::2]  # Grab only the rise, max, and set times from the tuple - that is, every other value by using ::2


    if None in next_pass_times:
        break

    #Calculate the pass duration
    duration = int((next_pass_times[2] - next_pass_times[0])*60*60*24) #duration in seconds - subtract set time from rise time

    #Solar position at max altitude of pass
    home.date = next_pass_times[1]  #Set home time to max altitude time of pass
    sun = ephem.Sun()
    sun.compute(home)
    sun_alt = math.degrees(sun.alt)

    #Calculate whether satellite is (naked eye) visible to an observer on the ground.  The satellite is reflectin sunlight to the observer
    visibility = False
    if iss.eclipsed is False and -28 < math.degrees(sun.alt) < -6:
        visibility = True

    #IMPORTANT:  Ensure that ISS is not in Earth's umbra (totally eclipsed).  It should be in the umbra such at the sun is between -28 and -6 degress elevation
    #Reference:  https://space.stackexchange.com/questions/4339/calculating-which-satellite-passes-are-visible

    #PyEphem seems to run into calculation problems with next_pass ocassionally and for passes occuring 6 months or further into the future.  There's a bug where set times appear before rise time, making duration negative.
    #It appears safe to skip the errant issue for this project but reliable calcuations of passes should be limited to withing a few weeks of TLE epoch.
    if duration >= 0:

        #Export - write each pass to file
        print("{}, {}, {}, {}, {}, {}".format(convert_to_localdate(next_pass_times[0]),
                                              convert_to_localdate(next_pass_times[1]),
                                              convert_to_localdate(next_pass_times[2]),
                                              duration, visibility,
                                              math.degrees(sun.alt)))

        new_file.write("{}, {}, {}, {}, {}, {}".format(convert_to_localdate(next_pass_times[0]),
                                              convert_to_localdate(next_pass_times[1]),
                                              convert_to_localdate(next_pass_times[2]),
                                              duration, visibility,
                                              math.degrees(sun.alt)))
        new_file.write("\n")

    #Set home location date to last time value in tuple, the pass set time so that we can use this to compute next pass time
    home.date = next_pass_times[-1]

#Close file connection
new_file.close()




