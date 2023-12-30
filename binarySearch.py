# if target exist return target else return - 1

nums = [-1, 0, 1, 2, 3,4,7,9, 10, 20];

def binarySearch(list, left, right, target):
    if left >  right:
        return -1
    
    mid = (left + right) // 2

    if list[mid] == target:
        return target
    
    if(list[mid] < target):
        return binarySearch(list, mid + 1, right, target)
    
    return binarySearch(list, left, mid - 1, target)

print(binarySearch(nums, 0, len(nums) - 1, 16))