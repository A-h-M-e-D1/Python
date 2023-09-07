# This App used To File organizer
import os
import shutil

# Show folders and files 
my_files = os.listdir()
print(my_files)

# Define file types and their corresponding folders
my_folders = {
    '.py': 'Python Programs',
    '.txt':'files txt',
    '.pdf':r"C:\Users\DELL\Documents\html\sheets",
    
}

# Get user input for file name
file_name = input("Enter File name: ")

# Check if file type is in dictionary and move file to corresponding folder
# if file_name.endswith('.py'):
#     move_file = shutil.move(file_name, my_folders['.py'])
#     print(f"{file_name} moved to {my_folders['.py']} folder")
    
# elif file_name.endswith('.txt'):
#     move_file = shutil.move(file_name, my_folders['.txt'])
#     print(f"{file_name} moved to {my_folders['.txt']} folder")
# elif file_name.endswith('.pdf'):
#     move_file=shutil.move(file_name,my_folders['.pdf'])
#     print(f"{file_name} moved to {my_folders['.pdf']} folder")
    
# else:
#     print("Invalid file type")

