#Some fill text for now.
import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [21, 19, 17, 4, 27, 20, 10, 18, 23, 22, 6, 5, 13, 12, 26, 16, 25, 24, 15] #top to bottom is easiest
def setup():
	for x in range(len(pinList)):
		GPIO.setup(pinList[x], GPIO.OUT)
def on(pin):
	GPIO.output(pinList[pin], GPIO.HIGH)

def off(pin):
	GPIO.output(pinList[pin], GPIO.LOW)

def allOn():
	for x in range(len(pinList)):
		GPIO.output(pinList[x], GPIO.HIGH)
	
def allOff():
	for x in range(len(pinList)):
		GPIO.output(pinList[x], GPIO.LOW)

def invert(pin):
	input = GPIO.input(pinList[pin])
	if input:
		GPIO.output(pinList[pin], GPIO.LOW)
	else:
		GPIO.output(pinList[pin], GPIO.HIGH)

def allInvert():
	for x in range(len(pinList)):
		input = GPIO.input(pinList[x])
		if input:
			GPIO.output(pinList[x], GPIO.LOW)
		else:
			GPIO.output(pinList[x], GPIO.HIGH)

def countUp(delay, inv):
	input = GPIO.input(pinList[0])
	if (inv == 1):
		allOn()
	else:
		allOff()
	if not input:
		if (inv != 1):
			on(0)
	if (inv == 1):
		off(0)
	time.sleep(delay)
	for x in range(1, len(pinList)):
		off(x - 1)
		on(x)
		if (inv == 1):
			invert(x)
			invert(x - 1)
		time.sleep(delay)
	if (inv == 1):
		on(len(pinList) - 1)
	else:
		off(len(pinList) - 1)
def countDown(delay, inv):
	y = len(pinList) - 1
	input = GPIO.input(pinList[y])
	if (inv == 1):
		allOn()
	else:
		allOff()
	if not input:
		if (inv != 1):
			on(y)
	if (inv == 1):
		off(y)
	time.sleep(delay)
	for x in range(1, len(pinList)):
		off(y)
		on(y - 1)
		if (inv == 1):
			invert(y)
			invert(y - 1)
		time.sleep(delay)
		y-=1
	if (inv == 1):
		on(0)
	else:
		off(0)

def alternate(alt):
	x = alt
	y = len(pinList) / 2
	for z in range(0, y):
		on(x)
		x+=2

def upOn(delay):
	for x in range(0, len(pinList)):
		input = GPIO.input(pinList[x])
		if not input:
			on(x)
			time.sleep(delay)

def upOff(delay):
	for x in range(0, len(pinList)):
		input = GPIO.input(pinList[x])
		if input:
			off(x)
			time.sleep(delay)

def downOn(delay):
	y = len(pinList) - 1
	for x in range(0, len(pinList)):
		input = GPIO.input(pinList[y])
		if not input:
			on(y)
			time.sleep(delay)
		y-=1

def downOff(delay):
	y = len(pinList) - 1
	for x in range(0, len(pinList)):
		input = GPIO.input(pinList[y])
		if input:
			off(y)
			time.sleep(delay)
		y-=1



def randList():
	usedPin = [len(pinList)]
	for y in range(0, len(pinList) - 1):
		usedPin.append(len(pinList))
	usedPin[0] = random.randint(0, len(pinList) - 1)
	for x in range (1 ,len(pinList)):
		uniqe = 1
		while (uniqe != 0):
			uniqe = len(usedPin)
			next = random.randint(0, len(pinList) - 1)
			for y in range(0, len(usedPin)):
				if (next != usedPin[y]):
					uniqe-=1
		usedPin[x] = next
	return usedPin

def randOn(delay):
	list = randList()
	for x in list:
		on(list[x])
		time.sleep(delay)

def randOff(delay):
	list = randList()
	for x in list:
		off(list[x])
		time.sleep(delay)

def shortRandList():
	usePin = []
	size = random.randint(1, 5)
	for x in range(0, size):
		usePin.append(len(pinList))
	usePin[0] = random.randint(0, len(pinList) - 1)
	if (size != 1):
		for x in range(1, len(usePin)):
			uniqe = 1
			while (uniqe != 0):
				uniqe = len(usePin)
				next = random.randint(0, len(pinList) - 1)
				for y in range(0, len(usePin)):
					if (next != usePin[y]):
						uniqe -= 1
			usePin[x] = next
	return usePin	

def twinkleOff():
	use = shortRandList()
	print (use)
	offTime = random.uniform(.1, .2)
	betweenTime = random.uniform(.5, 1.0)
	for x in range(0, len(use)):
		off(use[x])
	time.sleep(offTime)
	for x in range(0, len(use)):
		on(use[x])
	allOff()
	time.sleep(betweenTime)

def twinkleOn():
	use = shortRandList()
	print (use)
	offTime = random.uniform(.1, .2)
	betweenTime = random.uniform(.5, 1.0)
	for x in range(0, len(use)):
		on(use[x])
	time.sleep(offTime)
	for x in range(0, len(use)):
		off(use[x])
	allOn()
	time.sleep(betweenTime)

#allOn()
#allOff()
#allInvert()
#countUp(delay, inv)
#countDown(delay, inv)
#alternate(alt) (alt: 0 or 1)
#upOn(delay)
#upOff(delay)
#downOn(delay)
#downOff(delay)
#randOn(delay)
#randOff(delay)
#twinkleOff()
#twinkleOn()

setup()
isOff = 1
allOff()
while True:
	if isOff:
		next = random.randint(0, 8)
		if (next == 0):
			allOn()
			isOff = 0
		if (next == 1):
			alternate(0)
			time.sleep(.2)
			iter = random.randint(5, 15)
			for x in range(0, iter):
				allInvert()
				time.sleep(.2)
			leave = random.randint(0, 1)
			if (leave == 0):
				allOn()
				isOff = 0
			if (leave == 1):
				allOff()
				isOff = 1
		if (next == 2):
			countUp(.2, 0)
			isOff = 1
		if (next == 3):
			countDown(.2, 0)
			isOff = 1
		if (next == 4):
			isDown = random.randint(0, 1)
			if isDown:
				countDown(.2, 0)
				countUp(.2, 0)
			else:
				countUp(.2, 0)
				countDown(.2, 0)
			isOff = 1
		if (next == 5):
			randOn(.2)
			isOff = 0
		if (next == 6):
			twinkleOff()
			isOff = 1
		if (next == 7):
			upOn(.2)
			isOff = 0
		if (next == 8):
			downOn(.2)
			isOff = 0
	if not isOff:
		next = random.randint(0, 7)
		if (next == 0):
			allOff()
			isOff = 1
		if (next == 1):
			countUp(.2, 1)
			isOff = 0
		if (next == 2):
			countDown(.2, 1)
			isOff = 0
		if (next == 3):
			isDown = random.randint(0, 1)
			if isDown:
				countDown(.2, 1)
				countUp(.2, 1)
			else:
				countUp(.2, 1)
				countDown(.2, 1)
			isOff = 0
		if (next == 4):
			randOff(.2)
			isOff = 1
		if (next == 5):
			twinkleOn()
			isOff = 0
		if (next == 6):
			upOff(.2)
			isOff = 1
		if (next == 7):
			downOff(.2)
			isOff = 1
