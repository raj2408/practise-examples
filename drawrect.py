def space():
    print(' ' * (length-2), end='')
    print('*')

length = int(input())
breadth =int(input())

# for i in range (0,length) :
#     print ('*', end = '')
print('*'*length, end='')
print('')
for i in range(0,breadth -2):
    print ('*',end ='')
    space()
print('*'*length, end='')



