import shutil
import os
from time import sleep
import datetime
import sys

# create the test folder
now = datetime.datetime.now()
newFolderName = "Kobold_XB1_Test_" + now.strftime("%Y_%m_%d_%H%M")
print(newFolderName)

# new_asserts_test_folder_name = 'greeting3' 

# wid64 file path
source_path = r'C:\Kobold_Test_Files\Test Win64 source'
input_path = r'C:\Kobold_Test_Files\Test Win64 input' 
output_path = r'C:\Kobold_Test_Files\Test Win64 output'

# xbox file path
# source_path = r'C:\Kobold_Test_Files\Test XB1 source'
# input_path = r'C:\Kobold_Test_Files\Test XB1 input' 
# output_path = r'C:\Kobold_Test_Files\Test XB1 output'

# PS4 file path
# source_path = r'C:\Kobold_Test_Files\Test PS4 source'
# input_path = r'C:\Kobold_Test_Files\Test PS4 source input' 
# output_path = r'C:\Kobold_Test_Files\Test PS4 source output'

copy_file_destination_path = input_path + '\\' + newFolderName

# input_path + '\\' + newFolderName
# output_path + '\\' + newFolderName

# set up the flag
pass_the_script_flag = 1

print(input_path)
print(output_path)
print(copy_file_destination_path)

'''Moving the source files to the destination'''
shutil.copytree(source_path, copy_file_destination_path)
# sleep(200)

## shutil.rmtree(copy_file_destination_path)