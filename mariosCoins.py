import random

coins = [1/4, 1/2, 3/4]

def flipCoin(coinNum):
  rand = random.uniform(0,1)
  return rand < coins[coinNum]

def randCoin():
  return random.randint(0, len(coins) - 1)

def testSingleFlip(numIter):
  successes = 0
  for i in range(numIter):
    if flipCoin(randCoin()):
      successes += 1
  print(f"successes: {successes}")
  rate = successes/numIter
  print(f"success rate: {rate:.2f}")
  return rate

def testDoubleFlip(numIter):
  successes = 0
  for i in range(numIter):
    theCoin = randCoin()
    if flipCoin(theCoin):
      if flipCoin(theCoin):
        successes += 1
  print(f"successes: {successes}")
  rate = successes/numIter
  print(f"success rate: {rate:.2f}")
  return rate