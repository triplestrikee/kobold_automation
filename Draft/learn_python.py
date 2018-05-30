# import the follwoing modulars
import datetime
import sys
import os

myStr = input('Please input a string: ')

def countWhiteSpace(str):
  count = 0
  for i in range(len(str)):
    if(str[i] == ' '):
      count += 1
  return count

print('Number of the whitespace in the string is: ',countWhiteSpace(myStr))
print('Number of the whitespace in the input string is: {}'.format(countWhiteSpace(myStr)))

now = datetime.datetime.now()
newDirName = "Kobold_XB1_Test_" + now.strftime("%Y_%m_%d-%H%M")
print(newDirName)

