#1
def sum_to (n):
  if n == 1:
    return 1
  return n + sum_to(n-1)

print(sum_to(10))

#2
def largest (nums):
  #accepting an array of numbers
  nums.sort()
  #sorting the array from smallest to largest
  return nums[-1]
  #-1 returns the last number which would be the largest

print(largest([5, 2, 6, 9]))

#3
def occurrences (str, strg):
  input()

#4
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product