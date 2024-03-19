# Function to create a list of integers from user input and compute their sum
def compute_sum_of_integers():
    # Get user input for a list of integers separated by spaces
    integer_list = input("Enter a list of integers separated by spaces: ").split()

    # Convert the input strings to integers
    integer_list = [int(num) for num in integer_list]

    # Compute the sum of the integers
    total_sum = sum(integer_list)

    # Print the sum
    print("Sum of the integers:", total_sum)

# Main program
if __name__ == "__main__":
    compute_sum_of_integers()
