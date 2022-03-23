import os
file = input("Which file do you want to delete?\n")
if os.path.exists(file):
  os.remove(file)
  print("\n'%s' file successfully deleted!" % file)
else:
  print("\n'%s' file doesn't exist..." % file)

"""
This is a trial file for Python Practice... By using this... when you run this file to your terminal... 
You have to write your file name and press "Enter"... By pressing "Enter" the file will be deleted...

Θ But here's a CONDITION that the file that you want to delete by using this 'file-deleter.py', must exist at the same folder Θ
"""
