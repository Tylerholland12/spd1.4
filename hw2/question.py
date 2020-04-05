# Given a non-empty array of digits representing a non-negative integer,
#  plus one to the integer.

# Questions
# -----------
# Are the numbers sorted?

# Assumptions
# -----------
# We know that each element in the array contains a single digit
# The array is only containing digits
# It does not matter if there are positives or negeatives

# How I would solve this
# -----------
# I would start by creating a function that takes in the array variable and the setting up a 
# loop that searches for the last item in the array and once that item is found I will increase
# that value by one 

numbers = [2, 4, 5, 6]

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

