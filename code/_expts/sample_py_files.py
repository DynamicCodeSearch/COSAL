"""
def bubbleSort(nums):
  for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
  return nums

def bubbleSort(array):
  n = len(array)
  for i in range(n):
    swops = 0
    for j in range(i+1, n):
      if array[j] < array[i]:
        array[j], array[i] = array[i], array[j]
        swops += 1
    if swops == 0:
      break

def bubbleSort(arr):
  swap = True
  while swap:
    swap = False
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        x = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = x
        swap = True

def bubblesort(l):
  for pasada in range(1, len(l)-1):
    for i in range(0,len(l)-1):
      if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]
  return 0

def bubblesort(X):
  N = X.shape[0]
  for end in range(N, 1, -1):
    for i in range(end - 1):
      cur = X[i]
      if cur > X[i + 1]:
        tmp = X[i]
        X[i] = X[i + 1]
        X[i + 1] = tmp

def bubblesort(lst):
  for i in range(len(lst)-1):
    for j in range(len(lst)-1):
      if (lst[j]>lst[j+1]):
        t=lst[j]
        lst[j]=lst[j+1]
        lst[j+1]=t
  return lst

def BubbleSort(list):
  i=0
  while i<len(list) - 1:
    if list[i] > list[i+1]:
      tmp = list[i]
      list[i] = list[i+1]
      list[i+1] = tmp
      i=0
    else:
      i +=1
  return list

def bubble(lst):
  for i, val1 in enumerate(lst):
    for j, val2 in enumerate(lst):
      if lst[i] < lst[j]:
        lst[i], lst[j] = lst[j], lst[i]
  return lst
"""