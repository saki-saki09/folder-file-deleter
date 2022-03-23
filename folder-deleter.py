import os
folder = input("Which file do you want to delete?\n")
if os.path.exists(folder):
  os.rmdir(folder)
  print("\n'%s' folder successfully deleted!" % folder)
else:
  print("\n'%s' folder doesn't exist..." % folder)