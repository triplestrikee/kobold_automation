str = input('Please enter a string here: ')
count = 0
for i in range(len(str)):
  if str[i] == ' ':
    count = count + 1

print('The number of white space in the string is: ', count) 
print('The string you entered is: ', str) 



