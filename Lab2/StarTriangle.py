while True:
    x = int(input('Please give an integer in range 3 to 9: '))
    if(x < 3 or x > 9): continue
    else: break
for count in range(1, x+1):
    print(count*"*")
for count in range(x+1, 0, -1):
    print(count*"*")
