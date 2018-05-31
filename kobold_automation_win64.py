#This script support multiple input files

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

# xbox file path
# source_path = r'C:\Kobold_Test_Files\Test XB1 source'
# input_path = r'C:\Kobold_Test_Files\Test XB1 input' 
# output_path = r'C:\Kobold_Test_Files\Test XB1 output'

# wid64 file path
source_path = r'C:\Kobold_Test_Files\Test Win64 source'
input_path = r'C:\Kobold_Test_Files\Test Win64 input' 
output_path = r'C:\Kobold_Test_Files\Test Win64 output'

copy_file_destination_path = input_path 

print(input_path)
print(output_path)
print(copy_file_destination_path)

'''Moving the source files to the destination'''
# shutil.copytree(source_path, copy_file_destination_path)
# sleep(200)

## shutil.rmtree(copy_file_destination_path)


# ----------------List of all the files ----------------
source_files = os.listdir(source_path)
os.chdir(source_path)

source_file_name = []
for f in source_files:
   file_name, file_ext = os.path.splitext(f)
   source_file_name.append(file_name)

# remove duplicated elements
# source_file_name = list(set(source_file_name))
source_files.sort()
source_files.sort()

source_file_name_pdb =  []
source_file_name_bpb =  []
source_file_name_dll =  []
source_file_name_info = []
source_file_name_exe = []
source_file_name_elf = []


for i in range(len(source_files)-1):
  #win64 file
  if source_file_name[i] == source_file_name[i+1] and source_files[i].endswith('.dll') and source_files[i+1].endswith('.pdb'):
    source_file_name_dll.append(source_file_name[i] + '.dll') 
    source_file_name_bpb.append(source_file_name[i] + '.bpb') 
    source_file_name_info.append(source_file_name[i] + '.info') 
    source_file_name_pdb.append(source_file_name[i] + '.pdb') 
  #xbox file
  if source_file_name[i] == source_file_name[i+1] and source_files[i].endswith('.exe') and source_files[i+1].endswith('.pdb'):
    source_file_name_exe.append(source_file_name[i] + '.exe')        
    source_file_name_bpb.append(source_file_name[i] + '.bpb') 
    source_file_name_info.append(source_file_name[i] + '.info') 
    source_file_name_pdb.append(source_file_name[i] + '.pdb') 
  #ps4 file
  if source_files[i].endswith('.efl'):
    source_file_name_bpb.append(source_file_name[i] + '.bpb')
    source_file_name_elf.append(source_file_name[i] + '.elf')
    source_file_name_info.append(source_file_name[i] + '.info') 

#generate output file names +.gz
compressed_source_file_name_pdb =  []
compressed_source_file_name_bpb =  []
compressed_source_file_name_dll =  []
compressed_source_file_name_exe =  []
compressed_source_file_name_elf = []

for i in range(len(source_file_name_pdb)):
  compressed_source_file_name_pdb.append(source_file_name_pdb[i] + '.gz')

for i in range(len(source_file_name_bpb)):
  compressed_source_file_name_bpb.append(source_file_name_bpb[i] + '.gz')

for i in range(len(source_file_name_dll)):
  compressed_source_file_name_dll.append(source_file_name_dll[i] + '.gz')

for i in range(len(source_file_name_exe)):
  compressed_source_file_name_exe.append(source_file_name_exe[i] + '.gz')

for i in range(len(source_file_name_elf)):
  compressed_source_file_name_elf.append(source_file_name_elf[i] + '.gz')


print('input files--------------------')
print(
source_file_name_pdb, 
source_file_name_bpb, 
source_file_name_dll, 
source_file_name_info, 
source_file_name_exe,
source_file_name_elf
)

print('output files--------------------')

print(
compressed_source_file_name_pdb,
compressed_source_file_name_dll,
compressed_source_file_name_bpb,
compressed_source_file_name_exe,
compressed_source_file_name_elf
)


print ('----------------List of all files in the input folder ----------------')
input_files = os.listdir(input_path)
os.chdir(input_path)
input_file_name = []
for f in input_files:
   input_file_name.append(f) 

#check the presnece of each file
for i in range(len(source_file_name_bpb)):
  if source_file_name_bpb[i] in input_file_name:
    print('Yes')
  else:
    print("missing: ", source_file_name_bpb[i])

for i in range(len(source_file_name_pdb)):
  if source_file_name_pdb[i] in input_file_name:
    print('Yes')
  else:
    print("missing: ", source_file_name_pdb[i])

for i in range(len(source_file_name_dll)):
  if source_file_name_dll[i] in input_file_name:
    print('Yes')
  else:
    print("missing: ", source_file_name_dll[i])

for i in range(len(source_file_name_exe)):
  if source_file_name_exe[i] in input_file_name:
    print('Yes')
  else:
    print("missing: ", source_file_name_exe[i])

for i in range(len(source_file_name_info)):
  if source_file_name_info[i] in input_file_name:
    print('Yes')
  else:
    print("missing: ", source_file_name_info[i])



print ('----------------List of all files in the output folder ----------------')
output_files = os.listdir(output_path)
os.chdir(output_path)
output_file_name = []
for f in output_files:
  output_file_name.append(f)

#checking the presence of each compressed file
for i in range(len(compressed_source_file_name_pdb)):
  if compressed_source_file_name_pdb[i] in output_file_name:
    print('Yes')
  else:
    print("missing: ", compressed_source_file_name_pdb[i])


for i in range(len(compressed_source_file_name_dll)):
  if compressed_source_file_name_dll[i] in output_file_name:
    print('Yes')
  else:
    print("missing: ", compressed_source_file_name_dll[i])

for i in range(len(compressed_source_file_name_bpb)):
  if compressed_source_file_name_bpb[i] in output_file_name:
    print('Yes')
  else:
    print("missing: ", compressed_source_file_name_bpb[i])

for i in range(len(compressed_source_file_name_exe)):
  if compressed_source_file_name_exe[i] in output_file_name:
    print('Yes')
  else:
    print("missing: ", compressed_source_file_name_exe[i])

