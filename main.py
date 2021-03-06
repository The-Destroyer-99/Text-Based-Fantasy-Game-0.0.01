from time import sleep as slp
from os import system as stm
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
# BS1 To BS8
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
BS1 = int(0)
BS2 = int(0)
BS3 = int(0)
BS4 = int(0)
BS5 = int(0)
BS6 = int(0)
BS7 = int(0)
BS8 = int(0)


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
		break
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
	BS1 += 1
elif backstory_yn.lower() == "no" :
	pass
else :
	print(inval)

if BS1 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp1)
else :
	pass

if input("") == """
""" :
	BS2 += 1
else :
	pass

if BS2 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp2)
else :
	pass

if input("")  == """
""" :
	BS3 += 1
else :
	pass

if BS3 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp3)
else :
	pass

if input("")  == """
""" :
	BS4 += 1
else :
	pass

if BS4 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp4)
else :
	pass

if input("")  == """
""" :
	BS5 += 1
else :
	pass

if BS5 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp5)
else :
	pass

if input("")  == """
""" :
	BS6 += 1
else :
	pass

if BS6 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp6)
else :
	pass

if input("")  == """
""" :
	BS7 += 1
else :
	pass

if BS7 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp7)
else :
	pass

if input("")  == """
""" :
	BS8 += 1
else :
	pass

if BS8 == 1 :
	os.stm("clear")
	kindaslowtype(backstoryp8)
else :
	pass

