from tools.numbers.simp import add,subtract
def sumofdigits(number):
    # Ensure the input is a non-negative integer
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

    # Calculate the sum of digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10

   
def ispal(number):
    # Ensure the input is a non-negative integer
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

    # Convert the number to a string
    number_str = str(number)

    # Check if the string is equal to its reverse
    return number_str == number_str[::-1]




