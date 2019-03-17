import random

operator = ["-", "+", "*", "/"]

while True:
	useoperator = random.choice(operator)
	a = random.randint(1,1000)
	b = random.randint(1,1000)
	if useoperator == "-":
		result = a - b
	if useoperator == "+":
		result = a + b
	if useoperator == "*":
		a = random.randint(1,10)
		b = random.randint(1,10)
		result = a * b
	if useoperator == "/":
		a = random.randint(1,100)
		b = random.randint(1,a)
		result = a // b
	print(a, useoperator, b, " = ")
	user_result = input("> ")
#	user_result = input(a + useoperator + b + " = ")
	if user_result == str(result):
		print("Spravne!")
	elif user_result == "quit":
		break
	else:
		while user_result != str(result):
#			user_result = input("Spatne :-( Zkus to jeste jednou! \n" + a + useoperator + b" = ")
			print("Spatne :-( Zkus to jeste jednou! \n", a, useoperator, b, " = ")
			user_result = input("> ")
			if user_result == "quit":
				print("Spravny vysledek je ",result ," ty troubo!")
				break
		if user_result == str(result):
			print("Spravne!")

	
