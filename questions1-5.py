import os

# Q1.Print current working directory
print(os.getcwd())

# Q2. check if file path is file or directory
file="des.txt"
if(os.path.isfile(file)):
  print("file is present") 
elif (os.path.isdir(file)):
  print("directory is exists")
else :
  print("none of the file and directory is not exists")

# Optional: Check existence using os.path.exists
print("file exists" if os.path.exists(file) else "file not exists")

# Q3.create directory if not exists
directory="data_input"
print("directory is exists" if (os.path.exists(directory)) else os.mkdir(directory))

# Q4.print all .txt files in current folder and print count of that files

path=os.getcwd()
files_count=0
for file in os.listdir(path):
  if file.endswith(".txt"):
    files_count+=1
print(f"text files in {os.getcwd()}:{files_count}")

# Q5. Create directory move the .txt files in current folder to that directory
import shutil
path=os.getcwd()
print("directory is exists" if (os.path.exists("directory")) else os.mkdir("directory"))
for file in os.listdir(path):
  if file.endswith(".txt"):
    shutil.move(file,"directory")

