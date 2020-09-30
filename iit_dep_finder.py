import csv
import sys

def criteria_satisfied(opr, cr, rank):
	return rank > opr and rank < cr and cr < 1200

rank = int(sys.argv[1])
deps = []

with open("data.txt", "r") as branches:
	reader = csv.DictReader(branches, delimiter=",")
	line_count = 0
	for row in reader:
		cr = int(row["CR"])
		opr = int(row["OR"])
		if criteria_satisfied(opr, cr, rank):
			deps.append(row)



for dep in sorted(deps, key=lambda x: int(x["CR"])):
	print(dep["INSTI"] + " " + dep["DEP"] + " " + dep["OR"] + " " + dep["CR"])