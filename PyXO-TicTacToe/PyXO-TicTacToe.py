import AI
import time

def isWin(field, playerAmount):
	x = 1
	if((field[0] == x and field[3] == x and field[6] == x) or
	   (field[1] == x and field[4] == x and field[7] == x) or
	   (field[2] == x and field[5] == x and field[8] == x) or
	   (field[0] == x and field[1] == x and field[2] == x) or
	   (field[3] == x and field[4] == x and field[5] == x) or
	   (field[6] == x and field[7] == x and field[8] == x) or
	   (field[0] == x and field[4] == x and field[8] == x) or
	   (field[2] == x and field[4] == x and field[6] == x)):
		if playerAmount == 1:
			print("Ты победил!")
		else:
			print("Крестик победил!")
		print()
		return True

	x = 2
	if((field[0] == x and field[3] == x and field[6] == x) or
	   (field[1] == x and field[4] == x and field[7] == x) or
	   (field[2] == x and field[5] == x and field[8] == x) or
	   (field[0] == x and field[1] == x and field[2] == x) or
	   (field[3] == x and field[4] == x and field[5] == x) or
	   (field[6] == x and field[7] == x and field[8] == x) or
	   (field[0] == x and field[4] == x and field[8] == x) or
	   (field[2] == x and field[4] == x and field[6] == x)):
		if playerAmount == 1:
			print("Ты проиграл!")
		else:
			print("Нолик победил!")
		print()
		return True

	y = True
	for x in field:
		if x == 0:
			y = False
	if y:
		print("Ничья!")
		print()
		return True

def printField(field):
	for x in range(0, 3):
		line = "|"
		for y in range(0, 3):
			if field[y + x * 3] == 0:
				if fieldType == "Y":
					line += str(y + 1 + x * 3) + "|"
				else:
					line += " |"
			else:
				if field[y + x * 3] == 1:
					line += "X|"
				else:
					line += "O|"
		print(line)

print("PyXO - Tic Tac Toe")
print("By xzxADIxzx")
print("V1.4 Release")
print()

time.sleep(1)

print("Во время своего хода введите цифру клетки")
print("|1|2|3|")
print("|4|5|6|")
print("|7|8|9|")
print()

time.sleep(1)

print("Y/N")
while True:
	fieldType = input("На поле отображать цифры? ")
	if fieldType != "Y" and fieldType != "N":
		print("Введите Y или N...")
	else:
		break

time.sleep(0.5)

while True:
	try:
		playerAmount = int(input("Кол-во игроков: "))
		if playerAmount > -1 and playerAmount < 3:
			break
		else:
			print("Введите число от 0 до 2")
	except ValueError:
		print("Введите целое число...")
print()

time.sleep(1)

while True:
	playerTurn = 0
	field = [0 for x in range(9)]

	if playerAmount == 0:
		crossTurn = True
		while True:
			time.sleep(1)
			AITurn = AI.AITurn(field)
			if crossTurn:
				field[AITurn] = 1
				print("Ход крестика: " + str(AITurn + 1))
			else:
				field[AITurn] = 2
				print("Ход нолика: " + str(AITurn + 1))
			crossTurn = not crossTurn
			printField(field)
			print()
		
			if isWin(field, playerAmount):
				break

	if playerAmount == 1:
		while True:
			while True:
				try:
					playerTurn = int(input("Ваш ход: "))
					if playerTurn > 0 and playerTurn < 10:
						if field[playerTurn - 1] < 1:
							field[playerTurn - 1] = 1
							break
						else:
							print("Клетка занята...")
					else:
						print("Введите число от 1 до 9")
				except ValueError:
					print("Введите целое число...")
		
			printField(field)
			print()
		
			if isWin(field, playerAmount):
				break
		
			AITurn = AI.AITurn(field)
			field[AITurn] = 2
			print("Ход ИИ: " + str(AITurn + 1))
			printField(field)
			print()
		
			if isWin(field, playerAmount):
				break

	if playerAmount == 2:
		crossTurn = True
		while True:
			while True:
				try:
					if crossTurn:
						playerTurn = int(input("Ход крестика: "))
					else:
						playerTurn = int(input("Ход нолика: "))
					if playerTurn > 0 and playerTurn < 10:
						if field[playerTurn - 1] < 1:
							if crossTurn:
								field[playerTurn - 1] = 1
							else:
								field[playerTurn - 1] = 2
							crossTurn = not crossTurn
							break
						else:
							print("Клетка занята...")
					else:
						print("Введите число от 1 до 9")
				except ValueError:
					print("Введите целое число...")
		
			printField(field)
			print()
		
			if isWin(field, playerAmount):
				break

	print("Y/N")
	while True:
		tryAgain = input("Попробуешь ещё? ")
		if tryAgain != "Y" and tryAgain != "N":
			print("Введите Y или N...")
		else:
			break

	if tryAgain == "Y":
		print()
	else:
		print()
		break

print("Программа завершена!")
input()