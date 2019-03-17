f = open("scores.txt", "w")

while True:
	participant = input("Participant name > ")
	if participant == "quit":
		print("Finished")
		break
	score = input("Score for " + participant + "> ")
	f.write(participant + "," + score + "\n")

f.close()

