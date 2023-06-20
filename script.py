import os

counter = 1

for filename in os.listdir(os.getcwd()):
  file_extension = os.path.splitext(filename)[1]
  print(file_extension)

  if len(filename) > 10:
    new_filename = filename[:9] + "_" + str(counter) + file_extension
  else:
    new_filename = filename + "_" + str(counter) + file_extension

  if new_filename not in os.listdir(os.getcwd()) and filename != "script.py":
    os.rename(filename, new_filename)
  counter += 1
