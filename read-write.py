

# Function to modify the content
def modify_content(content):
    # Example modification: converting all text to uppercase
    return content.upper()

# Open and read the file
try:
    with open("input.txt", "r") as infile:
        content = infile.read() 

    # Modify the content
    modified_content = modify_content(content)

    # Write the modified content to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)
    print("File content has been modified and written to 'output.txt'.")

except FileNotFoundError:
    print("The file 'input.txt' was not found.")
except IOError:
    print("There was an error reading or writing the file.")
