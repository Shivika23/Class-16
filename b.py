#file = open('New_filee.txt','x')
#file.close()

import os
print("Checking if file exists or not..")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("File doesn't exist.")

file_2 = open("my_file.txt", 'w')
file_2.write("Hello world.")
file_2.close()


os.remove("New_file.txt")
os.remove("New_filee.txt")
