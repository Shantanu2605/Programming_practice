#1- Requires password to excess the code!
import colorama
from colorama import Fore

password= 'Password123'
for i in range(1):
    pwd= input(Fore.BLUE + "Enter Password to run the code: ")
    c=1
    if pwd== password:
        print(Fore.LIGHTRED_EX+"Program opened!")

    else:
        print(Fore.YELLOW+ "Incorrect password, try again! You've 3 more chances left")
        pwd= input(Fore.BLUE + "Enter Password to run the code: ")

        if pwd == password:
            print(Fore.LIGHTRED_EX+"Program opened! Re-Enter the Password to run the code!!")
        else:
            print(Fore.YELLOW+ "Incorrect password, try again! You've 2 more chances left")

        pwd= input(Fore.BLUE + "Enter Password to run the code: ")

        if pwd == password:
            print(Fore.LIGHTRED_EX+"Program opened!")
        else:
                print(Fore.YELLOW+ "Incorrect password, try again! You've 1 more chance left OR the program would be blocked")
                pwd= input(Fore.BLUE + "Enter Password to run the code: ")
                if pwd == password:
                    print(Fore.LIGHTRED_EX+"Program opened!")

                else:
                    print(Fore.RED+ "Invalid Password, it seems like you're stranger!")
                    print(Fore.RED+ "--PROGRAM BLOCKED - NO ACCESS--")
                    exit()

print(Fore.WHITE+ "-----------------------------------")
print(Fore.WHITE+"*************************")
print(Fore.WHITE+"PROGRAM OVERVIEW:- ")








List= ["Monday,","Tuesday,","Wednesday,","Thursday,","Friday,","Saturday,","Sunday,",":))"]
a,b,c,d,e,f,g,h= List
print(Fore.GREEN+'Days of the week are:', a,b,c,d,e,f,g,h)
print('& Reverse days of the week are:',g,f,e,d,c,b,a,h)

#2-
a= ["SKS","John","Leonard","John","SKS","John","Tyson","Dave","Leonard","Stella","Stella","John","SKS","Dave","Tyson"]
print("------------------------------")
print("Most frequently occuring name is:", max(set(a),
                                                   key= a.count))
print("& ")
print("Least frequently occuring name is:", min(set(a),
                                                key= a.count))

print("------------------------------------------")
b= [45,88,92,97,44,45,92,85,79,100,79,44,88.7,73.4,88,92,97,45,85,97,88,79,100,92,79,88,62,88]
print("Most frequently occuring number is:", max(set(b),
                                                   key= b.count))
print("Now guess the least frequently occured number!!")
print("The least frequently number is:", min(set(b),
                                            key= b.count))


#5-
myname= "Anurag Rajpoot Singh"[::-1]
print(myname)

#6- (Tells you whether a name is the same to read as by back)

name= 'wow'
isPalindrome= name.find(name[::-1])==0
print(isPalindrome)

#7-
try:
    num= int(input(Fore.LIGHTBLUE_EX+ "Enter a number: "))
except Exception as e:
    print(e)

table= [num*i for i in range(1,21)]
print(Fore.LIGHTMAGENTA_EX+ f"You entered {num}")
print(Fore.LIGHTMAGENTA_EX+ f"Table from 1 to 20 for {num} are as follows:-")
print(table)


#8- A simple and small chatbot
import time
import camelcase
time.sleep(1)
print(Fore.LIGHTWHITE_EX+"Do you want to chat with chatbot ?")
ans= input("(y/n)?: ")
time.sleep(0.25)
if ans== 'y':
    print("Starting your conversation...")
elif ans== 'n':
        exit()
time.sleep(1)
print("Almost done")
time.sleep(1)
print("===========================================================================================================")
time.sleep(0.5)
print(Fore.LIGHTBLUE_EX+ "Hi, I'm Franklin and I'm a chatbot, what's your name?")
print("(To exit the chat anytime, just say 'bye')")
MyName= input("My name is: ")
if 'bye' in MyName or 'exit' in MyName:
    exit()
