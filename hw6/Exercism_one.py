# numbers = [2, 4, 5, 6]
numbers = ["6", "&", 8, 4]

def increase_last_item(numbers):
    # loops throught each number until it reaches the last index in the array
    for index in range(len(numbers)-1, -1, -1):
        
        # If the final number in the array is less than 9(single digits only) then incrinment that number by 1
        if numbers[index] < 9:
            numbers[index] += 1
            # return all numbers and make
            return numbers
        numbers[index] = 0
    return [1] + numbers

# prints all of the numbers
print(increase_last_item(numbers))