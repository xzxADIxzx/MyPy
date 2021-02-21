import time
import random

# ABCDEFGHIJKLMNOPQRSTUVWYXZ
# АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
# 0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwYyXxZz
# АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя !?.,:;@#`+-*/=%$&_\(){}[]<>"'
translation = {"0": "000", "1": "001", "2": "002", "3": "003", "4": "004", "5": "005", "6": "006", "7": "007", "8": "008", "9": "009", 
			   "A": "010", "a": "011", "B": "012", "b": "013", "C": "014", "c": "015", "D": "016", "d": "017", "E": "018", "e": "019", 
			   "F": "020", "f": "021", "G": "022", "g": "023", "H": "024", "h": "025", "I": "026", "i": "027", "J": "028", "j": "029", 
			   "K": "030", "k": "031", "L": "032", "l": "033", "M": "034", "m": "035", "N": "036", "n": "037", "O": "038", "o": "039", 
			   "P": "040", "p": "041", "Q": "042", "q": "043", "R": "044", "r": "045", "S": "046", "s": "047", "T": "048", "t": "049", 
			   "U": "050", "u": "051", "V": "052", "v": "053", "W": "054", "w": "055", "Y": "056", "y": "057", "X": "058", "x": "059", 
			   "Z": "060", "z": "061", 
			   "А": "070", "а": "071", "Б": "072", "б": "073", "В": "074", "в": "075", "Г": "076", "г": "077", "Д": "078", "д": "079", 
			   "Е": "080", "е": "081", "Ё": "082", "ё": "083", "Ж": "084", "ж": "085", "З": "086", "з": "087", "И": "088", "и": "089", 
			   "Й": "090", "й": "091", "К": "092", "к": "093", "Л": "094", "л": "095", "М": "096", "м": "097", "Н": "098", "н": "099", 
			   "О": "100", "о": "101", "П": "102", "п": "103", "Р": "104", "р": "105", "С": "106", "с": "107", "Т": "108", "т": "109", 
			   "У": "110", "у": "111", "Ф": "112", "ф": "113", "Х": "114", "х": "115", "Ц": "116", "ц": "117", "Ч": "118", "ч": "119", 
			   "Ш": "120", "ш": "121", "Щ": "122", "щ": "123", "Ъ": "124", "ъ": "125", "Ы": "126", "ы": "127", "Ь": "128", "ь": "129", 
			   "Э": "130", "э": "131", "Ю": "132", "ю": "133", "Я": "134", "я": "135", 
			   " ": "140", "!": "141", "?": "142", ".": "143", ",": "144", ":": "145", ";": "146", "@": "147", "#": "148", "`": "149", 
			   "+": "150", "-": "151", "*": "152", "/": "153", "=": "154", "%": "155", "$": "156", "&": "157", "_": "158", "\\": "159", 
			   "(": "160", ")": "161", "{": "162", "}": "163", "[": "164", "]": "165", "<": "166", ">": "167", "\"": "168", "\'": "169"}

def invTran(translation):
	inv = []
	for x in translation.keys():
		inv.append((translation[x], x))
	return dict(inv)

def move(string, isEncrypt):
	global key
	key0 = int(str(key)[0])
	stringStart = ""
	stringEnd = ""
	if isEncrypt:
		for x in range(0, len(string) - key0):
			stringStart += string[x]
		for x in range(0, key0):
			stringEnd += string[len(string) - key0 + x]
	else:
		for x in range(0, key0):
			stringStart += string[x]
		for x in range(key0, len(string)):
			stringEnd += string[x]
	return stringEnd + stringStart

def charToInt(string):
	stringCon = ""
	for x in string:
		try:
			stringCon += translation[x]
		except :
			stringCon += "888"
	return stringCon

def intToChar(string):
	stringCon = ""
	string = [string[x: x + 3] for x in range(0, len(string), 3)]
	invTranslation = invTran(translation)
	for x in string:
		try:
			stringCon += invTranslation[x]
		except :
			stringCon += "~"
	return stringCon

def evenNotEven(string, isEncrypt):
	global key
	keySum = 0
	for x in str(key):
		keySum += int(x)
	stringMod = ""
	for x in range(0, len(string)):
		number = int(string[x])
		if x % 2 == key % 2:
			if isEncrypt:
				number += keySum
				while number > 9:
					number -= 10
			else:
				number -= keySum
				while number < 0:
					number += 10
			stringMod += str(number)
		else:
			stringMod += string[x]
	return stringMod

def addRandomNumbers(string):
	global key
	stringStart = ""
	stringEnd = ""
	for x in range(0, len(str(key)) ** 2):
		stringStart += str(random.randint(0, 9))
	for x in range(0, len(str(key))):
		stringEnd += str(random.randint(0, 9))
	return stringStart + string + stringEnd

def delRandomNumbers(string):
	global key
	stringCls = ""
	for x in range(0, len(str(string)) - len(str(key)) ** 2 - len(str(key))):
		stringCls += string[x + len(str(key)) ** 2]
	return stringCls

def addKeyInPower(string, isEncrypt):
	for x in range(0, 998):
		y = 1000 - x
		if len(str(int(message) + key ** y)) <= len(string):
			if isEncrypt:
				return str(int(message) + key ** y)
			else:
				return str(int(message) - key ** y)
	return string

def addKeySqrt(string, isEncrypt):
	global key
	keySqrt = str(round(key ** .5))
	stringMod = ""
	for x in string:
		if isEncrypt:
			number = int(x) + int(keySqrt[0])
			while number > 9:
				number -= 10
		else:
			number = int(x) - int(keySqrt[0])
			while number < 0:
				number += 10
		stringMod += str(number)
	return stringMod

def reverse(string):
	stringRev = []
	for x in string:
		stringRev += [x]
	stringRev.reverse()
	return "".join(stringRev)

print("PyCrypt")
print("By xzxADIxzx")
print("V1.0 Release")
print()

time.sleep(1)

print("E/D")
while True:
	ED = input("Зашифровать/Расшифровать? ")
	if ED != "E" and ED != "D":
		print("Введите E или D...")
	else:
		print()
		break

time.sleep(1)

message = input("Введите сообщение: ")
while True:
	try:
		key = abs(int(input("Введите ключ: ")))
		if key > 99999:
			break
		else:
			print("Введите минимум 6 значное число...")
	except ValueError:
		print("Введите целое число...")
print()

time.sleep(1)

if ED == "E":
	message = move(message, True)
	message = charToInt(message)
	message = evenNotEven(message, True)
	message = addRandomNumbers(message)
	message = addKeyInPower(message, True)
	message = addKeySqrt(message, True)
	message = reverse(message)
else:
	message = reverse(message)
	message = addKeySqrt(message, False)
	message = addKeyInPower(message, False)
	message = delRandomNumbers(message)
	message = evenNotEven(message, False)
	message = intToChar(message)
	message = move(message, False)

print("Вывод: " + str(message))
print("Программа завершена!")
input()