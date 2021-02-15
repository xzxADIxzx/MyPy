import random

def isCornerTaken(field):
	return field[0] == 1 or field[2] == 1 or field[6] == 1 or field[8] == 1

def appraiser(field):
	AIValues = [100, 20, 3, 2, 1]
	cost = 0

	# AI Win
	if((field[0] == 2 and field[3] == 2 and field[6] == 2) or
	   (field[1] == 2 and field[4] == 2 and field[7] == 2) or
	   (field[2] == 2 and field[5] == 2 and field[8] == 2) or
	   (field[0] == 2 and field[1] == 2 and field[2] == 2) or
	   (field[3] == 2 and field[4] == 2 and field[5] == 2) or
	   (field[6] == 2 and field[7] == 2 and field[8] == 2) or
	   (field[0] == 2 and field[4] == 2 and field[8] == 2) or
	   (field[2] == 2 and field[4] == 2 and field[6] == 2)):
		cost += 1 * AIValues[0]

	# Player Win
	if field[0] == 2 and field[3] == 1 and field[6] == 1:
		cost += 1 * AIValues[1]
	if field[0] == 1 and field[3] == 2 and field[6] == 1:
		cost += 1 * AIValues[1]
	if field[0] == 1 and field[3] == 1 and field[6] == 2:
		cost += 1 * AIValues[1]
	if field[1] == 2 and field[4] == 1 and field[7] == 1:
		cost += 1 * AIValues[1]
	if field[1] == 1 and field[4] == 2 and field[7] == 1:
		cost += 1 * AIValues[1]
	if field[1] == 1 and field[4] == 1 and field[7] == 2:
		cost += 1 * AIValues[1]
	if field[2] == 2 and field[5] == 1 and field[8] == 1:
		cost += 1 * AIValues[1]
	if field[2] == 1 and field[5] == 2 and field[8] == 1:
		cost += 1 * AIValues[1]
	if field[2] == 1 and field[5] == 1 and field[8] == 2:
		cost += 1 * AIValues[1]
	if field[0] == 2 and field[1] == 1 and field[2] == 1:
		cost += 1 * AIValues[1]
	if field[0] == 1 and field[1] == 2 and field[2] == 1:
		cost += 1 * AIValues[1]
	if field[0] == 1 and field[1] == 1 and field[2] == 2:
		cost += 1 * AIValues[1]
	if field[3] == 2 and field[4] == 1 and field[5] == 1:
		cost += 1 * AIValues[1]
	if field[3] == 1 and field[4] == 2 and field[5] == 1:
		cost += 1 * AIValues[1]
	if field[3] == 1 and field[4] == 1 and field[5] == 2:
		cost += 1 * AIValues[1]
	if field[6] == 2 and field[7] == 1 and field[8] == 1:
		cost += 1 * AIValues[1]
	if field[6] == 1 and field[7] == 2 and field[8] == 1:
		cost += 1 * AIValues[1]
	if field[6] == 1 and field[7] == 1 and field[8] == 2:
		cost += 1 * AIValues[1]
	if field[0] == 2 and field[4] == 1 and field[8] == 1:
		cost += 1 * AIValues[1]
	if field[0] == 1 and field[4] == 2 and field[8] == 1:
		cost += 1 * AIValues[1]
	if field[0] == 1 and field[4] == 1 and field[8] == 2:
		cost += 1 * AIValues[1]
	if field[2] == 2 and field[4] == 1 and field[6] == 1:
		cost += 1 * AIValues[1]
	if field[2] == 1 and field[4] == 2 and field[6] == 1:
		cost += 1 * AIValues[1]
	if field[2] == 1 and field[4] == 1 and field[6] == 2:
		cost += 1 * AIValues[1]

	# Take center
	if field[4] == 2 and not isCornerTaken(field):
		cost += 1 * AIValues[2]

	# GG
	if field[4] == 2 and field[0] == 2 and not isCornerTaken(field):
		cost += 1 * AIValues[2]
	if field[4] == 2 and field[2] == 2 and not isCornerTaken(field):
		cost += 1 * AIValues[2]
	if field[4] == 2 and field[6] == 2 and not isCornerTaken(field):
		cost += 1 * AIValues[2]
	if field[4] == 2 and field[8] == 2 and not isCornerTaken(field):
		cost += 1 * AIValues[2]

	# EASY
	if field[4] == 2 and field[0] == 2 and (field[2] or field[6]):
		cost += 1 * AIValues[2]
	if field[4] == 2 and field[2] == 2 and (field[0] or field[8]):
		cost += 1 * AIValues[2]
	if field[4] == 2 and field[6] == 2 and (field[0] or field[8]):
		cost += 1 * AIValues[2]
	if field[4] == 2 and field[8] == 2 and (field[2] or field[6]):
		cost += 1 * AIValues[2]

	#If center taken
	if field[4] == 1 and field[0] == 2:
		cost += 1 * AIValues[3]
	if field[4] == 1 and field[2] == 2:
		cost += 1 * AIValues[3]
	if field[4] == 1 and field[6] == 2:
		cost += 1 * AIValues[3]
	if field[4] == 1 and field[8] == 2:
		cost += 1 * AIValues[3]

	# |1|X|O|
	# |4|5|X|
	# |7|8|9|
	if field[1] == 1 and field[5] == 1 and field[2] == 2:
		cost += 1 * AIValues[3]
	if field[5] == 1 and field[7] == 1 and field[8] == 2:
		cost += 1 * AIValues[3]
	if field[7] == 1 and field[3] == 1 and field[6] == 2:
		cost += 1 * AIValues[3]
	if field[3] == 1 and field[1] == 1 and field[0] == 2:
		cost += 1 * AIValues[3]

	# |1|X|O|
	# |4|5|6|
	# |7|8|X|
	if field[1] == 1 and field[8] == 1 and field[2] == 2 and field[0] == 0:
		cost += 1 * AIValues[3]
	if field[1] == 1 and field[6] == 1 and field[0] == 2 and field[2] == 0:
		cost += 1 * AIValues[3]
	if field[5] == 1 and field[6] == 1 and field[8] == 2 and field[2] == 0:
		cost += 1 * AIValues[3]
	if field[5] == 1 and field[0] == 1 and field[2] == 2 and field[8] == 0:
		cost += 1 * AIValues[3]
	if field[7] == 1 and field[0] == 1 and field[6] == 2 and field[8] == 0:
		cost += 1 * AIValues[3]
	if field[7] == 1 and field[2] == 1 and field[8] == 2 and field[6] == 0:
		cost += 1 * AIValues[3]
	if field[3] == 1 and field[2] == 1 and field[0] == 2 and field[6] == 0:
		cost += 1 * AIValues[3]
	if field[3] == 1 and field[8] == 1 and field[6] == 2 and field[0] == 0:
		cost += 1 * AIValues[3]

	# |X|2|3|
	# |4|5|6|
	# |7|8|O|
	if field[0] == 1 and field[8] == 2:
		cost += 1 * AIValues[3]
	if field[8] == 1 and field[0] == 2:
		cost += 1 * AIValues[3]
	if field[2] == 1 and field[6] == 2:
		cost += 1 * AIValues[3]
	if field[6] == 1 and field[2] == 2:
		cost += 1 * AIValues[3]

	# Build lines
	if field[0] == 0 and field[3] == 2 and field[6] == 2:
		cost += 1 * AIValues[4]
	if field[0] == 2 and field[3] == 0 and field[6] == 2:
		cost += 1 * AIValues[4]
	if field[0] == 2 and field[3] == 2 and field[6] == 0:
		cost += 1 * AIValues[4]
	if field[1] == 0 and field[4] == 2 and field[7] == 2:
		cost += 1 * AIValues[4]
	if field[1] == 2 and field[4] == 0 and field[7] == 2:
		cost += 1 * AIValues[4]
	if field[1] == 2 and field[4] == 2 and field[7] == 0:
		cost += 1 * AIValues[4]
	if field[2] == 0 and field[5] == 2 and field[8] == 2:
		cost += 1 * AIValues[4]
	if field[2] == 2 and field[5] == 0 and field[8] == 2:
		cost += 1 * AIValues[4]
	if field[2] == 2 and field[5] == 2 and field[8] == 0:
		cost += 1 * AIValues[4]
	if field[0] == 0 and field[1] == 2 and field[2] == 2:
		cost += 1 * AIValues[4]
	if field[0] == 2 and field[1] == 0 and field[2] == 2:
		cost += 1 * AIValues[4]
	if field[0] == 2 and field[1] == 2 and field[2] == 0:
		cost += 1 * AIValues[4]
	if field[3] == 0 and field[4] == 2 and field[5] == 2:
		cost += 1 * AIValues[4]
	if field[3] == 2 and field[4] == 0 and field[5] == 2:
		cost += 1 * AIValues[4]
	if field[3] == 2 and field[4] == 2 and field[5] == 0:
		cost += 1 * AIValues[4]
	if field[6] == 0 and field[7] == 2 and field[8] == 2:
		cost += 1 * AIValues[4]
	if field[6] == 2 and field[7] == 0 and field[8] == 2:
		cost += 1 * AIValues[4]
	if field[6] == 2 and field[7] == 2 and field[8] == 0:
		cost += 1 * AIValues[4]
	if field[0] == 0 and field[4] == 2 and field[8] == 2:
		cost += 1 * AIValues[4]
	if field[0] == 2 and field[4] == 0 and field[8] == 2:
		cost += 1 * AIValues[4]
	if field[0] == 2 and field[4] == 2 and field[8] == 0:
		cost += 1 * AIValues[4]
	if field[2] == 0 and field[4] == 2 and field[6] == 2:
		cost += 1 * AIValues[4]
	if field[2] == 2 and field[4] == 0 and field[6] == 2:
		cost += 1 * AIValues[4]
	if field[2] == 2 and field[4] == 2 and field[6] == 0:
		cost += 1 * AIValues[4]
	return cost

def AITurn(field):
	y = 0
	fieldEmpty = []
	for x in field:
		if x == 0:
			fieldEmpty += [y]
		y += 1

	y = 0
	costs = []
	fieldCalculate = []
	for x in fieldEmpty:
		fieldCalculate = field[:]
		fieldCalculate[x] = 2
		costs += [[appraiser(fieldCalculate), y]]
		y += 1

	costs.sort(key = lambda x: x[0], reverse = True)
	y = 0
	sortedCosts = []
	for x in costs:
		if costs[y][0] == costs[0][0]:
			sortedCosts += [costs[y]]
		y += 1

	return fieldEmpty[sortedCosts[random.randint(0, len(sortedCosts) - 1)][1]]