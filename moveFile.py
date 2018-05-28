import shutil
import os
from time import sleep
from datetime import datetime


#Enter a new folder name
new_folder_name = 'greeting'
src_files_path = 'C:\Kobold_Test_Files\output'
des_files_path = 'C:/Users/hashen/Desktop/Kobold - Automation(Draft)/' + new_folder_name

# os.mkdir(input_path)
#print('Before copy operation: ' )
shutil.copytree(src_files_path, des_files_path)

#shutil.copy('moveFile.py', 'nimabbb')
print ('List of all the files ----------------')
# print(os.listdir(des_files_path))
des_files = os.listdir(src_files_path)

#remove folder and all contents
sleep(5)
shutil.rmtree(des_files_path)