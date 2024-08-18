# import os 

# files = os.listdir("rename-file-using-py/figures")
# i = 1
# for file in files:
#     if file.endswith(".png"):
#         print(files)
#         os.rename(f"rename-file-using-py/figures/{file}", f"rename-file-using-py/figures/{i}.png")
#         i = i+1


import os

# Path to the directory containing png files
directory = 'rename-file-using-py/figures'

# Fetch all files in the directory
files = os.listdir(directory)

# Filter out all non-png files
png_files = [file for file in files if file.endswith('.png')]

# Sort files alphabetically to maintain an order before renaming
png_files.sort()

# Rename each png file numerically
for index, file_name in enumerate(png_files):
    # Define new file name as index starting from 1.png
    new_file_name = f"{index + 1}.png"
    
    # Define source and destination paths for renaming
    src_path = os.path.join(directory, file_name)
    dst_path = os.path.join(directory, new_file_name)
    
    # Rename file
    os.rename(src_path, dst_path)
