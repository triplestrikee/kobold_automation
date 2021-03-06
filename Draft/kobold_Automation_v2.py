import shutil
import os
from time import sleep
from datetime import datetime

# for xbox files

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

# shutil.rmtree(copy_file_destination_path)


# os.chdir(output_path)
# print(os.getcwd())
#list all the files in the files folder
print ('----------------List of all the files ----------------')
source_files = os.listdir(source_path)
os.chdir(source_path)

source_file_name = []
for f in source_files:
   file_name, file_ext = os.path.splitext(f)
   source_file_name.append(file_name)
  #  print(file_name)
  #  print(source_file_name)

# remove duplicated elements
source_file_name = list(set(source_file_name))

source_file_name_bpb = source_file_name[0] + '.bpb'
source_file_name_exe = source_file_name[0] + '.exe'
source_file_name_info = source_file_name[0] + '.info'
source_file_name_pdb = source_file_name[0] + '.pdb'

source_file_name_bpb_compressed = source_file_name_bpb + '.gz' 
source_file_name_exe_compressed = source_file_name_exe + '.gz'
source_file_name_pdb_compressed = source_file_name_pdb + '.gz'

print(source_file_name_bpb )
print(source_file_name_exe )
print(source_file_name_info) 
print(source_file_name_pdb )

print('output-    -------------------------')
print(source_file_name_bpb_compressed)  
print(source_file_name_exe_compressed) 
print(source_file_name_pdb_compressed) 

  #  print(file_ext)
  #  info = os.stat(f)
  #  print(info.st_size)
# sleep(300)

print ('----------------List of all the files ----------------')
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


# print ('----------------List of all the files ----------------')
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

#   #  print(file_name.split('.'))
#   #  info = os.stat(f)
#   #  print(info.st_size)