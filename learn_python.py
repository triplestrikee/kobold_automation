# import the follwoing modulars
import datetime
import sys
import os

str = input('Please enter a string: ')
count = 0
for i in range(len(str)):
  if(str[i] == ' '):
    count = count + 1

print('Number of the whitespace in the string is: ',count)

print('Hi ni hao {}'.format(count))

now = datetime.datetime.now()
newDirName = "Kobold_XB1_Test " + now.strftime("%Y_%m_%d-%H%M")
print(newDirName)
