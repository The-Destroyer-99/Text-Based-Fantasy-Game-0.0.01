from time import sleep as slp
import os
import random
import sys
import time

# variable list
# fancylineshort
# fancylinelong
# startmenuinput
# typehere
# username
# credits
# backstoryp1 to p8
# backstory_yn
# loadingtime
# LTfloat
# inlval

inval = "Invalid Input"

def fasttype(a):
  for b in a:
    time.sleep(0.005)
    sys.stdout.write(b)
    sys.stdout.flush()

def midtype(a):
  for b in a:
    time.sleep(0.03)
    sys.stdout.write(b)
    sys.stdout.flush()

def kindaslowtype(a):
  for b in a:
    time.sleep(0.043)
    sys.stdout.write(b)
    sys.stdout.flush()

def slowtype(a):
  for b in a:
    time.sleep(0.1)
    sys.stdout.write(b)
    sys.stdout.flush()

fancylineshort = "{[//|/||\\=_-_=/||\\|\\\\]}"
fancylinelong = "{\\\\_______/[/.**.-{.._..}-.**.\\]\\_______//}"

credits = """Owner|Lead Game Dev:
TheDestroyer99|Ayden Q.

-\__/-+-=~~~~=-+-\__/-

Lead Helper\\Game Dev:
Christopher Dai
"""

typehere = ">> "
backstoryp1 = '''Work In Progress'''
backstoryp2 = '''Work In Progress'''
backstoryp3 = '''Work In Progress'''
backstoryp4 = '''Work In Progress'''
backstoryp5 = '''Work In Progress'''
backstoryp6 = '''Work In Progress'''
backstoryp7 = '''Work In Progress'''
backstoryp8 = '''Work In Progress'''


loadingtime = random.randint(1, 4)
slp(loadingtime)
print("Loading")
loadingtime = random.randint(1, 4)
slp(loadingtime)
os.system('clear')
print("Loading.")
loadingtime = random.randint(1, 4)
slp(loadingtime)
os.system('clear')
print("Loading..")
loadingtime = random.randint(1, 4)
slp(loadingtime)
os.system('clear')
print("Loading...")
loadingtime = random.randint(1, 4)
slp(loadingtime)
os.system('clear')
print("Loading....")
loadingtime = random.randint(1, 4)
slp(loadingtime)
os.system('clear')
print("Done!!!")
loadingtime = random.randint(1, 4)
slp(loadingtime)
os.system("clear")

while True:
	slp(2)

	os.system("clear")
	
	kindaslowtype("""Hello!!

Start
Credits
Leave
How To Play

""" + str(typehere))

	startmenuinput = input()
	slp(1)
	os.system("clear")


	if startmenuinput.lower() == "leave":
		os._exit
	elif startmenuinput.lower() ==	"credits":
		slowtype(credits)
	elif startmenuinput.lower() == "how to play":
	 print("WIP")
	elif startmenuinput.lower() == "start":
		LTfloat = random.random()
		slp(LTfloat)
		print("Loading")
		LTfloat = random.random()
		slp(LTfloat)
		os.system("clear")
		print("Loading.")
		LTfloat = random.random()
		slp(LTfloat)
		os.system("clear")
		print("Loading..")
		LTfloat = random.random()
		slp(LTfloat)
		os.system("clear")
		print("Loading...")
		LTfloat = random.random()
		slp(LTfloat)
		os.system("clear")
		print("Welcome!!!\n")
		break
	else:
		fasttype(inval)

midtype('''
Would You Like To Know The Backstory?

Yes
No

''')

backstory_yn = input(typehere)

if backstory_yn.lower() == "yes" :
	kindaslowtype(backstoryp1)
elif backstory_yn.lower() == "no" :
	pass
else :
	print(inval)