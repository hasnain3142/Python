name = input("Enter your name: ")
print("Hello There,",name,"\nThink of an integer between any desired range...I will try to guess it")
input("Enter when ready...")
print("Now, tell me range of your number")
high = int(input("Enter highest limit: "))                                                #Maximum Range Limit
low = int(input("Enter lowest limit: "))                                                  #Minimum Range Limit
from math import log,ceil,floor                                                             #Imported three functions from module named math
guesses = ceil(log(high-low,2))+1                                                        #We implemented a formula of binary bisection
print("So",name,"now, I am gonna ask some questions in order to guess your number\nPlease answer the following questions in yes or no.\nPress 'y' or 'Y' for yes and 'n' or 'N' for no\n\
I'll have total",guesses,"guesses, whenever I will guess a wrong value my no of guesses will decrease")
input("Alright?")
print("Let's Start")
myguess = int((high+low)/2)                                                               #Using Binary Bisection , first guess should be the average of max and min range
count = 0
while True:                                                                                           #We started an infinite while loop which will break  when we will guess the number
    count += 1
    ans = input(f"Is the value {myguess}? ")                                         #First, we took input a character which will be the central point of further algorithm
    ans = ans.upper()                                                                            #We capitalized the character in case user entered a lower case character
    if ans =="Y":                                                                                    #If user answered yes we will terminate the loop, as we guessed the number 
        break
    elif ans != "Y" and ans != "N":
        count -= 1
        print("Error: Please answer using either 'Y' or 'N'")
        input("Press any key to continue")
        continue
    ans = input(f"Is the value greater than {myguess}? ")               #If user won't answer yes, we will ask another question and skip the upper if block
    ans = ans.upper()
    if ans =="Y":                                                                                 #If user answered yes to our second question positively,
        low = myguess                                                                         #We increased our lowest limit to our guess and ignored all values in between
        myguess = ceil((myguess+high)/2)                                         #We also adjusted our guess according to new range
    elif ans =="N":                                                                             #If user answered no to our second question
        high = myguess                                                                       #We  decreased our maximum limit to our guess and ignored all values in between 
        myguess = floor((myguess+low)/2)                                        #We also adjusted our guess according to range
    else:
        count -= 1
        print("Error: Please answer using either 'Y' or 'N'")
        input("Press any key to continue")
        continue
print("The value you chose is:",myguess)                                      #While loop will terminate when we will guess the number and then this statement would be printed
print("I guessed your number in",count,"attempts\nHence my score is",guesses-count)
