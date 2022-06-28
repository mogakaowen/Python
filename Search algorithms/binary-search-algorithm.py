def binary_search(a_list, item):
    
    first = 0
    last = len(a_list) - 1
    i=0
    
    while first <= last:
        i = (first + last) / 2
        i=int(i)
        if a_list[i] == item:
            return i
        elif a_list[i] > item:
            last = i - 1
        else:
            first = i + 1
    return -1

a_list=[1,2,3,4,5,6,7,8]
item=input('Enter element to be found: ')
item=int(item)

result=binary_search(a_list, item)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element was not found in the list")


#OR
def binary_search(a_list, item):
    
    first = 0
    last = len(a_list) - 1
    
   
    while first <= last:
        i = (first + last) / 2
        i=int(i)
        if a_list[i] == item:
            return 'The number {item} was found at position {i}'.format(item=item, i=i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
    return 'The number {item} was not found in the list'.format(item=item)

a_list=[1,2,3,4,5,6,7,8]
item=input('Enter element to be found: ')
item=int(item)


result=binary_search(a_list, item)

print(result)

#Recursive binary search
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
        # Element is not present in the array
    else:
        return -1
 
# Test array
arr = [1,2,3,4,5,6,7,8]
x = input("Number to be found: ")
x=int(x)
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


#OR

def binary_search_recursive(a_list, first, last, item):

    if last>=first:
        i = (first + last) // 2

        if a_list[i] == item:
            return 'The number {item} was found at position {i}'.format(item=item, i=i)

        elif a_list[i] > item:
            last=i-1
            return binary_search_recursive(a_list, first, last, item)

        else:
            first=i+1
            return binary_search_recursive(a_list, first, last, item)

    else:
        return 'The number {item} was not found in the list'.format(item=item)

a_list=[1,2,3,4,5,6,7,8]
item=input('Enter element to be found: ')
item=int(item)
first = 0
last = len(a_list) - 1

result=binary_search_recursive(a_list, first, last, item)
print(result)