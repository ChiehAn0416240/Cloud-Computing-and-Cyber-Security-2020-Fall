#!/usr/bin/env python
import sys

month_conversion = {
    'Jan':'01', 'Feb':'02', 'Mar':'03',
    'Apr':'04', 'May':'05', 'Jun':'06',
    'Jul':'07', 'Aug':'08', 'Sep':'09',
    'Oct':'10', 'Nov':'11', 'Dec':'12',
}
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()   
    # split the line into multiple words by "whitespace" (default)
    words = line.split()
	
    # after splitting, the information we need is stored in words[3] --> words[3] looks like "[07/Mar/2004:16:05:49"
    date = words[3][1:12].split('/')
    year = date[2]
    month = month_conversion[date[1]]
    day = date[0]
    hour = words[3][13:15]	# two-digits
	
    output = '%s-%s-%s T %s:00:00.000' % (year, month, day, hour)   
    print '%s\t%s' % (output, 1)
 
