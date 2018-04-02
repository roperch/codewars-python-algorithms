min([-52, 56, 30, 29, -54, 0, -110]) --> -110
min([42, 54, 65, 87, 0]) --> 0
max([4,6,2,1,9,63,-134,566]) --> 566
max([5]) --> 5

def min(arr):
  min = arr[0]
  for num in arr:
      if num < min:
          min = num
  return min

def max(arr):
  max = arr[0]
  for num in arr:
      if num > max:
          max = num
  return max
