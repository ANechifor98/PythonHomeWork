from threading import Thread, Lock, Event
import time, random

mutex = Lock()
customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15

class BarberShop:
	waitingCustomers = []

	def __init__(self, barber, numberOfSeats):
		self.barber = barber
		self.numberOfSeats = numberOfSeats
		print('BarberShop initilized with {0} seats'.format(numberOfSeats))
		print('Customer min interval {0}'.format(customerIntervalMin))
		print('Customer max interval {0}'.format(customerIntervalMax))
		print('Haircut min duration {0}'.format(haircutDurationMin))
		print('Haircut max duration {0}'.format(customerIntervalMax))
		print('---------------------------------------')

	def openShop(self):
		print('Barber shop opens')
		workingThread = Thread(target = self.barberGoToWork)
		workingThread.start()

	def barberGoToWork(self):
		while True:
			mutex.acquire()
			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]
				del self.waitingCustomers[0]
				mutex.release()
				self.barber.cutHair(c)
			else:
				mutex.release()
				print('Barber sleeps')
				barber.sleep()
				print('Barber wakes up')
	
	def enterBarberShop(self, customer):
		mutex.acquire()
		print('\n>> {0} entered the shop and is looking for a seat'.format(customer.name))
		if len(self.waitingCustomers) == self.numberOfSeats:
			print('Waiting room is full, {0} is leaving.'.format(customer.name))
			mutex.release()
		else:
			print('{0} sat down in the waiting room'.format(customer.name))
			self.waitingCustomers.append(c) 
			mutex.release()
			barber.wakeUp()

class Customer:
	def __init__(self, name):
		self.name = name

class Barber:
	barberWorkingEvent = Event()

	def sleep(self):
		self.barberWorkingEvent.wait()

	def wakeUp(self):
		self.barberWorkingEvent.set()

	def cutHair(self, customer): 
		self.barberWorkingEvent.clear()
		print('{0} is having a haircut'.format(customer.name))
		randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax+1)
		time.sleep(randomHairCuttingTime)
		print('{0} is done'.format(customer.name))


if __name__ == '__main__':
	customers = []
	customers.append(Customer('6'))
	customers.append(Customer('7'))
	customers.append(Customer('8'))
	customers.append(Customer('9'))
	customers.append(Customer('1'))
	customers.append(Customer('2'))
	customers.append(Customer('3'))
	customers.append(Customer('4'))
	customers.append(Customer('5'))
	customers.append(Customer('10'))
	customers.append(Customer('11'))
	barber = Barber()
	barberShop = BarberShop(barber, numberOfSeats=10)
	barberShop.openShop()

	while len(customers) > 0:
				c = customers.pop()
				barberShop.enterBarberShop(c)
				customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1)
				time.sleep(customerInterval)
