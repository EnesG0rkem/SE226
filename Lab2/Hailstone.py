x = int(input('Please give an integer: '))
step = 0
print(x, end=' ')
while x!= 1 :
    step += 1
    if x % 2 == 0 :
        x //= 2
    else: 
        x = x*3 +1
    print(' -> ',x,end=' ')
else:
    print('\nTotal number of steps: ', step)
