str = input('Please enter a string: ')
count = 0
for i in range(len(str)):
  if(str[i] == ' '):
    count = count + 1

print('Number of the whitespace in the string is: ',count)

print('Hi ni hao {}'.format(count))