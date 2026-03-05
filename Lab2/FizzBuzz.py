while True:
    x = int(input('Please give an integer in the range of 10 and 100: '))
    if(x<10 or x>100): continue
    else: break
fizzCounter = 0
buzzCounter = 0
fizzBuzzCounter = 0

for num in range(1,x+1):
    if num % 7 == 0: continue
    if num % 3 == 0 and num % 5 == 0: 
        print("FizzBuzz")
        fizzBuzzCounter += 1
    elif num % 3 == 0: 
        print("Fizz")
        fizzCounter += 1
    elif num % 5 == 0: 
        print("Buzz")
        buzzCounter += 1
    else: print(num)

print("--- Summary ---",
      "\nFizz count: ", fizzCounter,
      "\nBuzz count: ", buzzCounter,
      "\nFizzBuzz count: ", fizzBuzzCounter
)