import matplotlib.pyplot as plt
from random import randint as rnd
amountOfDice = int(input('Hur många tärningar vill du kasta?'))
amount = int(input('Hur många gånger vill du kasta?'))
amountOfSides = int(input('Hur många sidor ska tärningarna ha?'))

sum = []
frequency = []
plt.plot(sum, frequency[amountOfDice:])

for i in range(amountOfSides*amountOfDice+1):
   frequency.append(int('0'))

def throw(diceAmount, diceSides):
   sumOfThrow = 0
   if len(sum) < amountOfSides*2 - amountOfDice:
      for i in range(amountOfDice, amountOfDice*amountOfSides+1):
         sum.append(i)
   for i in range(diceAmount):
      sumOfThrow = sumOfThrow + rnd(1, diceSides)
   return sumOfThrow

for i in range(amount):
   throws = throw(amountOfDice, amountOfSides)
   frequency[throws] = frequency[throws] + 1
   plt.clf()
   plt.plot(sum, frequency[amountOfDice:])
   plt.pause(0.05)
      
plt.plot(sum, frequency[amountOfDice:], 'g')
plt.show()