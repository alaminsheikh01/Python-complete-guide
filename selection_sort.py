def findsmaller(arr):
  smallest = arr[0]
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
  return smallest_index    


def selectionsort (arr):
  newarr = []
  for i in range(len(arr)):
    smallest = findsmaller(arr)
    newarr.append(arr.pop(smallest))
  return newarr

print(selectionsort([2,4,6,1,8]))  
