import random

# Based on CS70 Discussion 10A Question 3 "Mario's Coins"

# Define the heads probability of each coin
coins = [1/4, 1/2, 3/4]

# Helper functions
def flipCoin(coinNum): # flips coin and returns True if heads, False if tails
  rand = random.uniform(0,1)
  return rand < coins[coinNum]

def randCoin(): # returns random coin index
  return random.randint(0, len(coins) - 1)

def randCoinList(): # returns random combination of coin indecies
  return random.sample(range(len(coins)), len(coins)) 


# Mario randomly picks a single coin and flips it once
# What is the probability that the flip shows heads?
def testSingleFlip(numIter):
  successes = 0
  for _ in range(numIter):
    if flipCoin(randCoin()):
      successes += 1
  print(f"successes: {successes}")
  rate = successes/numIter
  print(f"success rate: {rate:.2f}")
  print(f"expected rate: {1/2:.2f}")
  return rate

# Mario randomly picks a single coin and flips it twice
# What is the probability that both flips show heads?
def testDoubleFlip(numIter):
  successes = 0
  for _ in range(numIter):
    theCoin = randCoin()
    if flipCoin(theCoin):
      if flipCoin(theCoin):
        successes += 1
  print(f"successes: {successes}")
  rate = successes/numIter
  print(f"success rate: {rate:.2f}")
  print(f"expected rate: {7/24:.2f}")
  return rate

# Mario arranges his three coins in a row.
# He flips the coin on the left, which shows heads
# He then flips the coin in the middle, which shows heads
# Finally, he flips the coin on the right.
# What is the probability that it also shows heads?
def testC(numIter):
  successes = 0
  for _ in range(numIter):
    for i in randCoinList():
      if not flipCoin(i):
        break
      if i == len(coins)-1:
        successes += 1
  print(f"successes: {successes}")
  rate = successes/numIter
  print(f"success rate: {rate:.2f}")
  print(f"expected rate: {9/22:.2f}")
  return