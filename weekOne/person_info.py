# Function to store information about a person in a dictionary and print it
def store_person_info():
    # Create an empty dictionary to store person's information
    person_info = {}

    # Ask the user for input and store the information in the dictionary
    person_info['name'] = input("Enter your name: ")
    person_info['age'] = input("Enter your age: ")
    person_info['favorite_color'] = input("Enter your favorite color: ")

    # Print the dictionary containing person's information
    print("Person's information:")
    print(person_info)

# Main program
if __name__ == "__main__":
    store_person_info()
