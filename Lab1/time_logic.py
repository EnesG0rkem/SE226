seconds = int(input('Please type the seconds you want to convert\n'))
copy = seconds
hours = int(seconds) // 3600
seconds -= hours*3600
minutes = seconds// 60
seconds -= minutes*60
print(copy, ' seconds is ' ,hours,  ' hours,', minutes,' minutes, and', seconds,' seconds.')
