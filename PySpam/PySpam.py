import pyautogui
import time

print("PySpam")
print("By NoName")
print("V1.2 Release")
print()

message = input("Какое отправить сообщение?   ")

while True:
	try:
		amount = int(input("Какое Кол-во раз отправить сообщение?   "))
		break
	except ValueError:
		print("Введите целое число...")

while True:
	try:
		duration = float(input("С какой задержкой в сек отправлять сообщения?   "))
		break
	except ValueError:
		print("Введите число...")

print()
print("После нажатия \"Enter\" начнёться таймер на 10сек")
print("За это время вы должны выделить текстовое поле")
print("P.S. Что бы остановить спам пошевелите мышкой")

input()
time.sleep(10)

print("Статус:")
print("Прошло времени : Сообщений отправлено")

mousePos = pyautogui.position()
statusTime = time.time()

for x in range(0, amount):
	if x == round(amount / 5 * 1):
		print(str(round(time.time() - statusTime, 2)) + ":" + str(x))

	if x == round(amount / 5 * 2):
		print(str(round(time.time() - statusTime, 2)) + ":" + str(x))

	if x == round(amount / 5 * 3):
		print(str(round(time.time() - statusTime, 2)) + ":" + str(x))

	if x == round(amount / 5 * 4):
		print(str(round(time.time() - statusTime, 2)) + ":" + str(x))

	if mousePos != pyautogui.position():
		break

	pyautogui.typewrite(message)
	pyautogui.press("enter")
	time.sleep(duration)

print(str(round(time.time() - statusTime, 2)) + ":" + str(x + 1))
print(str(round(amount / (time.time() - statusTime), 2)) + "/сек")
print()

print("Программа завершена!")
input()