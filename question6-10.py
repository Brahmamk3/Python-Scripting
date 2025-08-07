# Q6.count  files types of .py, .txt
import os
text_count=0
py_count=0

for file in os.listdir(os.getcwd()):
  if file.endswith(".txt"):
    text_count+=1
  elif file.endswith(".py"):
    py_count+=1
print("text files:",text_count,"python files:",py_count)

# Q7.rename all .txt files by adding new string before file name
import shutil
for file in os.listdir(os.getcwd()):
  if file.endswith(".txt"):
    os.rename(file,"new_"+file)

# Q8. Remove first 4 characters from all .txt file names : new_text1.txt
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt") and len(file) > 4:
      print(file)
      new_name = file[4:]
      os.rename(file, new_name)
      print(f"Renamed: {file} -> {new_name}")

# Q9.print all file and folder sizes in kb of file along with name
for file in os.listdir(os.getcwd()):
  print(f"{file} size is:{os.path.getsize(file)}kb")

#Q10.sort the files by types : .py comes first and .txt 

py_files=[]
txt_files=[]
for file in os.listdir(os.getcwd()):
  if file.endswith(".txt"):
    txt_files.append(file)
  elif file.endswith(".py"):
    py_files.append(file)

sorted_files=py_files+txt_files

for file in sorted_files:
  print(file)




    
