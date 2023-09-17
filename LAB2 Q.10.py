'''A day has 86,400 secs (24*60*60). Given a number in the range 1 to 86,400, output the current
time as hours, minutes, and seconds with a 24-hour clock. For example: 70,000 sec is 19 hours,
26 minutes, and 40 seconds'''
num=int(input("Enter the time in seconds:"))
hour=num//3600
hour1=num%3600
minute=hour1//60
second=hour1%60
print(hour,"hours",minute,"minutes",second,"seconds")
