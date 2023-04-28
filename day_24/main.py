# Reading a file in python
file = open("day_24/Input/Letters/starting_letter.txt")
contents = file.read()
print(contents)

# Closing a file
file.close()

# Writing to a file in python
with open("day_24/test.txt", mode="a") as file:
    file.write("New Text.")
