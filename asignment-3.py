def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as infile:
        original_content = infile.read()
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Could not read the file.")
else:
    modified_content = modify_content(original_content)
    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to {new_filename}")
    except IOError:
        print("Error: Could not write to the new")