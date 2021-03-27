#Program to chat with user
#Goal Basic:
# Hi,Hello,Morning,Bye- Greetings
def Chat():
	while True:
		botq=input("You can ask me anything:")
		# print(botq)
		MorningGreet=["Morning","Good Morning","Gm"]
		nightGreet=["good night","Good night","gn","GN"]
		greeting=["Hi","Hello","helllo","Hieee","Hie","heeee","Hi babu"]
		byeGreet=["Bye","Good bye","good bye tc"]
		if botq in MorningGreet:
			print("Bot: Good Morning user")
		elif botq in greeting:
			print("Bot: Hello user")
		elif botq in byeGreet:
			print("Bot: Bye user !")
		elif botq in nightGreet:
			print("Bot: Good night user")
		else:
			print("Im learning..")
Chat()	

