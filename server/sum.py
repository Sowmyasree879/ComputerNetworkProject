import sys  # Import the sys module

# Get the number of command-line arguments
length = len(sys.argv)

# Get the list of command-line arguments, excluding the first argument (which is the script name)
arg_list = sys.argv[1:]

# Initialize a sum variable to 0
sum = 0

# Iterate over the list of arguments and add each one to the sum variable after converting it to an integer
for i in arg_list:
    sum += int(i)

# Print the sum of the command-line arguments
print(sum)
