import shutil
import os
from time import sleep
import datetime
import sys

# set up the test environment
now = datetime.datetime.now()
newFolderName = "Kobold_XB1_Test_" + now.strftime("%Y_%m_%d_%H%M")
print(newFolderName)

new_asserts_test_folder_name = 'greeting3' 
source_path = r'C:\Kobold_Test_Files\Test XB1 source'
input_path = r'\\eac-fs1.eac.ad.ea.com\cqe_kobold$\eac-kobold-dev\Input\dev\ManualBuildCopyTests\XB1' +'/' + new_asserts_test_folder_name
output_path = r"\\eac-fs1.eac.ad.ea.com\cqe_kobold$\eac-kobold-dev\Output\eac-kobold-dev\Input\dev\ManualBuildCopyTests\XB1" +'/' + new_asserts_test_folder_name
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
source_file_name = list(set(source_file_name))

#create file names
source_file_name_bpb = source_file_name[0] + '.bpb'
source_file_name_exe = source_file_name[0] + '.exe'
source_file_name_info = source_file_name[0] + '.info'
source_file_name_pdb = source_file_name[0] + '.pdb'

source_file_name_bpb_compressed = source_file_name_bpb + '.gz' 
source_file_name_exe_compressed = source_file_name_exe + '.gz'
source_file_name_pdb_compressed = source_file_name_pdb + '.gz'

print('----------------------all file names--------------------------')
print(source_file_name_bpb )
print(source_file_name_exe )
print(source_file_name_info) 
print(source_file_name_pdb )

print(source_file_name_bpb_compressed)  
print(source_file_name_exe_compressed) 
print(source_file_name_pdb_compressed) 



print ('----------------List of all files in the input folder ----------------')
input_files = os.listdir(input_path)
os.chdir(input_path)
input_file_name = []
for f in input_files:
   input_file_name.append(f) 

print(input_file_name)


if source_file_name_bpb in input_file_name:
  print('Yes')
else:
  print("no")

if source_file_name_exe in input_file_name:
  print('Yes')
else:
  print("no")

if source_file_name_info in input_file_name:
  print('Yes')
else:
  print("no")
  
if source_file_name_pdb in input_file_name:
  print('Yes')
else:
  print("no")


print ('----------------List of all files in the output folder ----------------')
output_files = os.listdir(output_path)
os.chdir(output_path)
output_file_name = []
for f in output_files:
  output_file_name.append(f)
   
print(output_file_name)

if source_file_name_bpb_compressed in output_file_name:
  print('Yes')
else:
  print("no")

if source_file_name_exe_compressed in output_file_name:
  print('Yes')
else:
  print("no")

if source_file_name_pdb_compressed in output_file_name:
  print('Yes')
else:
  print("no")
