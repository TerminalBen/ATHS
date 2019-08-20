import datetime,time

import time
import datetime

print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))                   #year
print("Month of year: ", datetime.date.today().strftime("%B"))                  #Month
print("Week number of the year: ", datetime.date.today().strftime("%W"))        #week number of the current year, starting with the first Monday as the first day of the first week
print("Weekday of the week: ", datetime.date.today().strftime("%w"))            #day of the week as a decimal, Sunday=0
print("Day of year: ", datetime.date.today().strftime("%j"))                    #day of the year (001 to 366)
print("Day of the month : ", datetime.date.today().strftime("%d"))              #day of the month (01 to 31)
print("Day of week: ", datetime.date.today().strftime("%A"))                    #full weekday name
