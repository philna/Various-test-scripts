import requests
#Arrow is a Python library that offers a sensible, human-friendly approach to creating, manipulating,
# formatting and converting dates, times, and timestamps.
import arrow

#  This script connects to the OpenNotify ISS Pass Time API
#  API Documentation:  http://open-notify.org/Open-Notify-API/ISS-Pass-Times/

#Set file path for exporting ISS pass data to file
new_path = '/users/pnaranjo/pycharmprojects/untitled/iss-passes.csv'
new_file = open(new_path,'w')

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of Seattle, WA at our house in Phinney Ridge
#  It's also set to return 100 passes (n), the maximum allowed by the API

parameters = {"lat": 47.67459, "lon": -122.349, "alt": 66.0, "n": 100}

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
# print(response.status_code)



# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)


# Get the response data as a dictionary in json format.
data = response.json()


#Export to .csv file


# Iterate through duration and risetime for ISS
print('{}  {}  {}'.format("Pass Duration (minutes)", ",", "Rise time above (10° elevation)"))

#Write file column headers
new_file.write('{}  {}  {}'.format("Pass Duration (minutes)", ",", "Rise time above (10° elevation)\n"))

print(type(response.risetime))


#Iterate - response is the key - see API docs
for each in data['response']:
    myList = ['{:5.3f}'.format(each['duration']/60) , arrow.get(each['risetime']).format('YYYY-MM-DD HH:mm:ss ZZ')]
    myString = ','.join(map(str, myList))

    #print('{:5.3f}'.format(each['duration']/60), ",", arrow.get(each['risetime']))
    print(myString)

    #Write data to file
    new_file.write(myString)
    new_file.write("\n")

#Close file connection
new_file.close()









