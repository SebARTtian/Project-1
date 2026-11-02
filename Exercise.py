import csv

def totalAverage(hrs):
	total = 0
	for hr in hrs:
		total = total + hr
	total = total / len(hrs)
	return total



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
print(hrs)

print(totalAverage(hrs))
