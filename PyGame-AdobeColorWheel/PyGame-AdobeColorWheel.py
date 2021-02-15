import pyautogui as gui
import time
import pyscreeze

def MouseCloseCorner():
	mousePosX, mousePosY = gui.position()
	if mousePosX < 100 and mousePosY < 100:
		return True

gui.FAILSAFE = False

print("PyGame - Adobe Color Wheel")
print("By xzxADIxzx")
print("V1.0 Release")
print()

time.sleep(1)

print("После нажатия \"Enter\" начнёться таймер на 3сек")
print("За это время вы должны выделить окно браузера")
print("https://color.adobe.com/color-wheel-game")
print("Не двигайте и не закрывайте окно")
print("P.S. Что бы остановить бота переместите курсор")
print("В левый верхний угол")

input()
time.sleep(3)

Xs = [0 for x in range(39)]
Ys = [0 for x in range(39)]

allFine = True
for x in range(0, 39):
	if MouseCloseCorner():
		allFine = False
		break

	try:
		Xs[x], Ys[x] = gui.locateCenterOnScreen("imgs/" + str(x) + ".png")
	except:
		print("Error: Не получается определить положение игры")
		print("Error: Попробуйте открыть окно в полноэкранном режиме")
		allFine = False
		break

	if x == 10 or x == 20 or x == 30:
		print("Определяем положение игры")
		print("Подождите...")
		print()

if allFine:
	for x in range(0, 39):
		gui.moveTo(Xs[x], Ys[x])
		time.sleep(0.05)

	mainButtonX, mainButtonY = gui.locateCenterOnScreen("imgs/start.png")
	gui.click(mainButtonX, mainButtonY)

toClick = []
while allFine:
	if MouseCloseCorner():
		break

	try:
		if gui.pixelMatchesColor(mainButtonX, mainButtonY, (0, 0, 0)):
			for x in toClick:
				gui.click(Xs[x], Ys[x])
				time.sleep(0.05)
			gui.moveTo(mainButtonX, mainButtonY)
			toClick = []
	except:
		print("Error: Не получается проверить цвет пикселя по центру")

	for x in range(0, 39):
		try:
			if gui.pixelMatchesColor(Xs[x], Ys[x], (255, 255, 255)):
				toClick += [x]
				time.sleep(0.5)
		except:
				print("Error: Не получается проверить цвет пикселя")
				
print("Программа завершена!")
input()