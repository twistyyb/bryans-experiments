import random
import math

# CS 70 Sp25 Note 18 Coupon Collecting
# Written 4/3/25 by Bryan Huang
# Tests the coupon colleting concept with probability and union bounds
# obtain all n coupons within m tries that give a random coupon


# from n possible coupons, try up to m times to get all n coupons
# return number of tries it took or -1 if limit was reached
def collect(n,m=-1):
  coupons = [0] * n
  countIter = 0
  while 0 in coupons:
    gotCoupon = random.randint(0, n - 1)
    coupons[gotCoupon] += 1
    countIter += 1
    if m > 0 and m < countIter:
      return -1

  return countIter


# with n coupons to collect, run collect num times
# return average number of tries to obtain all n coupons
def collectAvg(n, num):
  print(f"expecting (nln(n) + n): {math.floor(n*math.log(n)+n)}")
  nums = []
  for i in range(num):
    nums.append(collect(n))
  average = sum(nums) / len(nums) 
  print(f"average: {average:.2f}")


# with n coupons to collect, only try m = nln(n)+n times, num runs
# return rate at which m tries resulted in successfully obtaining all n coupons
def collectProb(n, num):
  m = math.floor(n*math.log(n)+n)
  returns = []
  for i in range(num):
    returns.append(collect(n, m))
  newReturns = list(filter(lambda x: x >= 0, returns))
  prob = len(newReturns)/num
  print(f"expected rate >=: {1-1/math.e}")
  print(f"success rate: {prob:.2f}")