x= camelcase.main.CamelCase()
v= x.hump(MyName)
time.sleep(0.15)
print("Typing...")
time.sleep(1)
print(f"Nice to meet you {v}")
h1= input(": ")
if h1== 'bye':
    exit()
elif h1== 'who are you?':
    print("Typing...")
    time.sleep(0.89)
    print("I'm a chatbot created by a Pro Developer and Data Scientist, Shantanu")
time.sleep(0.15)
print("Typing...")
time.sleep(1)
print(f"What are your hobbies {v} ?")
human1= input(": ")
if human1== 'bye':
    exit()
time.sleep(0.12)
print("Typing...")
time.sleep(1)
human1= human1.replace('my hobbies are', '')
print(f"Are your hobbies really {human1}?")
an2= input(": ")
if an2== 'bye' or an2== 'Bye' or an2== 'Bye!':
    exit()
elif an2== 'no' or an2== 'No' or an2== 'Nope':
    print("Then ?")
    ans2= input(": ")
    print("Typing...")
else:
 print("Typing...")
time.sleep(1)
print("Ohk... that's nice")
time.sleep(0.25)
print("What are you doing nowadays ?")
human3= input(": ")
if human3 == 'bye':
    exit()
time.sleep(0.15)
print("Typing...")
time.sleep(1)
print("Whoa! seems a little bit interesting XD")
time.sleep(0.35)
human2= input("My question to you is: ")
if human2== 'bye':
    exit()
elif human2== 'who are you?' or human2=='who created you?' or human2=='Who are you' or human2=='who made you':
    print("Typing...")
    time.sleep(0.65)
    print("I'm a chatbot created by a Pro Developer and Data Scientist, Shantanu")
elif human2== 'what is Data Science?' or human2=='What is data science?' or human2=='What is data science':
    print("Typing...")
    time.sleep(0.95)
    print("Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems "
          "to extract knowledge and insights from noisy, structured and unstructured data, "
          "and apply knowledge and actionable insights from data across a broad range of application domains."
          "If you don't trust me, you can also go to https://www.google.com/search?q=data+science&oq=Data+Sc&aqs=chrome.1.69i57j0i433i512l3j0i512j0i433i457i512j0i402l2j0i512l2.5207j0j7&sourceid=chrome&ie=UTF-8")
else:
 print("Typing...")
 time.sleep(1)
 print("That's kind of a weird question")
human4= input(":")
if human4== 'bye' or human4=='Bye' or human4=='bye!':
    exit()
if human4== 'really?' or human4=='Really' or human4=='Really?':
    print("Typing...")
    time.sleep(0.5)
    print("Yes, please ask something meaningful.")
    ans1= input(": ")
else:
 print("Typing...")
 time.sleep(0.35)
 print("I didn't understand what you're trying to say")
human5= input(": ")
if human5== 'bye':
    exit()
print("Typing...")
time.sleep(0.45)
print("Oh.. So how can I help you with that ?")
time.sleep(0.35)
print("Have I any role in that ?")
human6= input(": ")
if human6== 'bye':
    exit()
elif human6 == 'no' or human6 == 'No' or human6 == 'not at all':
    print("Typing...")
    time.sleep(0.5)
    print("Ok fine, bye")
    exit()
elif human6== 'yes' or human6=='Yes' or human6=='Yup':
    print("Typing...")
    time.sleep(0.67)
    print("Really ? "
          "I don't think so, "
          "Lol...")
    h2= input(": ")
    if h2 == 'bye':
        exit()
    print("Typing...")
    time.sleep(0.4)
    print("Am I clever?")
    h21= input(": ")
    if h21 == 'bye':
        exit()
    elif 'yes' in h21:
        print("Typing...")
        time.sleep(0.67)
        print("Thank You!")
    elif 'no' in h21:
        print("Typing...")
        time.sleep(0.67)
        print("Yeah, actually I need more data to be better")

        time.sleep(1)
    print("Hey listen to me, I've got to do some work, so I'll talk with you later. "
          "Have a nice day!")
else:
    print("Typing...")
    time.sleep(0.3)
    print("HmMMm?? what do you wanna say?")
    time.sleep(0.49)
    print("You're rude... I'll talk with you later")




















