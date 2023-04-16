import sys  # Import the sys module

# Get the list of command-line arguments, excluding the first argument (which is the script name)
args_list = sys.argv[1:]

# Convert the list of string arguments to a list of integers using a list comprehension
args_list = [int(i) for i in args_list]

# Sort the list of integers in ascending order
args_list.sort()

# Convert the list of integers back to a list of strings using a list comprehension
args_list = [str(i) for i in args_list]

# Join the list of strings using commas and assign the result to a variable
Sort = ','.join(args_list)

# Print the list of sorted integers as a comma-separated string
print(Sort)
