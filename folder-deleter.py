import os
folder = input("Which file do you want to delete?\n")
if os.path.exists(folder):
  os.rmdir(folder)
  print("\n'%s' folder successfully deleted!" % folder)
else:
  print("\n'%s' folder doesn't exist..." % folder)

"""
This is a trial file for Python Practice... By using this... when you run this file to your terminal... 
You have to write your folder name and press "Enter"... By pressing "Enter" the folder will be deleted...

Θ But here's a CONDITION that the folder that you want to delete by using this 'folder-deleter.py', must exist at the same folder Θ
"""
