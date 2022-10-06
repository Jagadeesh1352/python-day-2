month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('December','January', 'February'):
	season = 'winter'
elif month in ('March','April','May'):
	season = 'summer'
elif month in ('June','July','August'):
	season = 'spring'
else:
	season = 'fall'

if (month == 'March') and (day > 22):
	season = 'summer'
elif (month == 'June') and (day > 20):
	season = 'spring'
elif (month == 'September') and (day > 21):
	season = 'fall'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)

