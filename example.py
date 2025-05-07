import os

# Write/Open a file
"""with open('example.txt','w') as myFile:
    myFile.write("This is my new file\n")
    myFile.write("Hello World!")"""

# Read a file
"""with open('example.txt','r') as myFile :
    content=myFile.read()
    print(content)"""

# Rename a file
# os.rename('example.txt','example.text')

# Delete a file
# os.remove('example.txt')

# Create a folder
# os.mkdir('python_record')

# Rename a folder
# os.rename('python_record','practiceWithRabbil')

# Delete a folder
# os.rmdir('python_record1')

# try-except >> error/handle
"""try:
  os.rmdir('sagcu')
except Exception as error:
  print(f"Something went wrong {error}")
"""