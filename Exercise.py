import csv

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
