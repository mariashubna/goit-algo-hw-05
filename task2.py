def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0


    iter = 0
    

 
    while low <= high:
        iter += 1 

 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            upper_border = arr[mid]
            return iter, upper_border
 
    # якщо елемент не знайдений
    return -1

arr = [2.1, 3.1, 3.3, 3.4, 3.45, 4.4, 5.7, 10.2, 15.5, 17.8, 40.6]
x = 5.7
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
