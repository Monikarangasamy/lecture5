#Finding the square root the number with approximation method

x = 36
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guess = 0
while abs(guess**2-x) >= epsilon:
    guess += increment
    num_guess += 1
    print(f'num_guess ={num_guess}')
    print(f'{guess} is close to square root of {x}')
    
# same problem in another way

    x = int(input("Enter a number to find square root: "))
epsilon = 0.01
guess = 0.0
increment = 0.00001
num_guess = 0
while abs(guess*2-x) >= epsilon and (guess*2) <= x:
    guess += increment
    num_guess += 1
print('Number of guesses =', num_guess)
if abs(guess**2-x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(guess, 'is close to square root of', x)

#output
Enter a number to find square root:  36
Number of guesses = 1799501
Failed on square root of 36

# sample program 3

x = 36
epsilon = 0.01
guess = 0.0
increment = 0.00001 #try with 0.00001
num_guess = 0
while abs(guess*2-x) >= epsilon and (guess*2) <= x:
    guess += increment
    num_guess += 1
print(f'Number of guesses = {num_guess}')
if abs(guess**2-x) >= epsilon:
    print(f'Failed on square root of {x}')
    print(f'last guess was {guess}')
    print(f'last guess square is {guess*guess}')
else:
    print(f'{guess}is close to square root of {x}')

#Binary

x = int(input('Enter an integer: '))
result = ''
negflag = False
if x < 0:
    negflag = True
    x = abs(x)
elif x == 0:
    result = 0
while x > 0:
    result = str(x%2) + result
    x = x//2
if negflag:
    result = '-' + result
print(result)