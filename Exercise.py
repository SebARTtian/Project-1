import csv

def totalAverage(hrs):
	total = 0
	for hr in hrs:
		total = total + hr
	total = total / len(hrs)
	return total

def prop_above(hrs):
	count = 0
	for hr in hrs:
        	if hr > totalAverage(hrs):
                	count += 1
	total = count / len(hrs)
	total = total * 100
	return total


def median(ls):
	ls.sort()
	total = len(ls) % 2
	if total == 0:
		mid = len(ls) // 2
		return ls[mid]


fname =  "StudentExercise.csv"
fh =  open(fname)

hrs = []

next(fh)

for line in fh:
	exerciseHours = line.split(",")
	exercise = exerciseHours[0]
	if exercise != '':
		exercise = float(exercise)
		hrs.append(exercise)



propList = []

print(hrs)

print(totalAverage(hrs))

print(prop_above(hrs))

