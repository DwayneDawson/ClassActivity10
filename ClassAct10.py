import random
import math
import string

def checkPrime(n): 
    n = abs(int(n))

    if n < 2:
        return False

    if n == 2: 
        return True    

    if not n & 1: 
        return False

    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True
   
def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


#Retrieving student number
StudentNr = input("0. The student number is: ")
SNsplit = [int(i) for i in str(StudentNr)] 

primeNumbers = 0

for i in range(0,len(SNsplit)):
    if (checkPrime(SNsplit[i])) : 
        primeNumbers = primeNumbers + 1 

if (primeNumbers == 0):
    p = 1
    print("1. The number of Prime Numbers in this student number is: ",p)
else:
    p = primeNumbers
    print("1. The number of Prime Numbers in this student number is: ",p)

#Getting a random number between 25 and 50
q = random.randint(25,51)
print("2. The random number is: ", q)

# Division of (random number)/(prime numbers)
r = math.floor(q/p)
print("3. The number of strings to be generated is: ",r)

#Generate list of strings (i=0 -> r-1)
arrayWords = []
evenTest = True

for i in range(r):
    if (evenTest == True):
        arrayWords.append(randomString(5))
        evenTest = False
    else:
        arrayWords.append(randomString(7))
        evenTest = True

print("4. List of strings")
print("**********************************")
for i in range(r):
    print(i," - ",arrayWords[i])
print("**********************************")