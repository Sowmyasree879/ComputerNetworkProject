import sys  # Import the sys module

# Get the first command-line argument, which is a string
# Note: sys.argv[0] is the name of the Python script itself
parameter = sys.argv[1]

# Reverse the string using slice notation and assign it to txt
# Note: [::-1] slice notation means the entire string with a step of -1, effectively reversing it
txt = parameter[::-1]

# Print the reversed string
print(txt)
