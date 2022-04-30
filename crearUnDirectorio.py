#import necessary module
import os

#the name of my folder
dir = "mySuperCoolFolder"

#parent directory
parent_dir = "D:\G-W-F\python\APIs\intento1"

#path
path = os.path.join(parent_dir, dir)

#create dir
os.mkdir(path)

#two ways to say the same
print("Directory '%s' created " %dir)
print(f"Directory '{dir}' created")