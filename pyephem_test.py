import ephem
import datetime
"""
m = ephem.Mars('2016')
print(ephem.constellation(m))


m = ephem.Mars('2016/7/20')
#print('%s %s %.10f' % (m.name, m.elong, m.size))

print('%s %s %.10f' % (m.ra, m.dec, m.size))
"""



#Function to define date range to iterate over
def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

start = datetime.date( year = 2017, month = 1, day = 1 )
end = datetime.date( year = 2017, month = 12, day = 31 )


#Generate RA and Dec for Sun over date range
for date in daterange( start, end ):
    m = ephem.Sun(date)
    print ('{} {} {}'.format(date, m.ra, m.dec))

#Export to text file




