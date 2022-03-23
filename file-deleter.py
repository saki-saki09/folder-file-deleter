import os
file = input("Which file do you want to delete?\n")
if os.path.exists(file):
  os.remove(file)
  print("\n'%s' file successfully deleted!" % file)
else:
  print("\n'%s' file doesn't exist..." % file)