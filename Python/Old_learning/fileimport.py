import sys
import random

if len(sys.argv) < 2:
	print("Provide file name:")
	exit(1)

filename = sys.argv[1]
f = open(filename, "r")
dicti = {}

for i in f:
	value = (i.strip().split(","))
#	value1 = value[0]
#	value2 = value[1]
#	dicti[value1] = value[2]
	dicti[value[0]] = value[1]
f.close()
questions = list(dicti.keys())
while True:
	question = random.choice(questions)
	answer = dicti[question]
	userinput = input("Opoved na \"" + question + "\" je?:")
	if userinput == "quit":
		break
	elif answer == userinput:
		print("Correct")
	else:
		print("WRONG!! HAHAHAHA!! :-P LOOOOOOSER!!")
		print("There is hint for you dummy:")
		print(dicti)
